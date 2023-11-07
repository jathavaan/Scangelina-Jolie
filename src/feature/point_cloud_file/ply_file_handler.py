import os

import open3d as o3d
from pyntcloud import PyntCloud

from . import Filename, FileType
from .ifile_handler import IFileHandler
from ... import Config
from ...common.logger import ILogger


class PlyFileHandler(IFileHandler):
    __file: object

    def __init__(self, logger: ILogger) -> None:
        super().__init__(logger)

    def open(self, filename: Filename, file_type: FileType) -> None:
        if file_type not in [FileType.PLY]:
            raise ValueError("Invalid filetype. File has to be a PLY file.")

        filepath: str = os.path.join(Config.RAW_DATA_DIR.value, filename.value + file_type.value)
        # pcd = o3d.io.read_point_cloud(filename=filepath, print_progress=True)
        cloud: object = PyntCloud.from_file(filename=filepath)
        self.file = cloud

    def save(self, *point_clouds: o3d.geometry.PointCloud, file_prefix: str = None) -> None:
        raise NotImplementedError()

    def render_point_cloud_object(self) -> o3d.geometry.PointCloud:
        pass

    def list_dimensions(self) -> None:
        self.file.points
