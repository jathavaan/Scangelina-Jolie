import logging
import os
from enum import Enum


class Config(Enum):
    # Paths
    ROOT_DIR: str = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))
    DATA_DIR: str = os.path.join(ROOT_DIR, 'data')
    INPUT_DIR: str = os.path.join(DATA_DIR, 'input')
    RAW_DATA_DIR: str = os.path.join(INPUT_DIR, 'raw_data')
    CROPPED_DATA_DIR: str = os.path.join(INPUT_DIR, 'cropped_data')
    OUTPUT_DIR: str = os.path.join(DATA_DIR, 'output')
    LOG_DIR: str = os.path.join(ROOT_DIR, 'logs')

    # Settings
    LOGGING_LEVEL: Enum = logging.INFO
