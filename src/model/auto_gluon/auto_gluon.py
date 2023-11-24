import os
from datetime import timedelta, datetime

import pandas as pd
from autogluon.tabular import TabularPredictor

from .auto_gluon_parameters import AutoGluonParameter
from ... import Config
from ...common.logger import ILogger
from ...feature.preprocess import PreprocessedDto


class AutoGluon:
    __model: TabularPredictor
    __train_dto: PreprocessedDto
    __test_dto: PreprocessedDto
    __logger: ILogger
    __train_max_minutes: int
    __train_time_limit: int
    __model_path: str
    __predictions: pd.DataFrame

    def __init__(
            self,
            train_dto: PreprocessedDto,
            test_dto: PreprocessedDto,
            logger: ILogger,
            train_max_minutes: int = 10,
            model_directory: str = 'ag_model'
    ) -> None:
        self.train_dto = train_dto
        self.test_dto = test_dto
        self.logger = logger
        self.train_max_minutes = train_max_minutes
        self.train_time_limit = train_max_minutes * 60
        self.model_path = os.path.join(Config.MODELS_DIR.value, 'auto_gluon', f'{model_directory}_{train_max_minutes}')

    @property
    def model(self) -> TabularPredictor:
        return self.__model

    @model.setter
    def model(self, model: TabularPredictor) -> None:
        self.__model = model

    @property
    def train_dto(self) -> PreprocessedDto:
        return self.__train_dto

    @train_dto.setter
    def train_dto(self, train_dto: PreprocessedDto) -> None:
        self.__train_dto = train_dto

    @property
    def test_dto(self) -> PreprocessedDto:
        return self.__test_dto

    @test_dto.setter
    def test_dto(self, test_dto: PreprocessedDto) -> None:
        self.__test_dto = test_dto

    @property
    def logger(self) -> ILogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: ILogger) -> None:
        self.__logger = logger

    @property
    def train_max_minutes(self) -> int:
        return self.__train_max_minutes

    @train_max_minutes.setter
    def train_max_minutes(self, train_max_minutes: int) -> None:
        self.__train_max_minutes = train_max_minutes

    @property
    def train_time_limit(self) -> int:
        return self.__train_time_limit

    @train_time_limit.setter
    def train_time_limit(self, train_time_limit: int) -> None:
        self.__train_time_limit = train_time_limit

    @property
    def model_path(self) -> str:
        return self.__model_path

    @model_path.setter
    def model_path(self, model_path: str) -> None:
        self.__model_path = model_path

    @property
    def predictions(self) -> pd.DataFrame:
        return self.__predictions

    @predictions.setter
    def predictions(self, predictions: pd.DataFrame) -> None:
        self.__predictions = predictions

    def fit(self, label: str = 'label', overwrite_model: bool = False) -> None:
        start_time: datetime = datetime.now()
        end_time: datetime = start_time + timedelta(seconds=self.train_time_limit)
        start_string: str = start_time.strftime("%H:%M:%S")
        end_string: str = end_time.strftime("%H:%M:%S")

        if not overwrite_model and os.path.exists(self.model_path):
            self.logger.info(f"A model has already been trained and saved at {self.model_path}")
            self.logger.info("Loading model.")
            self.model = TabularPredictor.load(self.model_path, verbosity=AutoGluonParameter.VERBOSITY.value)
            self.logger.info("Model loaded.")
        else:
            self.logger.info(
                f"Training AutoGluon model for {self.train_time_limit} seconds. "
                f"Start time: {start_string}. Estimated end time: {end_string}"
            )

            self.model = TabularPredictor(
                label=label,
                problem_type=AutoGluonParameter.PROBLEM_TYPE.value,
                eval_metric=AutoGluonParameter.EVAL_METRIC.value,
                verbosity=AutoGluonParameter.VERBOSITY.value,
                path=self.model_path
            ).fit(
                train_data=self.train_dto.dataset,
                presets=AutoGluonParameter.PRESETS.value,
                time_limit=self.train_time_limit,
                verbosity=AutoGluonParameter.VERBOSITY.value
            )

            self.logger.info(f"Saving model to {self.model_path}")

    def predict(self) -> None:
        filepath: str = os.path.join(Config.PREDICTION_DIR.value, f'prediction_{self.train_max_minutes}.csv')

        if os.path.exists(filepath):
            self.logger.info(f"Loading predictions from {filepath}")
            predictions = pd.read_csv(filepath)
        else:
            start_time: str = datetime.now().strftime("%H:%M:%S")
            self.logger.info(f"Predicting with AutoGluon model at {start_time}")
            predictions = self.model.predict(self.test_dto.dataset)
            self.logger.info(f"Saving predictions to {filepath}")
            predictions.to_csv(filepath)

        self.predictions = predictions

    def predict_proba(self) -> pd.DataFrame:
        return self.model.predict_proba(self.test_dto.features)

    def get_leaderboard(self) -> pd.DataFrame:
        return self.model.leaderboard(silent=True)

    def feature_importance(self) -> pd.DataFrame:
        return self.model.feature_importance(self.train_dto.dataset)
