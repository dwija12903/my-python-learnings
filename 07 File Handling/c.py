#task to rename multiple files
import os 
os.chdir("C:\Users\Dwija\Pictures\Screenshots")
print(os.getcwd())
#print all the files in this directory
for f in os.lisdir():
  print(f)
  filename,fileext=os.path.splitetext(f) #seperates the extension and the rest in to diffrent tuple elements
  print(filename) #gives file name without extention
  title,course,num=filename.split('-') #splits the string into list elemnt whenever - occurs 
  print(course)
  title=title.strip() #removes all the leading whitespaces/ blankspaces 
  course=course.strip()
  new_name='{}-{}-{}'.format(num,course,fileext)
  os.rename(f,new_name)

  




