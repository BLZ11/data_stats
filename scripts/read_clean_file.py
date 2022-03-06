"""Module includes an API that reads the dirty input file and cleans any unecessary data"""
import numpy as np

def read_clean(file,number_columns):
    """Reads the input and clean data file to give the numbers from each column"""
    
    data = []
    status = 'initiate' # start reading the characters
    with open(file,mode='r') as reader: # read the file
        for rows in reader.readlines() : # read each row
            n = 0
            row_elements = np.array([]) # array the contains the numbers at rows
            for columns in rows: # read each column
                
                # Check if the leading character is a digit,-, or . 
                # if so, initiate the string variable and change the status to 'concatenate'
                if status == 'initiate':
                    if columns in np.array(['0','1','2','3','4','5','6','7','8','9']):
                        string = columns
                        status = 'concatenate'
                    elif (columns == '.') and (rows[n+1] in np.array(['0','1','2','3','4','5','6','7','8','9'])): # for decimal numbers with no 0 at the end
                        string = columns 
                        status = 'concatenate'
                    elif (columns == '-') and (rows[n+1] in np.array(['0','1','2','3','4','5','6','7','8','9'])): # for negative numbers
                        string = columns 
                        status = 'concatenate'
                        
                # Append the characters that makes part of the "correct" number
                # otherwise, initiate the string change the status to 'final' 
                elif status == 'concatenate':
                    if columns in np.array(['0','1','2','3','4','5','6','7','8','9']):
                        string += columns
                    elif (columns == '.') and (rows[n+1] in np.array(['0','1','2','3','4','5','6','7','8','9'])): 
                        string += columns
                    elif (columns == '.') and (rows[n+1] == '\n'):
                        status = 'final'
                    elif columns not in np.array(['0','1','2','3','4','5','6','7','8','9']):
                        status = 'final'
                        
                # Convert the "correct" number to a double precision number
                # Change the status variable to 'initiate' to repeat the steps mentioned above
                if status == 'final':
                    numbers = np.float64(string)
                    row_elements = np.concatenate((row_elements,np.array([numbers])))
                    status = 'initiate'                           
                n += 1
                
            # append the arrays of row_elements after reading the rows    
            data += row_elements,  
            
        reader.close() # close the file
    data = np.array(data) # convert list to np.ndarray         
    return np.array(data[:data.shape[0],:number_columns]) #data        