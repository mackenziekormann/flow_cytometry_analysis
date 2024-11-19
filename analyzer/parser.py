import fcsparser

def fcs_parser(fcs_filepath):
    """
    Parses an FCS file and returns metadata and data.

    Parameters: 
        fcs_filepath (str): Path to the FCS file

    Returns: 
        metadata (dict): Metadata
        data (pd.DataFrame): Flow cytometry event data
    """
    meta, data = fcsparser.parse(fcs_filepath, reformat_meta=True)

    return meta, data

def jo_parser(jo_filename):
    pass

if __name__ == "__main__":
    meta, data = fcs_parser('data/215_0.fcs')
    print(data)