import numpy as np


class Feature:
    @staticmethod
    def linearity(l1: float, l2: float, l3: float) -> float:
        return (l1 - l2) / l1

    @staticmethod
    def planarity(l1: float, l2: float, l3: float) -> float:
        return (l2 - l3) / l1

    @staticmethod
    def scattering(l1: float, l2: float, l3: float) -> float:
        return l3 / l1

    @staticmethod
    def omnivariance(l1: float, l2: float, l3: float) -> float:
        return (l1 * l2 * l3) ** (1 / 3)

    @staticmethod
    def anisotropy(l1: float, l2: float, l3: float) -> float:
        return (l1 - l3) / l1

    @staticmethod
    def eigenentropy(l1: float, l2: float, l3: float) -> float:
        return -1 * (l1 * np.log(l1) + l2 * np.log(l2) + l3 * np.log(l3))

    @staticmethod
    def change_of_curvature(l1: float, l2: float, l3: float) -> float:
        return l3 / (l1 + l2 + l3)

    @staticmethod
    def sum_of_eigenvalues(l1: float, l2: float, l3: float) -> float:
        return l1 + l2 + l3

    @staticmethod
    def z_range(z: np.ndarray) -> float:
        return np.max(z) - np.min(z)
