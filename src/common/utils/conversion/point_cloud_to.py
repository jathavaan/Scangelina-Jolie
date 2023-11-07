import numpy as np
import open3d as o3d
import pandas as pd


class PointCloudTo:
    @staticmethod
    def dataframe(point_cloud: o3d.geometry.PointCloud) -> pd.DataFrame:
        points: np.ndarray = np.asarray(point_cloud.points)
        colors: np.ndarray = np.asarray(point_cloud.colors)

        points_dataframe: pd.DataFrame = pd.DataFrame(columns=["x", "y", "z", "r", "g", "b"])
        points_dataframe["x"] = points[:, 0]
        points_dataframe["y"] = points[:, 1]
        points_dataframe["z"] = points[:, 2]

        points_dataframe["r"] = colors[:, 0]
        points_dataframe["g"] = colors[:, 1]
        points_dataframe["b"] = colors[:, 2]

        return points_dataframe

    @staticmethod
    def ndarray(point_cloud: o3d.geometry.PointCloud) -> np.ndarray:
        points: np.ndarray = np.asarray(point_cloud.points)
        colors: np.ndarray = np.asarray(point_cloud.colors)

        x: np.ndarray = points[:, 0]
        y: np.ndarray = points[:, 1]
        z: np.ndarray = points[:, 2]

        r: np.ndarray = colors[:, 0]
        g: np.ndarray = colors[:, 1]
        b: np.ndarray = colors[:, 2]

        points_array: np.ndarray = np.array([x, y, z, r, g, b]).T
        return points_array
