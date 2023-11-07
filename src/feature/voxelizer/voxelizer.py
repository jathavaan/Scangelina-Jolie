import numpy as np
import open3d as o3d
from tqdm.notebook import tqdm

from .voxelization_parameters import VoxelizationParameters
from ...common.logger import ILogger


class Voxelizer:
    __point_cloud: o3d.geometry.PointCloud
    __grid: o3d.geometry.VoxelGrid
    __voxels: list[o3d.geometry.Voxel]
    __voxel_bounding_boxes: list[tuple[np.ndarray, o3d.geometry.AxisAlignedBoundingBox]]

    def __init__(
            self,
            point_cloud: o3d.geometry.PointCloud,
            logger: ILogger,
            voxel_size: int = VoxelizationParameters.VOXEL_SIZE.value
    ) -> None:
        self.logger = logger
        self.point_cloud = point_cloud

        grid: o3d.geometry.VoxelGrid = o3d.geometry.VoxelGrid.create_from_point_cloud(
            input=self.point_cloud,
            voxel_size=voxel_size
        )

        if grid.is_empty():
            self.logger.warning("Voxel grid is empty.")
            self.grid = None
        else:
            self.grid = grid

    @property
    def logger(self) -> ILogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: ILogger) -> None:
        self.__logger = logger

    @property
    def point_cloud(self) -> o3d.geometry.PointCloud:
        return self.__point_cloud

    @point_cloud.setter
    def point_cloud(self, point_cloud: o3d.geometry.PointCloud) -> None:
        self.__point_cloud = point_cloud

    @property
    def grid(self) -> o3d.geometry.VoxelGrid:
        return self.__grid

    @grid.setter
    def grid(self, grid: o3d.geometry.VoxelGrid) -> None:
        self.__grid = grid

        self.voxels = self.grid.get_voxels()
        self.logger.info(f"Voxel grid created with {len(self.voxels)} voxels.")

        bounding_boxes: list[tuple[np.ndarray, o3d.geometry.AxisAlignedBoundingBox]] = []

        insufficient_voxels_count: int = 0
        for voxel in self.voxels:
            grid_index: np.ndarray = voxel.grid_index
            voxel_bounding_points: o3d.utility.Vector3dVector = self.grid.get_voxel_bounding_points(grid_index)

            bounding_box: o3d.geometry.AxisAlignedBoundingBox = o3d.geometry.AxisAlignedBoundingBox.create_from_points(
                voxel_bounding_points
            )

            bounding_boxes.append((grid_index, bounding_box))

        self.voxel_bounding_boxes = bounding_boxes

    @property
    def voxels(self) -> list[o3d.geometry.Voxel]:
        return self.__voxels

    @voxels.setter
    def voxels(self, voxels: list[o3d.geometry.Voxel]) -> None:
        self.__voxels = voxels

    @property
    def voxel_bounding_boxes(self) -> list[tuple[np.ndarray, o3d.geometry.AxisAlignedBoundingBox]]:
        return self.__voxel_bounding_boxes

    @voxel_bounding_boxes.setter
    def voxel_bounding_boxes(
            self,
            voxel_bounding_boxes: list[[np.ndarray, o3d.geometry.AxisAlignedBoundingBox]]
    ) -> None:
        self.__voxel_bounding_boxes = voxel_bounding_boxes
        self.logger.debug(f"Created bounding boxes for each voxel.")

    def extract_voxels(self) -> list[tuple[np.ndarray, o3d.geometry.PointCloud]]:
        voxels: list[tuple[np.ndarray, o3d.geometry.Voxel]] = []
        point_cloud: o3d.geometry.PointCloud = self.point_cloud
        bounding_boxes: list[tuple[np.ndarray, o3d.geometry.AxisAlignedBoundingBox]] = self.voxel_bounding_boxes

        insufficient_voxels_count: int = 0
        for i in tqdm(range(len(bounding_boxes)), desc="Extracting voxels..."):
            grid_index: np.ndarray = bounding_boxes[i][0]
            bounding_box: o3d.geometry.AxisAlignedBoundingBox = bounding_boxes[i][1]
            voxel: o3d.geometry.PointCloud = point_cloud.crop(bounding_box)

            if len(voxel.points) < VoxelizationParameters.MIN_VOXEL_POINT_COUNT.value:
                insufficient_voxels_count += 1
                self.logger.debug(f"Voxel {grid_index} has insufficient points ({len(voxel.points)}.")
                continue

            voxels.append((grid_index, voxel))

        self.logger.info(f"Extracted {len(voxels)} voxels, {insufficient_voxels_count} voxels were insufficient.")
        return voxels
