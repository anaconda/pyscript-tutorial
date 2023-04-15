import numpy as np
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
from numpy.typing import ArrayLike


def plot_class_distribution(y: ArrayLike, class_names: ArrayLike):
    class_count = np.bincount(y)

    shades_of_red = plt.cm.PuRd(np.linspace(0.5, 0.7, len(class_count)))
    fig, ax = plt.subplots(figsize=(5, 5))

    bars = plt.bar(class_names, class_count, color=shades_of_red)
    plt.ylim([0, max(class_count) + 5])

    # Loop through the bars and add annotations
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 1), textcoords="offset points", ha='center', va='bottom')
    return fig

def plot_feature_matrix(X: ArrayLike, y: ArrayLike):
    n_features = X.shape[1]
    fig, ax = plt.subplots(n_features, n_features, figsize=(12, 12))
    _ = scatter_matrix(X, ax=ax, c=y, cmap=plt.cm.PiYG)
    return fig
