import numpy as np
import open3d as o3d
import pandas as pd

from ...common.utils.conversion import PointCloudTo


class PointDto:
    __point_cloud: o3d.geometry.PointCloud
    __point_cloud_dataframe: pd.DataFrame
    __point_cloud_array: np.ndarray

    def __init__(self, point_cloud: o3d.geometry.PointCloud) -> None:
        self.point_cloud = point_cloud
        self.point_cloud_dataframe = PointCloudTo.dataframe(point_cloud)

        self.point_cloud_array = PointCloudTo.ndarray(point_cloud)

    @property
    def point_cloud(self) -> o3d.geometry.PointCloud:
        return self.__point_cloud

    @point_cloud.setter
    def point_cloud(self, point_cloud: o3d.geometry.PointCloud) -> None:
        self.__point_cloud = point_cloud

    @property
    def point_cloud_dataframe(self) -> pd.DataFrame:
        return self.__point_cloud_dataframe

    @point_cloud_dataframe.setter
    def point_cloud_dataframe(self, point_cloud_dataframe: pd.DataFrame) -> None:
        self.__point_cloud_dataframe = point_cloud_dataframe

    @property
    def point_cloud_array(self) -> np.ndarray:
        return self.__point_cloud_array

    @point_cloud_array.setter
    def point_cloud_array(self, point_cloud_array: np.ndarray) -> None:
        self.__point_cloud_array = point_cloud_array
