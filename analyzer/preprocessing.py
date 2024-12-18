from parser import fcs_parser

def debris_removal(data, fsc_threshold=500, ssc_threshold=500):
    """
    Removes debris based on forward scatter (FSC) and side scatter (SSC) thresholds.

    Parameters:
        data (pd.DataFrame): Data parsed from a FCS file
        fsc_threshold (int): Set to 500, sets the lower bound of forward scatter area for cells
        ssc_threshold (int): Set to 500, sets the lower bound of side scatter area for cells

    Returns:
        data (pd.DataFrame): Updated dataframe with cells with forward and side scatter below the threshold removed
    """
    return data[(data['FSC-A'] > fsc_threshold) & (data['SSC-A'] > ssc_threshold)]

def remove_dead(data, threshold=1500):
    """
    Removes dead cells based on viability data. 

    Parameters: 
        data (pd.DataFrame): Data parsed from a FCS file
        threshold (int): Set to 1500, sets lower bound for viability of cells to be classified as living

    Returns:
        pd.DataFrame: Updated dataframe with remaining cells above the threshold

    Raises: 
        KeyError: If 'Viability' column is missing
    """
    if 'Viability' not in data.columns:
        raise KeyError("Viability column not found in the data.")
    
    return data[data['Viability'] > threshold]

def normalize(data, method='zscore'):
    """
    Normalizees data using the specified method.
    
    Parameters: 
        data (pd.DataFrame): Data parsed from a FCS file
        method (str): Method used to normalize data
            - 'zscore': Standardize to mean=0, std=1
            - 'minmax': Scale to range [0,1]

    Returns:
        data (pd.DataFrame): Normalized dataframe
    """
    if method == 'zscore':
        return (data - data.mean()) / data.std()
    
    elif method == 'minmax':
        return (data - data.min()) / (data.max() - data.min())
    
    else:
        raise ValueError("Unsupported normalization method. Supported methods are 'zscore' or 'minmax'.")
    
def remove_outliers(data, method='zscore', threshold=3):
    """
    Remove outliers using the specified method.

    Parameters: 
        data (pd.DataFrame): Data parsed from a FCS file
        method (str):
            - 'zscore': Exclude points where |z| > threshold
            - 'iqr': Exclude points outside 1.5*IQR

    Returns:
        data (pd.DataFrame): Updated dataframe with outliers removed
    """
    if method == 'zscore':
        z_scores = (data - data.mean()) / data.std()
        return data[(z_scores.abs() < threshold).all(axis=1)]
    
    elif method == 'iqr':
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        iqr = Q3 - Q1
        return data[((data >= Q1 - 1.5 * iqr) & (data <= Q3 + 1.5 * iqr)).all(axis=1)]
    
    else:
        raise ValueError("Unsupported method. Supported methods are 'zscore' and 'iqr'.")
    
def remove_doublets(data):
    """
    Removes doublets from flow cytometry data using FSC-H and SSC-H columns.
    Doublets are events with disproportionately high height compared to area.

    Parameters:
        data (pd.DataFrame): Flow cytometry data.

    Returns:
        pd.DataFrame: DataFrame with doublets removed, or the original DataFrame if height columns are missing.

    Raises: 
        KeyError: If FCS or SSC height columns not found
    """
    if 'FSC-H' not in data.columns or 'SSC-H' not in data.columns:
        raise KeyError("One or more height columns not found.")
    
    data['FSC_Ratio'] = data['FSC-H'] / data['FSC-A']
    data['SSC_Ratio'] = data['SSC-H'] / data['SSC-A']

    fsc_lower, fsc_upper = 0.8, 1.2
    ssc_lower, ssc_upper = 0.8, 1.2

    filtered_data = data[
        (data['FSC_Ratio'] >= fsc_lower) & (data['FSC_Ratio'] <= fsc_upper) &
        (data['SSC_Ratio'] >= ssc_lower) & (data['SSC_Ratio'] <= ssc_upper)
    ]

    filtered_data = filtered_data.drop(columns=['FSC_Ratio', 'SSC_Ratio'])
    return filtered_data

    
def preprocess_pipeline(data, steps, **kwargs):
    """
    Apply preprocessing steps to flow cytometry data.

    Parameters:
        data (pd.DataFrame): Data parsed from a FCS file
        steps (list): List of preprocessing functions to apply
        kwargs (dict): Additional arguments for each function

    Returns:
        pd.DataFrame: Preprocessed data
    """
    for step in steps: 
        func = step['function']
        func_kwargs = step.get('kwargs', {})
        data = func(data, **func_kwargs)
    return data
    
if __name__ == '__main__':
    meta, data = fcs_parser('data/215_0.fcs')
    steps = [
    {'function': debris_removal, 'kwargs': {'fsc_threshold': 600, 'ssc_threshold': 600}},
    {'function': remove_dead, 'kwargs': {'threshold': 2000}},
    {'function': normalize, 'kwargs': {'method': 'zscore'}},
    {'function': remove_outliers, 'kwargs': {'method': 'zscore', 'threshold': 3}},
    ]

    preprocessed_data = preprocess_pipeline(data, steps)
    print(preprocessed_data)
