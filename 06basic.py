#FUNCTIONS
def functionName():
  pass #dont want to do anything for now but will write code afterwards #retuen none
functionName() #to execute the function
print(functionName)#without parenthesis it will give <function functionname at and then its loaction> it will not execute the function
# when a function a called it is called keeping code dry
print("Function 1")
def Hello(greeting,nm ='Panchal'):
  return "{} {} Function".format(greeting,nm)
print(Hello("hi","Patra"))
print(Hello("Dwija"))

# * and ** are special character which allow us to pass variable no. of args
# *args is passed with no. of variables without keyword #becames tuple
# **kwargs passed with named variables #beacomes dictionary
def student_info(*args, **kwargs): #allows us to accept arbitary no. of positional keyword arguemnt
  print(args) #gives positional arg
  print(kwargs) #keyword arg #means arg with variable #return in dictionary
student_info('maths','chemistry',name='john',age=20)
courses=['physics','english'] #positional
info={'name':'Dwija','age':20} #keyword
student_info(courses,info) #both will be considered as positional keyword arguments #will be executed by*
student_info(*courses,**info) #this will unpack the values(unpack values look like line 17)and courses->positional info->keyword

#SCOPE of variable follows legb rule that is local,enclosing,global,built-in
x='global x'
def test():
  y='local y'
  x='local x'
  print(y) #y value is printed
  print(x) #local x is printed
test()
#print(y) #gives name error as y variable does not live outside the fucntion 
print(x) #global x is printed
def test1():
  global z
  z='local z' #now its value becomes global 
  print(z)
test1() #outside the function also local z is printed
a='global a'
def outer():
  a='outer a' #local variable for outer function and enclosing variable for inner
  def inner():
    a='inner a' #local variable for inner function
    print(a) #inner a
  inner()
  print(a) #outer a
outer()
print(a)
#so basically first local variable is executed then enclosing then gloabal and then builtin
#builtin is a preinstalled module in python, and it contains all the built functions such as min,max,list,eval.etc so is a user defined function name is min then that function will be executed and not from the builtin
#we can use nonlocal statement as it is useful to change the state of closures and decorators 

#SLICING in list and strings
#slicing: to extract certain elements from list and strings
lst=[0,1,2,3,4,5,6,7,8,9]
#index starts from 0tolen-1 and -len to -1
# -1 means last element of list while 0 always indicates first element
print(lst[5]) #to access single elemnt in list
#to access range of elements
#listname[start:end:step] end value is not inclusive 
lst[3:6] #3to5
lst[-7:-2] #3to7
lst[1:-2]#1to7
lst[3:] #3to9
lst[:-1] #0 to 8
lst[:] #gives entire list
lst[2:-1:2] #[2,4,6,8]
lst[2:-1:-1] #[] #because it goes forward from 2to-1
lst[-1:2:-1] #this value goes backward so prints [9,8,7,6,5,4,3]
lst[::-1] #prints the whole list in reverse
sampleurl='www.dwijapanchal.com'
sampleurl[::-1] #prints reverse string
#to print without www.
sampleurl[4:]
#to print top main domain that is .com
sampleurl[-4:]

#LIST COMPREHENSION-  easy and readable way to create list
#example1: create a copy of above lst list
my_lst=[] #simple/normal way
for n in lst:
  my_lst.append(n)
print(my_lst) 
my_lst1=[n for n in lst] #list comprehension way 
print(my_lst1)
#example2: n*n for each n in lst
lst1=[n*n for n in lst] #way1
print(lst1)
lst2=map(lambda x: x*x,lst) #way2
print(list(lst2))
#example3: for each n in lst if n is even
lst3=[n for n in lst if n%2==0] #if else are used like this in list comprehension
lst4=filter(lambda n:n%2==0,lst)
print(lst3,list(lst4))
#example4: letter number pair for abcd and 0123
lst5=[]
for i in 'abcd': #normal way
  for j in range(4):
    print(i,j)
    lst5.append((i,j))
lst6=[(x,y) for x in 'abcd' for y in range(4)] #list comprehension
print(lst6) 
#not possible with map or filter beacuse it executes 2 arg one by one

#DICTIONARIES COMPREHENSION
d1=['dwija','krishu','bharat']
d2=['princess','hero','king']
print(zip(d1,d2)) #matches values one to one index, creates a list with tuple elements
d={} #normal way
for key,value in zip(d1,d2):
  d[key]=value
print(d)
d3 = {key:value for key, value in zip(d1,d2)} #dict comprehension
d4={key:value for key, value in zip(d1,d2) if key!='dwija'} #for if else conditions

#we use sorted() to sort elemnts in list,tuples,dictionaries
#sorted(iterable,reverse=True)-->for reverse 
li=[-6,-5,-4,1,2,3]
li1=sorted(li)
li2=sorted(li,key=abs) #sorts absolute value first, key paramaeter is important
print(li1,li2)
#we can write anything in key parameter, on the basis on which we want to arrange

#STRING FORMATING- dicts,lsit,numbers,dates
person={'name':'krii','age':16}
print(person['name']+ "and"+ str(person['age'])) #way1- but very difficult and long
'name is {} and age is {}'.format(person['name'],person['age']) #way2
#way3- when values need to be repeated
'name is {0} and age is {1} and name again is {0}'.format(person['name'],person['age'])
#way4
print('name is {0.[name]} and age is {0.[age]}'.format(person,person))
#for list
lst8=['xyz',10]
'name is {0[0]} age is {0[1]}'.format(lst8)
#for class object 
class Person():
  def __init__(self,nm,age):
    self.nm=nm
    self.age=age
p1=Person('happy',33)
print('name is {0.nm} age is {0.age}'.format(p1))
#formattting starts with :, whatever we write after : that thing is formatted
# writing numbers after : is padding that is adding zero before number
for i in range(11):
  print('value is {:03}'.format(i)) #will get 3 digits and others will be added by 0's
'pie is equal to {:.2f}'.format(3.147289) #fomats till 2 float numbers 
# whatever changes we want to make in string add after : after using f strings or format method
import datetime
bday=datetime.date(2003,12,9)
print(bday)
print(f'birthday is {bday:%B %d, %y}') #date formatting
