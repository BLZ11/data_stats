# data_stats 
data_stats is a Python program that reads data from a dirty file, cleans it, and extracts the x-variables and y-variable. 

Users can compute statistics such as:
1. minimum and maximum (for y-variable only)
2. averages and mean squared errors (MSE)
3. the ratio between the y-variable divided by each x-variable column.

All calculations were done using ```numpy``` API.

## How to run
Execute the code as:

```bash 
data_stats.py -N <number_of_columns> -y <position_of_y> -M -a -s -i <data_file> 
```
where

- ```-N <number_of_columns>``` specifies the total number of data columns (N), including y;
- ```-y <position_of_y>``` specifies which column (1 to N) contains the dependent variable y;
- ```-M``` the output shows the minimum and the maximum value of y;
- ```-a``` the output shows the average and the mean square of each column;
- ```-s``` the output shows the ratio between the average of y variables divided by the average of each of the x variables;
- ```-i <data_file>``` specifies the name of the data file to be analized;

Options ```-N```, ```-y```, and ```-i``` are mandatory.
At least one of ```-M```, ```-a```, or ```-s``` must be used.

Any variation of the command line is possible.

## Generating output
The mentioned command line prints the output. 

If the user prefers the output as a text file, execute the code as:
```bash 
data_stats.py -N <number_of_columns> -y <position_of_y> -M -a -s -i <data_file> > <output_file>.txt
```
where
- ```<output_file>``` specifies the name of the output file (user-defined)

## Modules
```data_stats.py``` uses five modules as separate Python files:
- ```cmd_line_parsing.py``` command line parsing
- ```read_clean_file.py``` data input file reading and cleaning 
- ```min_max.py``` minimum and maximum of y (gives fake results)
- ```mean_meansqr.py``` mean and mean square error for x and y
- ```ratio.py``` ratio between averages of y column to x columns 

For information on the API used for each of these modules, visit ```scripts/api_info.md```.

## Sample files

Some sample text files are present in ```test_files``` folder. This includes:
- ```DataFilePassed.txt``` which is free from exceptions 
- ```mis1.txt``` and ```mis2.txt``` which triggers exceptions
