import pandas as pd
from parser import fcs_parser

def generate_summary(data):
    """
    Generates a statistical summary of a FCS dataset

    Parameters:
        data (pd.DataFrame): Data parsed from a FCS file

    Returns: 
        report (pd.DataFrame): Summary report of the data
    """
    report = data.describe()
    return report

if __name__ == "__main__":
    _, data = fcs_parser('data/215_0.fcs')
    report = generate_summary(data)
    print(report)