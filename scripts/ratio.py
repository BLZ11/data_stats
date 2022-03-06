"""Module computes the ratio of the averages between y average divided by each x average"""
import numpy as np

def ratio(averages, position_y):
    """Compute ratios between y average divided by x averages"""
    
    ratios = averages[position_y-1] / averages # ratio of the y average and x averages
    
    return ratios