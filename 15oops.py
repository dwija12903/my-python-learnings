# we use classes and object as they allow us to locigically group or data and functions un a easy way 
# method is a function associated with class
# attributes are variables associated with class
import datetime
class employee():
  pass
class Employee:
  raise_amt=1.04 #CLASS VARIABLE #to access class variable we use self inside a method
  num_of_emp=0
  def __init__(self,first,last,pay): #constructor #initializing method
    self.first = first
    self.last = last
    self.pay = pay
    self.email =first+'.'+last+'@comapny.com' 

    Employee.num_of_emp += 1
  def fullname(self): #self is the 1st arg #obj name
    return '{} {}'.format(self.first,self.last)
  def apply_raise(self):
    self.pay=int(self.pay*self.raise_amt) #to access class variable also we need to use self  
  @classmethod
  def set_raise_amt(cls,amt): #cls is comman convention for class variable as it is self for instance 
    cls.raise_amt = amt

  @classmethod
  def from_string(cls,emp_str):
    first,last,pay=emp_str.split('-')
    return cls(first,last,pay)
  
  @staticmethod
  def workday(day):
    if day.weekday()== 5:
      return False
    return True
  
  def __repr__(self): #need to call them when we want to access with objects
    return "Employee '{}' '{}' '{}'".format(self.first,self.last,self.pay)
  def __str__(self):
    return '{}-{}'.format(self.fullname(),self.email)
  def __add__(self,n): 
    return self.pay+n.pay
  def __len__(self):
    return len(self.fullname())
  
  @property #use to convert method into attribute
  def fullnm(self): #Getter 
      return '{} {}'.format(self.first, self.last)
    
  @fullnm.setter
  def fullnm(self, name):
      first, last = name.split(' ')
      self.first = first
      self.last = last
    
  @fullnm.deleter
  def fullnm(self):
      print('Delete Name!')
      self.first = None
      self.last = None

# class is a blueprint to create an instance of a class and each unique employee will be the intsance of class

empp = employee() #instance of class emp1
emp2=employee()
print(empp)
print(emp2) #emp1 and emp2 both will have different location 
empp.first='bharat'
empp.last='panchal'
empp.pay=400000
emp2.first='dwija'
emp2.last='panchal'
emp2.pay=3000000 #difficult to use
print('dwija\'s salary is',emp2.pay)
print("Employee1= ",empp.first,empp.last)

emp=Employee('krishiv','panchal',5000000)
print(emp.last)
print('{} {}'.format(emp.first,emp.last)) #takes alot of time for print when we want for more instance instead we can create a method inside class
emp.fullname() #gives the same as above of print 
Employee.fullname(emp) #same as above code #other way 

print("BEFORE= " ,emp.pay)
emp.apply_raise()
print("AFTER= " ,emp.pay)

# we can access class variable from both instances and class 
print(emp.raise_amt) #to access class variable we need to use instance
print(Employee.raise_amt) #access from class
# no change has been done here so class and instance variabke value remains same

print(emp.__dict__) #gives the dictionary from emp object 
print(Employee.__dict__)

Employee.raise_amt = 1.05 #class variables changed #for the class and for all instance
print("change of class variable= " ,Employee.raise_amt) 
emp.raise_amt = 1.08  #INSTANCE VARIABLE #change of class variable only for instance
print(emp.raise_amt) #only insatnce variable is change, class variable remains same 
print(Employee.raise_amt)

print("Total number of objects created= ",Employee.num_of_emp)
empll=Employee('pragna','panchal',3000000)
print(empll.__dict__)
for key,value in empll.__dict__.items():
  print(key, "\t", value)
print("Update no. of employess= ", Employee.num_of_emp)

# DIFRRENCE B/W regular method, class methods, static methods
# regular methods automatically take instance as first argument 
# class methods take class as argument for doing that we use classmethod decorator
print(Employee.raise_amt)
print(emp.raise_amt)
print(empll.raise_amt)
Employee.set_raise_amt(1.04) #class methods are runned using class 
print(Employee.raise_amt)
print(emp.raise_amt) #value of instance doesnot changes 
print(empll.raise_amt)

