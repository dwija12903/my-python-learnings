#lamba argumentlist : expression
#LAMBA FUNCTIONS
#functions without name, also know as anonymous functions
#we can provide multiple arguments in lambda functions, no need to write return, it return automatically  
#we cant use condition statement in exprssion 

add= lambda a:a+10 #value is automatically returned to assigned function variable
#variables after lambda are the arguments 
print(add(5)) #value of argument for function
print(add) 

result=lambda a,b: (a*b,a/b)
m,d= result(10,2)
print("multiplication is ",m,"division is",d)

#filter
#filter(function,iterable->to be evaluted in function)
#only single argument is taken
num=[3,2,44,32,43]
lst=[45,32,21,67,88]
flt=filter(lambda x: x%2==0,num) #once excecuted, the after second execution will give blank list []
print(list(flt))
flt1=filter(lambda x: x>60,lst)
print(list(flt1))

#map
#map(function,iterable1,iterable2)
#function for which 2 arguments are needed takes 2 arguments from 2 diffrent iterables
#when equal number of elements are not present in 2 iterables then last elemets are neglected
a=map(lambda a,b:a+b,num,lst) #for mutiple iterables
print(list(a))
b=map(lambda x:x+10,num) #for single interable same as filter
print(list(b))

#reduce
#reduce(function,iterable)
#2 arguments are taken from same iterable but returns single value
import functools
c=functools.reduce(lambda x,y: x*y,num)
print("reduced value is",c)

#so basicallly 
#filter when only one input arg
#map when 2 input arg
#reduce when with 2 input arg continues evalution with single value output