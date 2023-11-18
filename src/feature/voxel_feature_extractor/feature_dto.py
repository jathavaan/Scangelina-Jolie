import numpy as np

from ...common.logger import ILogger
from ...common.utils.calculation.feature import Feature


class FeatureDto:
    __logger: ILogger

    __eigenvalues: np.ndarray
    __l1: float
    __l2: float
    __l3: float

    __planarity: float
    __linearity: float
    __scattering: float
    __omnivariance: float
    __sum_of_eigenvalues: float
    __eigenentropy: float
    __anisotropy: float
    __change_of_curvature: float
    __z_range: float

    __array: np.ndarray

    def __init__(self, eigenvalues: np.ndarray, z: np.ndarray, logger: ILogger) -> None:
        self.logger = logger

        self.eigenvalues = eigenvalues
        self.l1 = eigenvalues[0]
        self.l2 = eigenvalues[1]
        self.l3 = eigenvalues[2]

        self.planarity = Feature.planarity(self.l1, self.l2, self.l3)
        self.linearity = Feature.linearity(self.l1, self.l2, self.l3)
        self.scattering = Feature.scattering(self.l1, self.l2, self.l3)
        self.omnivariance = Feature.omnivariance(self.l1, self.l2, self.l3)
        self.sum_of_eigenvalues = Feature.sum_of_eigenvalues(self.l1, self.l2, self.l3)
        self.eigenentropy = Feature.eigenentropy(self.l1, self.l2, self.l3)
        self.anisotropy = Feature.anisotropy(self.l1, self.l2, self.l3)
        self.change_of_curvature = Feature.change_of_curvature(self.l1, self.l2, self.l3)
        self.z_range = Feature.z_range(z)

        self.array = np.array([
            self.l1,
            self.l2,
            self.l3,
            self.linearity,
            self.planarity,
            self.scattering,
            self.omnivariance,
            self.sum_of_eigenvalues,
            self.eigenentropy,
            self.anisotropy,
            self.change_of_curvature,
            self.z_range
        ])

    @property
    def logger(self) -> ILogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: ILogger) -> None:
        self.__logger = logger

    @property
    def eigenvalues(self) -> np.ndarray:
        return self.__eigenvalues

    @eigenvalues.setter
    def eigenvalues(self, eigenvector: np.ndarray) -> None:
        self.__eigenvalues = eigenvector

    @property
    def l1(self) -> float:
        return self.__l1

    @l1.setter
    def l1(self, l1: float) -> None:
        self.__l1 = l1

    @property
    def l2(self) -> float:
        return self.__l2

    @l2.setter
    def l2(self, l2: float) -> None:
        self.__l2 = l2

    @property
    def l3(self) -> float:
        return self.__l3

    @l3.setter
    def l3(self, l3: float) -> None:
        self.__l3 = l3

    @property
    def linearity(self) -> float:
        return self.__linearity

    @linearity.setter
    def linearity(self, linearity: float) -> None:
        self.__linearity = linearity

    @property
    def planarity(self) -> float:
        return self.__planarity

    @planarity.setter
    def planarity(self, planarity: float) -> None:
        self.__planarity = planarity

    @property
    def scattering(self) -> float:
        return self.__scattering

    @scattering.setter
    def scattering(self, scattering: float) -> None:
        self.__scattering = scattering

    @property
    def omnivariance(self) -> float:
        return self.__omnivariance

    @omnivariance.setter
    def omnivariance(self, omnivariance: float) -> None:
        self.__omnivariance = omnivariance

    @property
    def sum_of_eigenvalues(self) -> float:
        return self.__sum_of_eigenvalues

    @sum_of_eigenvalues.setter
    def sum_of_eigenvalues(self, sum_of_eigenvalues: float) -> None:
        self.__sum_of_eigenvalues = sum_of_eigenvalues

    @property
    def eigenentropy(self) -> float:
        return self.__eigenentropy

    @eigenentropy.setter
    def eigenentropy(self, eigenentropy: float) -> None:
        self.__eigenentropy = eigenentropy

    @property
    def anisotropy(self) -> float:
        return self.__anisotropy

    @anisotropy.setter
    def anisotropy(self, anisotropy: float) -> None:
        self.__anisotropy = anisotropy

    @property
    def change_of_curvature(self) -> float:
        return self.__change_of_curvature

    @change_of_curvature.setter
    def change_of_curvature(self, change_of_curvature: float) -> None:
        self.__change_of_curvature = change_of_curvature

    @property
    def z_range(self) -> float:
        return self.__z_range

    @z_range.setter
    def z_range(self, z_range: float) -> None:
        self.__z_range = z_range

    @property
    def array(self) -> np.ndarray:
        return self.__array

    @array.setter
    def array(self, array: np.ndarray) -> None:
        self.__array = array

    def __repr__(self) -> str:
        return f"FeatureDto(\n\teigenvalues=[{self.l1} {self.l2} {self.l3}], \n\tlinearity={self.linearity}, " \
               f"\n\tplanarity={self.planarity}, \n\tscattering={self.scattering}, " \
               f"\n\tomnivariance={self.omnivariance}, \n\tsum_of_eigenvalues={self.sum_of_eigenvalues}, " \
               f"\n\teigenentropy={self.eigenentropy}, \n\tanisotropy={self.anisotropy}, " \
               f"\n\tchange_of_curvature={self.change_of_curvature}"\
               f"\n\tz_range={self.z_range}\n)"
