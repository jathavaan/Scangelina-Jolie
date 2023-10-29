import numpy as np


class Color16BitTo:
    @staticmethod
    def color_8_bit(channel: np.ndarray) -> np.ndarray:
        conversion_factor: int = 65535
        return np.divide(channel, conversion_factor)
