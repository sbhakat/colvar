import os.path as op
import numpy as np
import pandas as pd

def read_colvar_header(filename, *column_names):
    """
    Read header from Plumed output. The header looks like "#! FIELDS time var1 var2"
    ----------
    filename : string
        Name of the plumed file that contains collective variable data
        (e.g. COLVAR).

    *column_names: string
        column names in COLVAR files
    Returns
    -------
    data : dictionary containing column names in COLVAR files
    
    """
    
    variables = dict.fromkeys(column_names, 0)
    with open(filename) as f:
        head = next(f).strip().split() 
    for k in variables:
        variables[k] +=head.index(k)-2
    return variables

def read_colvar(filename, *column_names):
    """
    Read header from Plumed output. The header looks like "#! FIELDS time var1 var2"
    ----------
    filename : string
        Name of the plumed file that contains collective variable data
        (e.g. COLVAR).

    *column_names: string
         column names in COLVAR files
    Returns
    -------
    data : dict

    Values corresponding column names

    >>> data = read_colvar("COLVAR","time", "tic1", "metad.rbias")
    >>> data
    >>> data['time']
    
    """
    column_numbers = read_colvar_header(filename, *column_names)
    colvar_data = dict.fromkeys(column_numbers.keys(),None)
    for k, v in column_numbers.items():
        colvar_data[k] = np.loadtxt(filename, comments="#!",usecols=v)
    return colvar_data


def transform(arrays):
    """
    Concatanate two arrays
    Example:
    data = read_colvar("COLVAR","chi1", "chi2", "chi2")
    data_transform = transform([data['chi1'], data[chi2], data[chi3]])
    
    """
    return np.vstack(arrays)
