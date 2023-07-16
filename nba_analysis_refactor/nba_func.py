
from __future__ import annotations
from typing import Optional, Union, List, Protocol

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.metrics as skm


def sort_top_players_by_stat(
        data: pd.DataFrame, stat: Union[List[str], str], n: Optional[int] = 5,
        ascending: Union[List[bool], bool] = False
) -> pd.DataFrame:
    """
    Find the top players as determined by the stats

    :param data: pd.DataFrame; player stats for the season

    :param stat: str or list of str; the stats to sort the player on

    :param n: optional; int; default is 5.  Get the top n players for the stats

    :param ascending: bool or list of bool; default is False.  The ascending parameter for pd.DataFrame.sort_values

    :return: pd.DataFrame; the top players by stat
    """
    if (n is not None) and n < 1:
        raise ValueError(f'Expected n to be None or an int > 0; received {n=}')

    data = data.sort_values(by=stat, ascending=ascending)
    return data if n is None else data.head(n)


def display_confusion_matrix(fitted_model, x: pd.DataFrame, y: pd.Series) -> None:
    """
    Display the confusion matrix and accuracy of the model.

    :param fitted_model: a fitted model

    :param x: pd.DataFrame; the features

    :param y: pd.Series; the target variable

    :return: None
    """
    model_name = fitted_model.__class__.__name__

    predictions = fitted_model.predict(x)
    confusion_matrix = skm.confusion_matrix(y, predictions, labels=fitted_model.classes_)
    display = skm.ConfusionMatrixDisplay(confusion_matrix, fitted_model.classes_)
    display.plot()
    plt.title(f'{model_name} Confusion Matrix')

    acc = skm.accuracy_score(y, predictions)
    print(f'{model_name} Accuracy: {acc}')


def display_confusion_matrix_with_protocol(fitted_model: FittedModel, x: pd.DataFrame, y: pd.Series) -> None:
    """
    Display the confusion matrix and accuracy of the model.

    :param fitted_model: a fitted model

    :param x: pd.DataFrame; the features

    :param y: pd.Series; the target variable

    :return: None
    """
    model_name = fitted_model.__class__.__name__

    predictions = fitted_model.predict(x)
    confusion_matrix = skm.confusion_matrix(y, predictions, labels=fitted_model.classes_)
    display = skm.ConfusionMatrixDisplay(confusion_matrix, fitted_model.classes_)
    display.plot()
    plt.title(f'{model_name} Confusion Matrix')

    acc = skm.accuracy_score(y, predictions)
    print(f'{model_name} Accuracy: {acc}')


class FittedModel(Protocol):
    def predict(self, x: pd.DataFrame) -> np.array: ...

    @property
    def classes_(self): ...
