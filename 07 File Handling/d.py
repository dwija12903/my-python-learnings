#csv files- comma seperated values
import csv
with open('E:/VS studio/Python/to learn py/7File Handling/names.csv','r') as f:
  reader=csv.reader(f)
  print(reader) #just a object in memory
  with open('E:/VS studio/Python/to learn py/7File Handling/names1.csv','w') as wf:
    writer=csv.writer(wf,delimiter='-') #delimiter means value will be seperated by - #delimetrs are /t
    next(reader) #skips the first and starts from 2nd
    for line in reader: 
      print(line) #print each line in list form
      print(line[2]) #prints email
      writer.writerow(line) #writes each list element means whole row

#to write using dictionaries
with open('E:/VS studio/Python/to learn py/7File Handling/names.csv','r') as f:
  reader=csv.DictReader(f)
  for line in reader:
    print(line) #not a proper way 
    print(line['email'])

with open('E:/VS studio/Python/to learn py/7File Handling/names.csv','r') as f:
  reader=csv.DictReader(f)
  with open('E:/VS studio/Python/to learn py/7File Handling/names1.csv','w') as wf:
    fieldnames=['first_name','last_name','email']
    writer=csv.DictWriter(wf,fieldnames=fieldnames,delimiter='\t')
    writer.writeheader() #writes the fieldnames as firstline 
    for line in reader:
      #del line['email'] #this doesnot write the email elemnet and deleted it
      writer.writerow(line)


  


