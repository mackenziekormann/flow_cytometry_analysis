import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from parser import fcs_parser

def plot_histogram(data, column, bins=50, color='blue', title=None, save_path=None):
    """
    Plot a histogram for a specific column.

    Parameters:
        data (pd.DataFrame): The dataset.
        column (str): Column to visualize.
        bins (int): Number of bins for the histogram.
        color (str): Color of the histogram bars.
        title (str): Plot title.
        save_path (str): Path to save the plot, if provided.
    """
    plt.hist(data[column], bins=bins, color=color, edgecolor='black', alpha=0.7)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(title or f'{column} Distribution')
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_scatter(data, x_column, y_column, color='blue', alpha=0.5, title=None, save_path=None):
    """
    Plot a scatter plot between two columns.

    Parameters:
        data (pd.DataFrame): The dataset.
        x_column (str): X-axis column.
        y_column (str): Y-axis column.
        color (str): Dot color.
        alpha (float): Transparency of dots.
        title (str): Plot title.
        save_path (str): Path to save the plot, if provided.
    """
    plt.scatter(data[x_column], data[y_column], c=color, alpha=alpha, s=5)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title or f'{x_column} vs {y_column}')
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_density(data, x_column, y_column, cmap='Blues', title=None, save_path=None):
    """
    Plot a density map for two columns.

    Parameters:
        data (pd.DataFrame): The dataset.
        x_column (str): X-axis column.
        y_column (str): Y-axis column.
        cmap (str): Color map for density.
        title (str): Plot title.
        save_path (str): Path to save the plot, if provided.
    """
    sns.kdeplot(
        x=data[x_column], y=data[y_column],
        cmap=cmap, fill=True, thresh=0.05, levels=100
    )
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title or f'Density: {x_column} vs {y_column}')
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_correlation_heatmap(data, marker_columns, title="Correlation Heatmap", save_path=None):
    """
    Plot a correlation heatmap for specified columns.

    Parameters:
        data (pd.DataFrame): The dataset.
        marker_columns (list): List of columns to compute correlations for.
        title (str): Title of the heatmap.
        save_path (str): Path to save the plot, if provided.
    """
    correlation = data[marker_columns].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    _, data = fcs_parser('data/215_0.fcs')
    marker_columns = ['FSC-A', 'SSC-A', 'CD19', 'CD20']

    plot_histogram(data, 'Viability', title='Viability Distribution')

    plot_scatter(data, 'FSC-A', 'SSC-A', title='FSC-A vs SSC-A (Size vs Granularity)')

    plot_density(data, 'FSC-A', 'SSC-A', title='Density Plot: FSC-A vs SSC-A')

    plot_correlation_heatmap(data, marker_columns, title='Marker Correlation Heatmap')
