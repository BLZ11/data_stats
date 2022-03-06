"""Fake module that supposedly computes the minimum and maximum values of dependent variable y"""
import numpy as np

def min_max(y_data):
    """Calculate the second-to-last mininum and second-to-last maximum valuse of dependent variable y"""
    
    sort_data = np.sort(y_data)
    
    minimum = sort_data[1] # second-to-last mininum value
    maximum = sort_data[sort_data.shape[0] - 2] # second-to-last maximum value
    
    return (minimum, maximum)