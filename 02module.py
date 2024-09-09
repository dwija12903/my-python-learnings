#import modulename
#module.function(arg) #to access the module functions

#from modulename as m import functionname1 as x,functionname2 #only functions mentioned here will to accessed

#from modulename import *  #will same as import modulename

#when a module is imported it checks loactions and the locations are present within list sys 
import sys
print(sys.path) # tells all the paths #list of directorys, python sees when we run a module
sys.path.append('directory name')

import math 
math.radians(90)
math.sin(math.radians(90))

import builtins
print(dir(builtins))

from operator import attrgetter
#used in key parameter to sort list with tuple elements 

#dont used builtin module name for module name 
#to import module there are many ways:
#1) import modulename
#	modulename.functionname(arg) #to acess function
#2) import modulename as variableNameForModule  #be x x.FunctionNAme
#3) from ModuleName import FunctionName #from here you can directly access fnction by name
#4) from modulenname import * #imports all the functions
#to know all the build in modules go to python documetation online then gobal module index

#script: executes something and uses modules
#module: execute nothing and contains function,variables 
#package: collection to related modules to achieve certain functionality
#library: collection of libraries to achieve wide range of functionality

import os #allows us to interact with os
os.getcwd() #gives current working directory
os.__file__ #location of file
dir(os) #allows to access all the functions
os.chdir('path') #to change directory
os.listdir() #lists path and floders in current directory
os.mkdir('foldername') #makes that folder/directory in the current directory
os.makedirs('foldername/subfolder2') #same as above but allows us to create inner directorys also
os.rmdir('path name') #reomve directory
os.removedirs('path name') #same as above
os.rename('original file name','new name file')
os.stat('filename') #gives all the details about the file and to access individual value .value 
os.walk('directory') #generater of tuple of 3 values with the given directory
os.environ() # prints all env
os.environ.get('home') #gives only particular env 
os.path.join('path1','file name') #join both the paths
os.path.basename('') #gives basename from the directory
os.path.dirname('')
os.path.split('') #seperates all the path in directory into list
os.path.exists('')
os.path.isdir('') #returns true if it is a dir
os.path.isfile('') #returns true is it is file

# import datetime
# import calendar as c
# import pytz #for time zone
# today=datetime.date.today() #todays date
# c.isleap(2017)
# #working with dates-month,day,year
# datetime.date(2003,9,12)#don't pass zeros before single digits #cretes date
# tday=datetime.date.today()
# tday.year
# tday.day
# tday.weekday() #monday is 0 and sunday is 6
# tday.isoweekday() #monday is 1 and sunday is 7
# #time deltas are diffrence bw two dates 
# tdelta=datetime.timedelta(days=7)
# tday+tdelta #gives +7 days # we can +,-
# #to calulate days left for my bday
# bday=datetime.date(2003,9,12)
# till_bday= bday- tday
# till_bday.days
# till_bday.total_seconds()
# #working with time-hrs,mins,seconds
# t=datetime.time(9,30,45,100000) #hrs,mins,secs,mirosecs
# t.hour
# dt=datetime.datetime(2016,7,26,12,30,45,100000)
# dt.time()
# dt.date()
# dt.year
# dt+tdelta #week +1
# #working with date time togather
# datetime.datetime.today() #current local date with none time zone
# datetime.datetime.now() #gives option of timezone
# datetime.datetime.utcnow() #time zone aware
# #with timezone 
# dttz=datetime.datetime(2016,7,24,12,30,54,tzinfo=pytz.UTC) #prints along with current datetime 
# tz=datetime.datetime.now(tz=pytz.UTC) #way1 to get timezone #current time with timezone
# datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)#way2 to get timezone
# pytz.all_timezones #gives all the timezone list with area 
# tz.astimezone(pytz.timezone('US/Moutain')) #gives the timezone 
# #to display the date use isoformats
# date1=datetime.datetime(2003,9,12,2,45,52)
# print(date1) 
# print('{:%B %d, %Y}').format(date1) #change format
# print('{:%B} {:%A %j}'.format(date1))

# import random
# random.random() #gives value b/w 0 and 1, 1 exclusive #gives floating values
# random.uniform(1,10) #floating value b/w 1 to 9.999999
# random.randint(1,6) #both inclusive #return integer no float
# num=['hello','hi','hey','howdy']
# random.choice(num) #guves random value from list
# colours=['red','black','green']
# res=random.choices(colours,k=10,weights=[18,18,4]) #gives list of 10 random results from the list #weights tell the probability red has 18 black has 18 green has 4 
# print(res)
# deck=list(range(1,53))
# random.shuffle(deck) #we didnt use choices as it gives repeated values too #shuffle gives unique values from the input list
# random.sample(deck,k=5) #gives any k values from the list 

# when we import a module of our created python file, it acutally runs the whole code of that module
#basically, __name__ = module name 
print('first module name',__name__) 
# when we import a module __name__=name of file
# when name=main, means the current file is only running
# if __name__=__main__ tells that if this file is directly run by python then goes to next condition




















