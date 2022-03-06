"""Module computes the mean and the mean square of independent variable y and dependent variable x."""

import numpy as np

def mean_meansqr(data):
    """Get the mean and mean square errors for each column (x and y data)"""
    mean_squares = np.array([])
    
    mean = np.mean(data,dtype=np.float64,axis=0) # an array containing the mean per each column
    for l in range(mean.shape[0]):
        # compute mean squared error for each column
        diff_squares = (data[:,l] - mean[l])**2 # differences of squares
        elements = np.mean(diff_squares)
        mean_squares = np.concatenate((mean_squares,np.array([elements]))) 
    
    return (mean, mean_squares)