import pandas as pd


class PreprocessedDto:
    def __init__(
            self,
            grid_index: pd.DataFrame,
            voxel_color: pd.DataFrame,
            bounding_box: pd.DataFrame,
            features: pd.DataFrame,
            labels: pd.DataFrame,
            dataset: pd.DataFrame
    ) -> None:
        self.grid_index = grid_index
        self.voxel_color = voxel_color
        self.bounding_box = bounding_box
        self.features = features
        self.labels = labels
        self.dataset = dataset
