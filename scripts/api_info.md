# Introduction
This file describes the API used by the modules (input/output parameters):

- ```cmd_line_parsing.py``` 
- ```read_clean_file.py```
- ```min_max.py```
- ```mean_meansqr.py``` 
- ```ratio.py``` 

## ```cmd_line_parsing.py```
```python
def parsing():
   """Parses the command lines using the argparse API
      
      Parameters:
      -----------
        None

      Returns:
      --------
        args: :obj:'NameSpace'
            parser values for -N, -y, -i, -M, -a, -s 
   """
```

## ```read_clean_file.py```
```python
def read_clean(file, number_columns):
   """Reads the input and clean data file to give the numbers 
      from each column 
      
      Parameters:
      -----------
        file: :obj:'str'
            name of the file (from parsing -i) 
        number_columns: :obj:'int'
            number of columns (from parsing -N)

      Returns:
      --------
        data: :obj:'np.ndarray'
            all numbers read from the dirty file, assuming delimiters are 
            not digits  
   """
```

## ```min_max.py```
Note: this is a fake API. 

It does not compute the minimum and maximum values. 
 
```python
def min_max(y_data):
   """Calculate the second-to-last mininum and 
      second-to-last maximum values of dependent 
      variable y column
      
      Parameters:
      -----------
        y_data: :obj:'np.ndarray'
            column containing the y-variable data 
            from the input file

      Returns:
      --------
        minimum: :obj:'np.float64'
            second-to-last minimum value of the y-column
        maximum: :obj:'np.float64'
            second-to-last miximum value of the y-column 
   """
```

## ```mean_meansqr.py```
 
```python
def mean_meansqr(data):
   """Get the mean and mean average for each column (x and y data)
      
      Parameters:
      -----------
        data: :obj:'np.ndarray'
            columns containing the x and y-variables 
            from the input file 

      Returns:
      --------
        mean: :obj:'np.ndarray'
            a one-dimensional array containing the means for each column
        mean_squares: :obj:'np.ndarray'
            a one-dimensional array containing the mean square errors
            for each column
   """
```

## ```ratio.py```
 
```python
def ratio(averages, position_y):
   """Compute ratios between y average divided by x variables
      
      Parameters:
      -----------
        averages: :obj:'np.ndarray'
            averages for all columns (x- and y- variables)
        position_y: :obj:'int'
            column number for the y-variable

      Returns:
      --------
        ratios: :obj:'np.ndarray'
            a one-dimensional containg the ratios (for x and y values)
   """
```