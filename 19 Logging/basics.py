# replace print statement by log statement
# log information to files 
# logging is same as print but it is very useful once project gets complex
# we can pipe it in some visvulization software to get better perespective
import logging
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

a=10
b=5
addres = add(a,b)
subres = subtract(a,b)
mulres = multiply(a,b)
divres = divide(a,b)

# logging levels allows us to specify what we want to log by seperating into categories
# from python documentation:
#DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk
# space low'). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging level is set to warning
logging.warning('Addition= {}'.format(addres))
# without using basiccongif, output is printed in terminal

logging.basicConfig(filename='log_script.txt',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
# DEBUG is diffrent from debug, it is just a constant that is integer in background
# by mentioning filename contents gets copy there and no output
# to change format of logging methods

logging.debug('Substraction= {} of {} - {}'.format(subres,a,b))
# after changing vaalues the previous ingo will be saved and new will be appended
logging.debug('Multiplication= {}'.format(mulres))

