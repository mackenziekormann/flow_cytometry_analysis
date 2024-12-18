from analyzer.parser import fcs_parser
import pytest
import pandas as pd


filepath = 'data/215_0.fcs'
meta, data = fcs_parser(filepath)


def test_parse_valid_file():
    assert isinstance(data, pd.DataFrame), "Data is a Pandas DataFrame"
    assert isinstance(meta, dict), "Metadata is a dictionary"
    assert data, "Data should be non-empty for a valid FCS file"
    assert meta, "Metadata should be non-empty for a valid FCS file"

def test_non_existent_file():
    fake_filepath = 'data/216_0.fcs'
    with pytest.raises(FileNotFoundError):
        fcs_parser(fake_filepath)