"""Module that uses the argparse API to parse the command line"""
import argparse
import numpy as np


#-------------------------------------------------------- 
# These classes contains the exception errors for each usage error 
class Error1(ValueError): pass
class Error2(TypeError): pass
class Error3(KeyError): pass

# This class overides the usage error from argparse to make an exception error
# If we do not do this, we will not be able to make exceptions. 
class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        keys = np.array(['-N','N','-y','Y','i','-i'])
        for i in keys:
            if message == 'argument ' + i +': expected one argument':
                raise Error1(message) 
            if message == 'argument ' + i +': invalid int value':
                raise Error2(message)
            if (message[:23] == 'unrecognized arguments:') or (message[:37] == 'the following arguments are required:'):
                raise Error3(message)
#---------------------------------------------------------
def parsing():
    """Parses the command line using the argparse API""" 
    
    parser = ThrowingArgumentParser(description = 'compute statistics for x and y variables.') 
    parser.add_argument('-N', action = 'store', help = 'number of columns', required = True, type = int)  
    parser.add_argument('-y', action = 'store', help = 'position of the y-variable', required = True, type = int)
    parser.add_argument('-i', action = 'store', help = 'name of the data file', required = True, type = str)
    parser.add_argument('-M', action = 'store_true', help = 'minimum and maximum value of y-variable', required = False)
    parser.add_argument('-a', action = 'store_true', help = 'average and mean square of x- and y-variables', required = False)
    parser.add_argument('-s', action = 'store_true', help = 'ratio of the average of y-variables divided by x-variables', required = False) 

    try:
        args = parser.parse_args()
        if (args.M == False) and (args.a == False) and (args.s == False):
            print(f'There must be at least one -M -a -s')
            return None
        else:
            return args
    except ValueError:
        print('\nValue for -N and -y, and/or -i are missing\n')
        return None
    except TypeError:
        print('\nProgram is reading a non-integer number for -N and/or -y')
        print('It may be:') 
        print("1. '-' is added before N and y")
        print('2. Not to compact -N,-y, and/or -i. You can compact these terms with other optional keys.')
        print('3. Use any integer number greater than 0. No special characters or letters are used\n')
        return None
    except KeyError:
        print('\nSeveral problems may have occured')
        print('It may be:')
        print('1.Missing -N, -y, and/or -i keys in the command line')
        print('2.Forgot to add hyphens to the optional.')
        print('3.Made up key terms')
        print('4.Key terms are repeated more than once.\n')
        return None