from enum import Enum


class FileType(Enum):
    PCD: str = ".pcd"
    PLY: str = ".ply"
    LAS: str = ".las"
    LAZ: str = ".laz"
