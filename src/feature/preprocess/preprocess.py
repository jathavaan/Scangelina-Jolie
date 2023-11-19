from typing import Union

import pandas as pd

from .data_dto import DataDto
from .preprocessed_dto import PreprocessedDto
from ...common.logger import ILogger


class Preprocess:
    __dto: DataDto
    __train_dto: PreprocessedDto
    __test_dto: PreprocessedDto
    __logger: ILogger

    def __init__(self, dto: DataDto, logger: ILogger) -> None:
        self.dto = dto
        self.logger = logger
        self.preprocess()

    @property
    def dto(self) -> DataDto:
        return self.__dto

    @dto.setter
    def dto(self, dto: DataDto) -> None:
        self.__dto = dto

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

    def preprocess(self) -> None:
        self.logger.debug('Preprocessing data...')
        train_data: pd.DataFrame = self.dto.train.copy()
        test_data: pd.DataFrame = self.dto.test.copy()

        self.train_data(train_data)
        self.test_data(test_data)
        self.logger.debug("Preprocessing done.")

    def common(self, data: pd.DataFrame) -> PreprocessedDto:
        data = self.transform_datatypes(data)
        data = self.normalize(data)
        data = self.log_transform(data)

        dto = Preprocess.create_dto(data)
        return dto

    def train_data(self, data: pd.DataFrame) -> None:
        dto = self.common(data)
        self.train_dto = dto

    def test_data(self, data: pd.DataFrame) -> None:
        dto = self.common(data)
        self.test_dto = dto

    def transform_datatypes(self, data: pd.DataFrame) -> pd.DataFrame:
        self.logger.debug('Transforming datatypes...')
        data['grid_x'] = data['grid_x'].astype('int32')
        data['grid_y'] = data['grid_y'].astype('int32')
        data['grid_z'] = data['grid_z'].astype('int32')
        return data

    def normalize(self, data: pd.DataFrame) -> pd.DataFrame:
        self.logger.debug('Normalizing data...')
        return data

    def log_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        self.logger.debug('Log transforming data...')
        return data

    @staticmethod
    def create_dto(data: pd.DataFrame) -> PreprocessedDto:
        def get_grid_index(raw_data: pd.DataFrame) -> pd.DataFrame:
            return raw_data[['grid_x', 'grid_y', 'grid_z']]

        def get_voxel_color(raw_data: pd.DataFrame) -> pd.DataFrame:
            return raw_data[['r', 'g', 'b']]

        def get_bounding_box(raw_data: pd.DataFrame) -> pd.DataFrame:
            return raw_data[[
                'max_bound_x',
                'max_bound_y',
                'max_bound_z',
                'min_bound_x',
                'min_bound_y',
                'min_bound_z'
            ]]

        def get_features(raw_data: pd.DataFrame) -> pd.DataFrame:
            return raw_data[[
                'l1',
                'l2',
                'l3',
                'planarity',
                'linearity',
                'scattering',
                'omnivariance',
                'sum_of_eigenvalues',
                'eigenentropy',
                'anisotropy',
                'change_of_curvature',
                'z_range'
            ]]

        def get_labels(raw_data: pd.DataFrame) -> Union[pd.DataFrame, None]:
            return raw_data[['label']] if 'label' in raw_data.columns else None

        def get_dataset(features: pd.DataFrame, labels: Union[pd.DataFrame, None]) -> pd.DataFrame:
            if labels is not None:
                return pd.merge(features, labels, left_index=True, right_index=True)

            return features

        dto: PreprocessedDto = PreprocessedDto(
            grid_index=get_grid_index(data),
            voxel_color=get_voxel_color(data),
            bounding_box=get_bounding_box(data),
            features=get_features(data),
            labels=get_labels(data),
            dataset=get_dataset(get_features(data), get_labels(data))
        )

        return dto
