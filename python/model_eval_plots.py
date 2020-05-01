"""Functions to plot model performance."""
from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve


def plot_pr(
    y: pd.Series, predict_proba: np.ndarray, title: Optional[str] = None
) -> mpl.axes._axes:
    """
    Plot the precision-recall curve.

    Parameters
    ----------
    y : pd.Series
        The target values the model was trained on.
    predict_proba : Two column np.ndarray
        Probabilities outputted by a model.
    title : str, optional (default=None)
        The title of the plot. By default will have no title.

    Returns
    -------
    axes : Matlotlib axes
        The precision-recall curve.
    """
    precision, recall, thresholds = precision_recall_curve(
        y, probas_pred=predict_proba[:, 1]
    )
    baseline = (y == 1).mean()
    plt.axhline(baseline, c="#d93025", label="Baseline")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.plot(recall, precision, label="PR curve")
    plt.axhline(0, c="#9E9E9E", zorder=1)
    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
    plt.xlim(0, 1)
    if title is not None:
        plt.title(title, loc="left")
    return plt.show()


def plot_confusion(
    y: pd.Series,
    predict_proba: np.ndarray,
    threshold: float = 0.5,
    title: Optional[str] = None,
) -> mpl.axes._axes:
    """
    Plot the confusion matrix.

    Parameters
    ----------
    y : pd.Series
        The target values the model was trained on.
    predict_proba : Two column np.ndarray
        Probabilities outputted by a model.
    threshold : float, optional (default=0.5)
        Determine the probability threshold. If the predicted
        probability is above the threshold, model will predict 1. By
        default 0.5.
    title : str, optional (default=None)
        The title of the plot. By default will have no title.

    Returns
    -------
    axes : Matlotlib axes
        Confusion matrix.
    """
    ax = sns.heatmap(
        confusion_matrix(y, (predict_proba[:, 1] > threshold)),
        annot=True,
        fmt=",",
        cmap=[
            "#efe5fd",
            "#d4bff9",
            "#b794f6",
            "#9965f4",
            "#7e3ff2",
            "#6002ee",
            "#5300e8",
            "#3d00e0",
            "#1c00db",
            "#0000d6",
        ],
    )
    plt.ylabel("Actual values")
    plt.xlabel("Prediced values")
    plt.ylim(2.0, 0)
    if title is not None:
        plt.title(title, loc="left")
    return ax


def plot_roc(
    y: pd.Series,
    predict_proba: np.ndarray,
    title: Optional[str] = None,
) -> mpl.axes._axes:
    """
    Plot the ROC curve.

    Parameters
    ----------
    y : pd.Series
        The target values the model was trained on.
    predict_proba : Two column np.ndarray
        Probabilities outputted by a model.
    title : str, optional (default=None)
        The title of the plot. By default will have no title.
    title : str, optional (default=None)
        The title of the plot. By default will have no title.

    Returns
    -------
    axes : Matlotlib axes
        Plot of ROC curve.
    """
    fpr, tpr, thresholds = roc_curve(y, predict_proba[:, 1])
    plt.plot([0, 1], [0, 1], "--", label="Baseline")
    plt.xlabel("False positive")
    plt.ylabel("True positive")
    plt.plot(fpr, tpr, label="ROC")
    plt.axhline(0, c="#9E9E9E", zorder=1)
    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
    if title is not None:
        plt.title(title, loc="left")
    return plt.show()


def plot_probability_dist(
    y: pd.Series,
    predict_proba: np.ndarray,
    threshold: float = 0.5,
    title: Optional[str] = None,
) -> mpl.axes._axes:
    """
    Plot the distribution of predicted probabilities per class.

    Parameters
    ----------
    y : pd.Series
        The target values the model was trained on.
    predict_proba : Two column np.ndarray
        Probabilities outputted by a model.
    threshold : float, optional (default=0.5)
        Determine the probability threshold. If the predicted
        probability is above the threshold, model will predict 1. By
        default 0.5. Will plot a vertical line representing the chosen
        value.
    title : str, optional (default=None)
        The title of the plot. By default will have no title.

    Returns
    -------
    axes : Matlotlib axes
        Plot of probability distributions.
    """
    sns.kdeplot(predict_proba[y == 0][:, 1], label="Not Fraud", zorder=2)
    sns.kdeplot(predict_proba[y == 1][:, 1], label="Fraud", zorder=2)
    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
    plt.xlabel("Modeled probability")
    plt.ylabel("Density")
    plt.axhline(0, c="#9E9E9E", zorder=1)
    plt.axvline(threshold, color="#9E9E9E", linestyle="dashed", zorder=1)
    plt.xticks(
        [i / 10 for i in range(0, 11, 2)], [f"{i/10:.0%}" for i in range(0, 11, 2)]
    )
    if title is not None:
        plt.title(title, loc="left")
    return plt.show()
