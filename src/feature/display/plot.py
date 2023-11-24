import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from ..preprocess.preprocessed_dto import PreprocessedDto
from ... import Config


class Plot:
    data: pd.DataFrame
    base_filepath: str
    figheight: int
    figwidth: int

    def __init__(self, dto: PreprocessedDto, filename: str) -> None:
        features: pd.DataFrame = dto.features
        labels: pd.DataFrame = dto.labels
        data: pd.DataFrame = pd.merge(features, labels, left_index=True, right_index=True)

        self.data = data
        self.base_filepath = os.path.join(Config.FIGURE_DIR.value, filename)
        self.figheight = 4
        self.figwidth = 20

    def violin(self) -> None:
        feature_columns = self.data.columns[:-1]
        n_features = len(feature_columns)
        rows = int(np.ceil(n_features / 2))
        fig, axes = plt.subplots(rows, 2, figsize=(self.figwidth, self.figheight * rows))
        axes = axes.flatten()

        for i, feature in enumerate(feature_columns):
            sns.violinplot(ax=axes[i], x=self.data['label'], y=self.data[feature], palette='coolwarm')
            axes[i].set_title(f'Violin Plot for {feature}')
            axes[i].set_xlabel('Label')
            axes[i].set_ylabel(feature)

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.savefig(f'{self.base_filepath}_violin.png')
        plt.show()

    def heatmap(self) -> None:
        correlation_matrix = self.data.iloc[:, :-1].corr()
        plt.figure(figsize=(self.figwidth, self.figwidth))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.savefig(f'{self.base_filepath}_heatmap.png')
        plt.show()

    def box_plot(self) -> None:
        feature_columns = self.data.columns[:-1]
        n_features = len(feature_columns)
        rows = int(np.ceil(n_features / 2))
        fig, axes = plt.subplots(rows, 2, figsize=(self.figwidth, self.figheight * rows))
        axes = axes.flatten()

        for i, feature in enumerate(feature_columns):
            sns.boxplot(ax=axes[i], x=self.data['label'], y=self.data[feature], palette='coolwarm')
            axes[i].set_title(f'Box Plot for {feature}')
            axes[i].set_xlabel('Label')
            axes[i].set_ylabel(feature)

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.savefig(f'{self.base_filepath}_boxplot.png')
        plt.show()

    def bar_plot(self) -> None:
        feature_columns = self.data.columns[:-1]  # Exclude the last column (label)
        n_features = len(feature_columns)
        rows = int(np.ceil(n_features / 2))
        fig, axes = plt.subplots(rows, 2, figsize=(self.figwidth, self.figheight * rows))
        axes = axes.flatten()

        for i, feature in enumerate(feature_columns):
            sns.barplot(ax=axes[i], x='label', y=feature, data=self.data, palette='coolwarm')
            axes[i].set_title(f'Bar Plot for {feature}')
            axes[i].set_xlabel('Label')
            axes[i].set_ylabel(feature)

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.savefig(f'{self.base_filepath}_barplot.png')
        plt.show()

    def histogram(self) -> None:
        feature_columns = self.data.columns[:-1]
        n_features = len(feature_columns)
        rows = int(np.ceil(n_features / 2))
        fig, axes = plt.subplots(rows, 2, figsize=(self.figwidth, self.figheight * rows))
        axes = axes.flatten()

        for i, feature in enumerate(feature_columns):
            axes[i].hist(self.data[feature], bins=20, color='skyblue', edgecolor='black')
            axes[i].set_title(f'Histogram for {feature}')
            axes[i].set_xlabel(feature)
            axes[i].set_ylabel('Frequency')

        for j in range(i + 1, len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.savefig(f'{self.base_filepath}_histogram.png')
        plt.show()
