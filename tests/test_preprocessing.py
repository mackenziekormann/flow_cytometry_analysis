import pytest
import pandas as pd
from analyzer.preprocessing import (
    debris_removal, remove_dead, normalize, remove_outliers, remove_doublets
)
from analyzer.parser import fcs_parser

filepath = 'data/215_0.fcs'
meta, data = fcs_parser(filepath)

def test_debris_removal():
    filtered_data = debris_removal(data, fsc_threshold=1500, ssc_threshold=1500)
    assert filtered_data['FSC-A'].min() >= 1500
    assert filtered_data['SSC-A'].min() >= 1500

def test_remove_dead():
    filtered_data = remove_dead(data, threshold=2000)
    assert filtered_data['Viability'].min() >= 2000

def test_remove_dead_missing_column():
    data = data.drop(columns=['Viability'])
    with pytest.raises(KeyError):
        remove_dead(data, threshold=2000)

def test_normalize_zscore():
    normalized_data = normalize(data[['FSC-A', 'SSC-A']], method='zscore')
    assert normalized_data.mean().round(2).all() == 0
    assert normalized_data.std().round(2).all() == 1

def test_normalize_minmax():
    normalized_data = normalize(data[['FSC-A', 'SSC-A']], method='minmax')
    assert normalized_data.min().all() == 0
    assert normalized_data.max().all() == 1

def test_normalize_invalid_method():
    with pytest.raises(ValueError):
        normalize(data, method='invalid')