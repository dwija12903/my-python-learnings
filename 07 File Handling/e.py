#use csv to prase csv file,count the contributers and put their names into html unordered list to drop into website
import csv
htmloutput=''
names=[]
with open('E:/VS studio/Python/to learn py/7File Handling/pateron.csv','r') as datafile:
  reader=csv.reader(datafile)
  #print(reader) #object which iterables
  #print(list(reader)) #prints the data in form of list
  next(reader) #skip 1st line
  next(reader) #skips 2nd line
  for line in reader:
    if line[0]=='No Reward':
      break #after this line next lines will not be printed
    print(reader)
    names.append(f"{line[0]} {line[1]}")

htmloutput += f'<p> There is currently {len(names)} public contributors. Thankyou! </p>'
htmloutput += '/n<ul>'
for name in names:
  htmloutput += f'/n/t<li> {names} </li>'
htmloutput += '/n </ul>'
print(htmloutput)
