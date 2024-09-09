# without generator
def square(nums):
  res=[]
  for i in nums:
    res.append(i*i)
  return res
num=square([1,2,3,4,5])
print(num)

# with generator
def Square(y):
  for i in y:
    yield i*i # creates generator
x=Square([1,2,3,4,5])
print(x) #they dont hold entire result into the memory it yields only one result so it has not calculated anything yet
print(next(x)) #now it yields first thing
print(next(x)) #each time we yield next we get next value
print(next(x))
print(next(x)) #when is list is executed fully and we use next method then it shows stop iteration error
# for num in x: #so to avoid stop iteration error
#   print(num)

# using list comprehension to create generator
z=[i*i for i in [1,2,3,4,5]] #list is created
print(z)
z1=(i*i for i in [1,2,3,4,5]) #generator
print(z1)
for i in z1: #to print way1
  print(i)
print(list(z1)) #way2

# generator saves the memory, it generators objects when they are executed,that is when needed
 
