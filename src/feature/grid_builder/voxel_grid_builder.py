import os
import numpy as np
import open3d as o3d
import pandas as pd

from .voxel_grid_dto import VoxelGridDto
from ..preprocess import PreprocessedDto
from ...common.logger import ILogger
from ...model import AutoGluon
from ... import Config


class VoxelGridBuilder:
    __auto_gluon: AutoGluon
    __logger: ILogger
    __voxel_mesh: o3d.geometry.TriangleMesh
    __voxel_grid_dto: VoxelGridDto

    def __init__(self, auto_gluon_model: AutoGluon, logger: ILogger) -> None:
        self.auto_gluon = auto_gluon_model
        self.logger = logger
        self.voxel_mesh = o3d.geometry.TriangleMesh()

        self.trees = []
        self.buildings = []
        self.river = []
        self.terrain = []

        self.build(self.auto_gluon.test_dto)

    @property
    def auto_gluon(self) -> AutoGluon:
        return self.__auto_gluon

    @auto_gluon.setter
    def auto_gluon(self, auto_gluon: AutoGluon) -> None:
        self.__auto_gluon = auto_gluon

    @property
    def logger(self) -> ILogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: ILogger) -> None:
        self.__logger = logger

    @property
    def voxel_mesh(self) -> o3d.geometry.TriangleMesh:
        return self.__voxel_mesh

    @voxel_mesh.setter
    def voxel_mesh(self, voxel_mesh: o3d.geometry.TriangleMesh) -> None:
        self.__voxel_mesh = voxel_mesh

    @property
    def voxel_grid_dto(self) -> VoxelGridDto:
        return self.__voxel_grid_dto

    @voxel_grid_dto.setter
    def voxel_grid_dto(self, voxel_grid_dto: VoxelGridDto) -> None:
        self.__voxel_grid_dto = voxel_grid_dto

    def build(self, dto: PreprocessedDto) -> None:
        grid_index: pd.DataFrame = dto.grid_index
        voxel_color: pd.DataFrame = dto.voxel_color
        max_bound: pd.DataFrame = dto.bounding_box[['max_bound_x', 'max_bound_y', 'max_bound_z']]
        min_bound: pd.DataFrame = dto.bounding_box[['min_bound_x', 'min_bound_y', 'min_bound_z']]
        features: pd.DataFrame = dto.features
        labels: pd.DataFrame = self.auto_gluon.predictions

        labeled_frame: pd.DataFrame = pd.concat([
            grid_index,
            voxel_color,
            max_bound,
            min_bound,
            features,
            labels
        ], axis=1)

        self.logger.info('Building voxel grid...')

        buildings: o3d.geometry.TriangleMesh = o3d.geometry.TriangleMesh()
        river: o3d.geometry.TriangleMesh = o3d.geometry.TriangleMesh()
        terrain: o3d.geometry.TriangleMesh = o3d.geometry.TriangleMesh()
        trees: o3d.geometry.TriangleMesh = o3d.geometry.TriangleMesh()

        def create_bounding_box(
                row: np.ndarray,
                buildings: o3d.geometry.TriangleMesh,
                river: o3d.geometry.TriangleMesh,
                terrain: o3d.geometry.TriangleMesh,
                trees: o3d.geometry.TriangleMesh
        ) -> None:
            label_colors = {
                'buildings': np.array([0.910, 0.502, 0.298]),
                'river': np.array([0.188, 0.765, 0.804]),
                'terrain': np.array([0.882, 0.722, 0.580]),
                'trees': np.array([0.553, 0.773, 0.588]),
            }

            max_bound: np.ndarray = row[6:9]
            min_bound: np.ndarray = row[9:12]
            label: np.ndarray = row[-1]

            bounding_box = o3d.geometry.TriangleMesh.create_box(
                width=max_bound[0] - min_bound[0],
                height=max_bound[1] - min_bound[1],
                depth=max_bound[2] - min_bound[2]
            )

            bounding_box.translate(min_bound)
            bounding_box.paint_uniform_color(label_colors[label])

            voxel_grid: o3d.geometry.TriangleMesh = self.voxel_mesh
            voxel_grid += bounding_box

            if label == 'buildings':
                buildings += bounding_box
            elif label == 'river':
                river += bounding_box
            elif label == 'terrain':
                terrain += bounding_box
            elif label == 'trees':
                trees += bounding_box

            self.voxel_mesh = voxel_grid
            self.logger.debug(f'Bounding box created')

        labeled_frame.apply(lambda row: create_bounding_box(
            row,
            buildings,
            river,
            terrain,
            trees
        ), axis=1)

        dto: VoxelGridDto = VoxelGridDto(
            voxel_grid=self.voxel_mesh,
            buildings=buildings,
            river=river,
            terrain=terrain,
            trees=trees
        )

        self.logger.info('Voxel grid built.')
        self.voxel_grid_dto = dto

    def save_grid(self, mesh: o3d.geometry.TriangleMesh, filename: str) -> None:
        path: str = os.path.join(Config.VOXEL_GRID_DIR.value, f'{filename}.ply')
        o3d.io.write_triangle_mesh(filename=path, mesh=mesh)
        self.logger.info(f'Voxel grid saved to {path}')
