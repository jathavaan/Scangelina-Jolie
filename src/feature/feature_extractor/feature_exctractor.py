import numpy as np
import open3d as o3d
from sklearn.decomposition import PCA

from .feature_dto import FeatureDto
from .pca_parameters import PCAParameters
from .point_dto import PointDto
from ...common.logger import ILogger


class FeatureExtractor:
    __pca: PCA
    __logger: ILogger
    __point_dto: PointDto
    __features: FeatureDto

    def __init__(self, point_cloud: o3d.geometry.PointCloud, logger: ILogger) -> None:
        self.logger = logger
        self.point_dto = PointDto(point_cloud)
        self.pca = PCA(
            n_components=PCAParameters.N_COMPONENTS.value,
        )

        self.logger.debug("Performing PCA on point cloud...")
        points: np.ndarray = self.point_dto.point_cloud_array[:, :3]
        self.pca.fit(points)

        z: np.ndarray = self.point_dto.point_cloud_array[:, 2]
        eigenvalues: np.ndarray = np.array(self.pca.explained_variance_)
        features: FeatureDto = FeatureDto(eigenvalues=eigenvalues, z=z, logger=self.logger)

        self.features = features
        self.logger.debug("PCA performed successfully.")

    @property
    def logger(self) -> ILogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: ILogger) -> None:
        self.__logger = logger

    @property
    def pca(self) -> PCA:
        return self.__pca

    @pca.setter
    def pca(self, pca: PCA) -> None:
        self.__pca = pca

    @property
    def features(self) -> FeatureDto:
        return self.__features

    @features.setter
    def features(self, features: FeatureDto) -> None:
        self.__features = features

    @property
    def point_dto(self) -> PointDto:
        return self.__point_dto

    @point_dto.setter
    def point_dto(self, point_dto: PointDto) -> None:
        self.__point_dto = point_dto
