from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

bar_color = (0.6, 0.6, 0.9) # rgb 0-1
mean_color = (0.4, 0.9, 0.4)
grid_color = (0.6, 0.6, 0.6)
edge_color = (0.4, 0.4, 0.4)
figure_size = (8.5, 5) # w_inch x h_inch

def minimum_difference(values):
    """Returns the minimum difference between any 2 elements in a sorted list"""
    min_diff = float("inf")
    prev_value = values[0]
    for value in values[1:]:
        diff = value - prev_value
        if diff < min_diff:
            min_diff = diff
        prev_value = value
    return min_diff

def barplot_numerical(data, xticks=None, title=None, xlabel=None, ylabel=None, fig_filename="test_barplot.png", xlim=None,
                      ylim=None, figure_size=figure_size, dpi=120, show_mean=True):
    values, freq = np.unique(data, return_counts=True)
    min_diff = minimum_difference(values)
    fig, ax = plt.subplots()
    fig.set_size_inches(figure_size)
    if np.any(xticks):
        ax.set_xticks(xticks)
    if np.any(xlim):
        ax.set_xlim(xlim)
    else:
        ax.set_xlim(values[0] - min_diff, values[-1] + min_diff)
    if np.any(ylim):
        ax.set_ylim(ylim)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.yaxis.grid(True, color=grid_color, lw=0.2)
    ax.set_axisbelow(True)
    ax.bar(values, freq, width=min_diff*0.75, color=bar_color, edgecolor=edge_color)
    if show_mean:
        mean_line = ax.axvline(data.mean(), color=mean_color, ls="--", lw=2)
        ax.legend([mean_line], ['Mean'], prop={"size": 12})
    fig.savefig(fig_filename, dpi=dpi)