# Context manager: allows us to properly manage resources so that we can specify what we can specify waht we want to setup
# if problems are not released then it will lead to resource leakage and may cause the system to either slow down or crash. It would be very helpful if users have a mechanism for the automatic setup and teardown of resources.
# Python provides an easy way to manage resources: Context Managers. The with keyword is used. When it gets evaluated it should result in an object that performs context management. Context managers can be written using classes or functions(with decorators).
# same as oops, we can change the object defination
# inmywords: open keyword of file object could be changed
# first way
class Open_file():
  def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
  def __enter__(self):
    self.file=open(self.filename,self.mode)
    return self.file
  def __exit__(self, exc_type, exc_val, traceback):
     self.file.close()
with Open_file('E:/VS studio/Python/to learn py/7 File Handling/sample.txt','w') as f:
  f.write('Dwija is studying in PDEU college')
print(f.closed)

from contextlib import contextmanager
@contextmanager #with context manager we can do whatever we want to do with the file 
def open_file(filee,mode):
   f = open(filee, mode)
   yield f
   f.close()
with open_file('E:/VS studio/Python/to learn py/7 File Handling/sample.txt','a') as f:
   f.write("\nHello dwija, How you doing?")
print(f.closed)