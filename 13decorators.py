# FIRST CLASS FUNCTION
# first class function- if it treats function as first class basicallyy an entity which supports all 
# the availabe entites of operation,operation is basically argument being passes, return of a 
# function and assignment of a variable
def square(x):
  return x*x
result=square(5)
print(square)
print(result)
x=square #this is know as first class function
print(x)
print(x(10)) # passing function as argument and return function as theie result  is called higher order function

def my_map(func,arg_lst):
  result=[]
  for i in arg_lst:
    result.append(func(i))
  return result
sq=my_map(square,[1,2,3,4,5])
print(sq)

def cube(x):
  return x*x*x
sq1=my_map(cube,[1,2,3,4,5])
print(sq1)
print(cube(4))

# return a function from another function- aspect of 1st class function
def logger(msg):
  def log_msg():
    print('log: ',msg)
  return log_msg #return a function
log_hi=logger('hi') #log_hi result returns a function, so result also needs to be called
log_hi() # this function remembers the value and also can be executed again

def html_tag(tag):
  def wrap_txt(msg):
    print('<{0}>{1}</{0}>'.format(tag,msg))
  return wrap_txt
r1=html_tag('h1')
print(r1)
r1('Text headline')
r1('Amother headline')
r2=html_tag('p')
r2('Paragraph headline!!')

# so basically first class functions means we can assign variables,pass fucntion as arguemnts 
# and return these function as other functions

# CLOSURES
def outer():
  msg='hi'
  def inner():
    print(msg) #msg is called free variable as it can we used anywhere inside outer function
  # return inner()
  return inner #return function 
outer() #does nothing 
res=outer()
print(res)
print(res.__name__)
res() 
res()
# so closure is a inner function that remembers and has access to variables in local scope in which it 
# was created even after the outer function has finished excecution

def outer1(msg):
  mess=msg
  def inner1():
    print(mess)
  return inner1
res1=outer1('Dwija Panchal')
res1()
res2=outer1('21BCP333')
res2()

# DECORATOR- it is a function that take other function as an argument, returns other function 
def decorator(func):
  def wrapper():
    return func()
  return wrapper
@decorator # it is same as result=decorator(display)
def display():
  print("Display function Ran") 
# when we dont use @, we need to write next 2 lines
# dis=decorator(display)
# dis()
display() #by using @ before function makes that @ function connected with it  
# for multiple arguments- use args and kwargs
def decoraor_info(func):
  def wrapper(*args,**kwargs): #takes arguments list mentioned
    print('Excecution before {}'.format(func.__name__))
    return func(*args,**kwargs) #runs the function
  return wrapper
@decoraor_info
def display_info(nm,age):
  print('Name is {} and age is {}'.format(nm,age))
display_info('Dwija',20)

print('USING CLASSES')
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)
@decorator_class
def display1():
  print('Display function ran successfulyy')
display1()

