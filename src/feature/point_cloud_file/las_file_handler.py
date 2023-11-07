import os
import time

import laspy
import open3d as o3d
from laspy import DimensionInfo
from laspy.lasdata import LasData

from .directory_type import DirectoryType
from .file_type import FileType
from .filename import Filename
from .ifile_handler import IFileHandler
from ... import Config
from ...common.logger import ILogger
from ...common.utils.conversion import LasTo


class LasFileHandler(IFileHandler):
    __file: LasData

    def __init__(self, logger: ILogger) -> None:
        super().__init__(logger)
        self.file = None

    def open(self, directory_type: DirectoryType, filename: Filename, file_type: FileType) -> None:
        if file_type not in [FileType.LAS, FileType.LAZ]:
            raise ValueError("Invalid filetype. File has to be a LAS or LAZ file.")

        if directory_type == DirectoryType.RAW:
            filepath: str = os.path.join(Config.RAW_DATA_DIR.value, filename.value + file_type.value)
        else:
            filepath: str = os.path.join(Config.CROPPED_DATA_DIR.value, filename.value + file_type.value)

        with laspy.open(filepath) as laspy_file:
            las_data: LasData = laspy_file.read()

        self.file = las_data

        point_count: int = len(las_data.points)
        self.logger.info(f"Loaded {point_count} points from {filename.value}{file_type.value}")

    def save(self, *point_clouds: o3d.geometry.PointCloud, file_prefix: str = None) -> None:
        point_cloud: o3d.geometry.PointCloud = o3d.geometry.PointCloud()
        for pcd in point_clouds:
            point_cloud += pcd

        filename: str = time.strftime("%Y%m%d-%H%M%S") + ".ply"
        if file_prefix:
            filename: str = file_prefix + "-" + filename

        path: str = os.path.join(Config.OUTPUT_DIR.value, filename)
        o3d.io.write_point_cloud(filename=path, pointcloud=point_cloud)

    def render_point_cloud_object(self) -> o3d.geometry.PointCloud:
        self.logger.info("Rendering point cloud object")
        point_cloud: o3d.geometry.PointCloud = LasTo.point_cloud(self.file)
        self.logger.info("Rendered point cloud object")

        return point_cloud

    def list_dimensions(self) -> None:
        las_data: LasData = self.file
        dimensions: list[DimensionInfo] = las_data.header.point_format.dimensions
        for dimension in dimensions:
            print(dimension.name)
