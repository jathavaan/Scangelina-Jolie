import numpy as np


class CovarianceMatrixTo:
    @staticmethod
    def eigenvalues_and_eigenvectors(covariance_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        eigenvalues, eigenvector = np.linalg.eig(covariance_matrix)
        return eigenvalues, eigenvector
