import open3d as o3d

from . import Filename, FileType
from .ifile_handler import IFileHandler
from ...common.logger import ILogger


class PlyFileHandler(IFileHandler):
    def __init__(self, logger: ILogger) -> None:
        super().__init__(logger)

    def open(self, filename: Filename, file_type: FileType) -> None:
        if file_type not in [FileType.PLY]:
            raise ValueError("Invalid filetype. File has to be a PLY file.")

    def save(self, *point_clouds: o3d.geometry.PointCloud, file_prefix: str = None) -> None:
        pass

    def render_point_cloud_object(self) -> o3d.geometry.PointCloud:
        pass

    def list_dimensions(self) -> None:
        pass
