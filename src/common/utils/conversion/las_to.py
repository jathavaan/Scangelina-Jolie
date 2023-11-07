import numpy as np
import open3d as o3d
import pandas as pd
from laspy import LasData

from .color_16_bit_to import Color16BitTo


class LasTo:
    @staticmethod
    def dataframe(las: LasData) -> pd.DataFrame:
        x_coordinates: np.ndarray = np.array(las.x)
        y_coordinates: np.ndarray = np.array(las.y)
        z_coordinates: np.ndarray = np.array(las.z)

        red_channel: np.ndarray = las.red
        green_channel: np.ndarray = las.green
        blue_channel: np.ndarray = las.blue

        points: pd.DataFrame = pd.DataFrame(
            columns=['X', 'Y', 'Z', 'red', 'green', 'blue'],
        )

        points["X"] = x_coordinates
        points["Y"] = y_coordinates
        points["Z"] = z_coordinates

        points["red"] = Color16BitTo.color_8_bit(red_channel)
        points["green"] = Color16BitTo.color_8_bit(green_channel)
        points["blue"] = Color16BitTo.color_8_bit(blue_channel)

        return points

    @staticmethod
    def point_cloud(las: LasData) -> o3d.geometry.PointCloud:
        points: pd.DataFrame = LasTo.dataframe(las)

        x: np.ndarray = points["X"].values
        y: np.ndarray = points["Y"].values
        z: np.ndarray = points["Z"].values

        point_cloud: o3d.geometry.PointCloud = o3d.geometry.PointCloud()
        point_cloud.points = o3d.utility.Vector3dVector(points[["X", "Y", "Z"]].values)
        point_cloud.colors = o3d.utility.Vector3dVector(points[["red", "green", "blue"]].values)

        return point_cloud
