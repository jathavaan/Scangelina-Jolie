from abc import ABC, abstractmethod
from typing import Any

import open3d as o3d

from .file_type import FileType
from .filename import Filename
from ...common.logger import ILogger


class IFileHandler(ABC):
    __file: Any
    __logger: ILogger

    def __init__(self, logger: ILogger) -> None:
        self.logger = logger

    @property
    def file(self) -> Any:
        return self.__file

    @file.setter
    def file(self, file: Any) -> None:
        self.__file = file

    @property
    def logger(self) -> ILogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: ILogger) -> None:
        self.__logger = logger

    @abstractmethod
    def open(self, filename: Filename, file_type: FileType) -> None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, *point_clouds: o3d.geometry.PointCloud, file_prefix: str = None) -> None:
        raise NotImplementedError()

    @abstractmethod
    def render_point_cloud_object(self) -> o3d.geometry.PointCloud:
        raise NotImplementedError()

    @abstractmethod
    def list_dimensions(self) -> None:
        raise NotImplementedError()