emp_str_1 ='john-doe-7000' 
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-doe-90000'
first,last,pay=emp_str_1.split('-')
new_emp1 = Employee(first,last,pay)
print(new_emp1.email)
print(new_emp1.pay)
# this is difficult so let us create a construstor 
new_emp2 = Employee.from_string(emp_str_2)
print(new_emp2.__dict__)

# static methods- dont take instance or class as first argument 
date = datetime.date(2016,7,10)
print(Employee.workday(date))

# INHERITANCE
class developer(Employee): #developer class inherits from employeee #it has all the attritubes and method inside employee class
  raise_amt=1.10
  def __init__(self, first, last, pay,prg):
    super().__init__(first, last, pay) #this passes the other arguments from superclass
    self.prg=prg

dev1 = developer('test','employee',50000,'python') #when created it first looked into developer class and then if it doesnot find anything inside it then it goes to employeee class and this is know as method resolution
dev2=developer('john','william',40000,'java')

# print(help(developer)) #we get all kind of information #method resolution--> class selection order #methods inheritaed

print("Before= ", dev1.pay) #as developer class as that class variable so value 1.10 will be considered
dev1.apply_raise()
print("After= ",dev1.pay)

print(dev1.email)
print(dev1.prg)

class manager(Employee):
  def __init__(self, first, last, pay,employee=None): #we pass none instead of [] beacuse we cant pass mutable datatypes as default arguments
    super().__init__(first, last, pay)
    if employee is None:
      self.employee=[]
    else:
      self.employee=employee
  
  def add_emp(self,emp):
    if emp not in self.employee:
      self.employee.append(emp)

  def remove_emp(self,emp):
    if emp in self.employee:
      self.employee.remove(emp)
  
  def print_emp(self):
    for emp in self.employee:
      print('-->',emp.fullname())

mgr1=manager('sue','smith',90000,[dev1])
print(mgr1.email)
print("before==")
mgr1.print_emp()
print("Adding employee")
mgr1.add_emp(dev2)
mgr1.print_emp()
print("Removing employee")
mgr1.remove_emp(dev1)
mgr1.print_emp()

# python has 2 builtin functions 
# isinstance() tells if an object is a instance of class
print(isinstance(mgr1,manager))
print(isinstance(mgr1,Employee))
print(isinstance(mgr1,developer))
# issubclass() tells us if class is subclass of another
print(issubclass(Employee,developer))
print(issubclass(developer,Employee))
print(issubclass(manager,developer))

# SPECIAL METHODS/MAGIC METHODS
# allow us to emulate builtin behaviour within python and also have we implement operator overloading, for example
# so from special methods we could change some builtin behaviours and are always staring with __ 
# __init__ is a commanly use special method
#  repr is a special method which recreates the object
# print(emp) #without repr output, <__main__.Employee object at 0x000001850D448710
print(emp) #object is changed and whatever is printed inside repr has changed the object

print(emp.__repr__)
print(emp.__str__)
# str is redable and repr is unamiguous 
# str can be easy understood and is in string format while repr can be any datatype
print("Diffrence b/w str and repr")# example
import datetime
import pytz
a=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b=str(a)
print("str",str(a),str(b))
print("repr",repr(a),repr(b))

print(int.__add__(2,3)) #print(2+3)
print(str.__add__('a','b')) #print('a'+'b')
print('text'.__len__()) #len('text') 
# we makes changes into special methods to acces objects #basically to access special methods we need to call it while creating classes
# forexample additiion of the class could be change by making changes in __add__ method for class 
# there are many methods which could be chnage for example __sub__, __mul__, __divmod__, etc 
print(emp+empll) #access __add__()
print(len(emp)) #__len__()
 
# we use property decorator because it help us to update attritubes, delete it and set value without using instance of class
print(emp.fullnm) #acesses getter method
emp.fullnm = 'corery will'
print(emp.fullnm) #access setter method
del emp.fullnm #access deleter method 
print(emp.fullnm) 