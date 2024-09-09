#file object
f1=open('E:/VS studio/Python/to learn py/7File Handling/test.txt','r')
print(f1.name)
print(f1.mode)
f1.close()
print(f1.closed) #tells wheather file is closed or not

with open('E:/VS studio/Python/to learn py/7File Handling/test.txt','r') as f: 
  #know as context manager #allows us to access sile within our block # closes file automatically
  f_contents=f.read() #reads whole file #cursor value changes
  print(f_contents)
  f_contents1=f.readlines() #gives list with /n that is new line character #coursor values changes
  print(f_contents1)
  f_contents2=f.readline() #prints only the first line after cursor
  print(f_contents2,end='') #we use end='' because print statement already starts with new line 
  f_contents2=f.readline()
  print(f_contents2,end='')
  for line in f:
    print(line) #reads file #way2
  sizetoread=100
  f.read(sizetoread) #reads 100 characters of file and changes cursor to 100 character
  while len(f.read(10)) > 0:
    print(f.read,end='*') #after each 10 charcater *will be present 
    f.read(10) #once whole file is read it will showw empty string
    #hence the condition might be broken
    f.tell() #tells the current position of cursor 
    f.seek(0) #chances the position of file
#once file is read it goes to next cursor and then after whole execution, it becomes empty string/list
  with open('E:\VS studio\Python\to learn py\7File Handling\test1.txt','w') as f:
    f.write('test')
    f.write("test") #writes after the last cursor
    f.seek(0) 
    f.write('DW') #it will go to cursor 0 and then overwrite dw that is first 2 alphabets




  