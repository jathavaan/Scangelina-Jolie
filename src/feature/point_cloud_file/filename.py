from enum import Enum


class Filename(Enum):
    # Raw data
    RAW_DATA: str = 'raw_data'
    CROPPED_RAW_DATA: str = 'cropped_raw_data'

    # Sliced data
    SLICE_1: str = 'cropped_raw_data_s1'
    SLICE_2: str = 'cropped_raw_data_s2'
    SLICE_3: str = 'cropped_raw_data_s3'
    SLICE_4: str = 'cropped_raw_data_s4'

    # Labeled data
    BUILDINGS: str = 'buildings'
    STREETS: str = 'streets'
    TREES: str = 'trees'
    TERRAIN: str = 'terrain'
    RIVERS: str = 'river'
