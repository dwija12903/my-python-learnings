import logging 
from employee import Employee

# when we don't specify any logger, by default root logger is considered. Specific logger
# can be congifured seperately

# logging.basicConfig(filename='E:/VS studio/Python/to learn py/19 Logging/sample.log',level=logging.INFO)

emp1 = Employee('Sudha','Murty')
emp2 = Employee('Durjo','Dutta')
# all this logging is executed onto the file.log file and not onto the sample.log because of logger 
# both have same root logger, so it does again overwrites the value onto the sample.log file 
# to configure both seperately we need to create, new logger

logger = logging.getLogger(__name__) #logger is created
logger.setLevel(logging.INFO) #sets the level to new logger
formatter = logging.Formatter('%(name)s :%(levelname)s: %(asctime)s: %(message)s') #to set format
file_handler = logging.FileHandler('E:/VS studio/Python/to learn py/19 Logging/sample.log') #filename
file_handler.setFormatter(formatter) #it sets the fortmat for The file
logger.addHandler(file_handler) 

logger.info('My name is dwija') 
emp3 = Employee('Dan','brown')

# so here employee class realted loggings are printed in employee.log beacuse we have created new logger 
# so basically new logger logges files are saved in sample.log and the rest which are runned under 
# employee module are saved in employee.log

# %(name)s tells the module used 
# when name=module name it means that it is excecuted from some other file module
# for example: line 3 in employee.log