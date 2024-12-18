import fcsparser
import os

def fcs_parser(fcs_filepath):
    """
    Parses an FCS file and returns metadata and data.

    Parameters: 
        fcs_filepath (str): Path to the FCS file

    Returns: 
        metadata (dict): Metadata
        data (pd.DataFrame): Flow cytometry event data

    Raises:
        FileNotFoundError: If the file does not exist at the given path
        ValueError: If the file is not the correct format or is corrupted
    """
    if not os.path.exists(fcs_filepath):
        raise FileNotFoundError(f"The file at '{fcs_filepath}' does not exist.")
    
    if not fcs_filepath.lower().endswith('.fcs'):
        raise ValueError(f"File at '{fcs_filepath}' not of the .fcs format.")
    
    meta, data = fcsparser.parse(fcs_filepath, reformat_meta=True)

    return meta, data

def jo_parser(jo_filename):
    pass

if __name__ == "__main__":
    meta, data = fcs_parser('data/215_0.fcs')
    print(data)