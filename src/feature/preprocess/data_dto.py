import pandas as pd


class DataDto:
    def __init__(self, train: pd.DataFrame, test: pd.DataFrame) -> None:
        self.train = train
        self.test = test

    def __repr__(self) -> str:
        return (
            f'Train: {self.train.shape} [No NaN: {self.train.isna().sum().sum()}] | '
            f'Test: {self.test.shape} [No NaN: {self.test.isna().sum().sum()}]'
        )
