import pandas as pd
from autogluon.tabular import TabularPredictor, TabularDataset

from .auto_gluon_parameters import AutoGluonParameter


class AutoGluon:
    __model: TabularPredictor
    __train_data: TabularDataset
    __test_data: TabularDataset

    def __init__(self, train_data: pd.DataFrame, test_data: pd.DataFrame) -> None:
        self.__train_data = TabularDataset(train_data)
        self.__test_data = TabularDataset(test_data)

    @property
    def model(self) -> TabularPredictor:
        return self.__model

    @property
    def train_data(self) -> TabularDataset:
        return self.__train_data

    @property
    def test_data(self) -> TabularDataset:
        return self.__test_data

    def fit(self, label: str = 'label') -> None:
        self.model = TabularPredictor(
            label=label,
            eval_metric=AutoGluonParameter.EVAL_METRIC.value,
        ).fit(
            train_data=self.train_data,
            presets=AutoGluonParameter.PRESETS.value
        )

    def predict(self) -> pd.DataFrame:
        return self.model.predict(self.test_data)

    def predict_proba(self) -> pd.DataFrame:
        return self.model.predict_proba(self.test_data)
