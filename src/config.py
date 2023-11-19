import logging
import os
from enum import Enum


class Config(Enum):
    # Paths
    ROOT_DIR: str = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))

    DATA_DIR: str = os.path.join(ROOT_DIR, 'data')
    MODELS_DIR: str = os.path.join(ROOT_DIR, 'models')
    LOG_DIR: str = os.path.join(ROOT_DIR, 'logs')
    FIGURE_DIR: str = os.path.join(ROOT_DIR, 'figures')

    INPUT_DIR: str = os.path.join(DATA_DIR, 'input')
    OUTPUT_DIR: str = os.path.join(DATA_DIR, 'output')

    RAW_DATA_DIR: str = os.path.join(INPUT_DIR, 'raw_data')
    CROPPED_DATA_DIR: str = os.path.join(INPUT_DIR, 'cropped_data')
    DATASETS_DIR: str = os.path.join(INPUT_DIR, 'datasets')

    PREDICTION_DIR: str = os.path.join(OUTPUT_DIR, 'predictions')
    VOXEL_GRID_DIR: str = os.path.join(OUTPUT_DIR, 'voxel_grids')

    # Settings
    LOGGING_LEVEL: Enum = logging.INFO
