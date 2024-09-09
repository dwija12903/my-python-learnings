try:
  pass
except Exception:
  pass
else: #runs code that needs to be executed when try block doesnot raise an exception
  pass
finally: #it runs no matter whatever happens, weather the code is successful or weather we through a exception
  pass
# we use try except blocks to avoid errros and detect errros inshort to manage errors
# example1
try:
  f=open('dwija.txt','r')
except Exception:
  print("Error detected")
# example2
try:
  f1=open('krishu.txt')
  # var= x
except FileNotFoundError as e:
  print(e)
  print("error detected in file")
except Exception as e: #tells us the exception
  print(e)  
# example3
try:
  a=4
except Exception as r:
  print('error has been detected')
  print(r)
else:
  a=4+3
  print(f'value of a is {a}')


