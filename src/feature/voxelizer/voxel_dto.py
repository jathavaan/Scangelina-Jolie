import numpy as np
import open3d as o3d


class VoxelDto:
    __grid_index: np.ndarray
    __bounding_box: o3d.geometry.AxisAlignedBoundingBox
    __point_cloud: o3d.geometry.PointCloud
    __voxel_color: np.ndarray

    def __init__(
            self, grid_index: np.ndarray,
            bounding_box: o3d.geometry.AxisAlignedBoundingBox,
            point_cloud: o3d.geometry.PointCloud,
            voxel_color: np.ndarray
    ) -> None:
        self.grid_index = grid_index
        self.bounding_box = bounding_box
        self.point_cloud = point_cloud
        self.voxel_color = voxel_color


    @property
    def grid_index(self) -> np.ndarray:
        return self.__grid_index

    @grid_index.setter
    def grid_index(self, grid_index: np.ndarray) -> None:
        self.__grid_index = grid_index

    @property
    def bounding_box(self) -> o3d.geometry.AxisAlignedBoundingBox:
        return self.__bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box: o3d.geometry.AxisAlignedBoundingBox) -> None:
        self.__bounding_box = bounding_box

    @property
    def point_cloud(self) -> o3d.geometry.PointCloud:
        return self.__point_cloud

    @point_cloud.setter
    def point_cloud(self, point_cloud: o3d.geometry.PointCloud) -> None:
        self.__point_cloud = point_cloud

    @property
    def voxel_color(self) -> np.ndarray:
        return self.__voxel_color

    @voxel_color.setter
    def voxel_color(self, voxel_color: np.ndarray) -> None:
        self.__voxel_color = voxel_color
