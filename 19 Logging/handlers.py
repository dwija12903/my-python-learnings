import logging

logger = logging.getLogger(__name__)

# create file handler
file_handler = logging.FileHandler('E:/VS studio/Python/to learn py/19 Logging/handlers.log')
stream_handler = logging.StreamHandler() #for streams, output executed in terminal

# set level of file
file_handler.setLevel(logging.WARNING)
stream_handler.setLevel(logging.ERROR)

# adding format to files
formatter = logging.Formatter('%(name)s :%(levelname)s: %(asctime)s: %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# add files to logger created
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging
logger.warning('This is warning message')
logger.error('this is error message')

# so basically stream handler loggings are printed in terminal 
# file handler executes all the loggings