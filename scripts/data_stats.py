#!/usr/bin/env python3
"""Main source code that computes x- and y-variable statistics"""
import numpy as np
from cmd_line_parsing import parsing
from mean_meansqr import mean_meansqr
from min_max import min_max
from ratio import ratio
from read_clean_file import read_clean

def print_info(values,y_pos, filename = '', cleaned_file = False, output_min_max = False, mean_mean_sqr = False, ratios = False):
    """Write the output file on the command line"""
    
    if cleaned_file == True:
        # print the cleaned output tables
        print(f' Input File: {filename}\n')
        print(f' Cleaned Input File:')
        for l in range(values.shape[1]):
            print(15 * '-',end='')
        print('')
        for l in range(values.shape[1]):
            print(f'   Column {l+1:<1}    ',end='')
        print('')
        for l in range(values.shape[1]):
            if l == y_pos - 1:
                print(f' (y-variable)  ',end='')
            else:
                print(f' (x-variable)  ',end='')
        print('')
        for l in range(values.shape[1]):
            print(15 * '-',end='')
        print('')
        for l in range(values.shape[0]):
            for i in range(values.shape[1]):
                print(f'    {values[l][i]:>6.2f}     ',end='')
            print('')
        for l in range(values.shape[1]):
            print(15 * '-',end='')
        print('')
            
    elif mean_mean_sqr == True:
        # Print the mean and MSE tables
        (means,means_sqr) = values
        print(f'\n\n Mean and Mean Squared Errors(MSE):')
        print(15 * '-',end='')
        for l in range(means.shape[0]):
            print(15 * '-',end='')
        print('')
        print(15 * ' ',end='')
        for l in range(means.shape[0]):
            print(f'   Column {l+1:<1}    ',end='')
        print('')
        print(15 * ' ',end='')
        for l in range(means.shape[0]):
            if l == y_pos - 1:
                print(f' (y-variable)  ',end='')
            else:
                print(f' (x-variable)  ',end='')
        print('')
        print(15 * '-',end='')
        for l in range(means.shape[0]):
            print(15 * '-',end='')
        print('')
        print('     Mean      ',end='')
        for l in range(means.shape[0]):
            print(f'    {means[l]:<8.2f}   ',end='')
        print('')
        print('     MSE       ',end='')
        for l in range(means.shape[0]):
            print(f'    {means_sqr[l]:<8.2f}   ',end='')
        print('')
        print(15 * '-',end='')
        for l in range(means.shape[0]):
            print(15 * '-',end='')
        print('')
            
    elif ratios == True:
        # print the ratios
        print(f'\n\n Ratio of y-variable/x-variable:')
        for l in range(values.shape[0]):
            print(15 * '-',end='')
        print('')
        for l in range(values.shape[0]):
            print(f'   Column {l+1:<1}    ',end='')
        print('')
        for l in range(values.shape[0]):
            if l == y_pos - 1:
                print(f' (y-variable)  ',end='')
            else:
                print(f' (x-variable)  ',end='')
        print('')
        for l in range(values.shape[0]):
            print(15 * '-',end='')
        print('')
        for l in range(values.shape[0]):
            if l == y_pos - 1:
                string = '-'
                print(f'  {string:>6}       ',end='')
            else:
                print(f'   {values[l]:>6.2f}      ',end='')
        print('')
        for l in range(values.shape[0]):
            print(15 * '-',end='')
        print('')
    
    elif output_min_max == True:
        # Print the minimum and maximum for the y-values
        minimum,maximum = values
        print(f'\n\n Minimum and Maximum Values:')
        print(30 * '-',end='')
        print('')
        print(15 * ' ',end='')
        print(f'   Column {y_pos:<1}    ',end='')
        print('')
        print(15 * ' ',end='')
        print(f' (y-variable)  ',end='')
        print('')
        print(30 * '-',end='')
        print('')
        print('     Minimum  ',end='')
        print(f'  {minimum:>8.2f}   ',end='')
        print('')
        print('     Maximum  ',end='')
        print(f'  {maximum:>8.2f}    ',end='')
        print('')
        print(30 * '-',end='')
        print('')
        
    return None
    
    


def main():
    """Main source code"""
    pars_val = parsing() # get the values from the command line
    
    try:
        # Read the dirty file, clean the data, and print information.
        clean_data = read_clean(pars_val.i,pars_val.N) 
        print_info(clean_data,pars_val.y,filename = pars_val.i, cleaned_file = True)
    except AttributeError:
        return None # if -i and -N are not given
    except FileNotFoundError: # if file cannot be found
        print(f"\nCannot find '{pars_val.i}' file.\n") 
        return None
    except IndexError: # too many indexes encounter
        print(f'\nToo many indexes present in the cleaned version of data.') 
        print(f'It may be because:')
        print(f'1.A newline was not added at the end of the file.')
        print(f'2.The number of elements in the column are not equal for each row.')
        print(f'3.There are one or more rows that has no numbers.')
        print(f'4.A digit delimiter is used instead of the other characters.\n')
        return None
        
    if pars_val.M == True:
        # Compute the minimum and maximum
        try:
            minimum, maximum = min_max(clean_data[:,pars_val.y-1])
            print_info((minimum,maximum),pars_val.y, output_min_max = True)
        except IndexError: # this occurs when the indexes are out of bound
            print(f'\nCould not calculate the minimum and maximum.')
            print(f'Indexes are out of bound. Try using a different value of -y and/or -N.\n')
            return None
            
        
    if (pars_val.a == True) or (pars_val.s == True):
        # means and mean squared averages for each column (if -a and/or -s is called)
        try:
            means, means_sqr = mean_meansqr(clean_data)
            if pars_val.a == True: 
                print_info((means,means_sqr),pars_val.y, mean_mean_sqr = True)
        except IndexError: # this occurs when the indexes are out of bound
            print(f'\nCould not calculate the means and mean-squared errors for each column.')
            print(f'Indexes are out of bound. Try using a different value of -y and/or -N.\n')
            return None
            
    if pars_val.s == True:
        # ratio of y divided by x variables for each column
        try:
            ratios = ratio(means,pars_val.y)
            print_info(ratios,pars_val.y, ratios = True)
        except IndexError: # this occurs when the indexes are out of bound 
            print(f'\nCould not calculate the ratios of y/x.')
            print(f'Indexes are out of bound. Try using a different value of -y and/or -N.\n')
            return None   
        
    return None
    
if __name__ == "__main__":
    main()