from enum import Enum


class Filename(Enum):
    RAW_DATA: str = 'raw_data'
    CROPPED_RAW_DATA: str = 'cropped_raw_data'
    SCALAR_FIELD: str = 'scalar_field'
    BUILDINGS: str = 'buildings'
    STREETS: str = 'streets'
    TREES: str = 'trees'
    TERRAIN: str = 'terrain'
    RIVERS: str = 'river'
