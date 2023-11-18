import pandas as pd
import numpy as np


class DataFrameTo:
    @staticmethod
    def ndarray(dataframe: pd.DataFrame) -> np.ndarray:
        return dataframe.to_numpy()