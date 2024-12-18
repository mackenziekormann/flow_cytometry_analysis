import pytest
import pandas as pd
from analyzer.parser import fcs_parser
from analyzer.analysis import (
    clustering,
    compare_populations,
    calculate_population_statistics,
    identify_outliers,
    calculate_cluster_proportions,
    marker_pair_correlation,
)

filepath = 'data/215_0.fcs'
meta, data = fcs_parser(filepath)

def test_clusters():
    labels = clustering(data, n_clusters=2)
    assert len(set(labels)) == 2, "Number of cluster should be equal to number of labels"
