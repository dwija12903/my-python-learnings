#STRINGS
message="bobby's pin" #use "" beacuse when we want to apply '
message1='''dwija hello how 
are you i am fine.''' #used for mutiple lines
s="Hello World"
print(s) #prints the string
print(s[3]) #prints the element at index 3
print(s[2:5]) #slicing if string start element is inclusive but stop element is not included in the list
print(s.lower()) #converts into lower
print(s.upper()) #to upper
print(s.count("l")) # counts total no of 'l'
new_s=s.replace('World','dwija') #replace the words
print(new_s)
#ways to print variables
print(s+""+new_s+" heyyyy")
print('{} ABC , {}'.format(s,new_s))
print(f'{s},{new_s} heyyyy') #using f strings
print(f'calculation of 4*4 is {4*4}')
print(dir(s)) #tells methods availabe for s

#INTERGERS AND FLOAT
num=3.43
print(type(num)) #tells the type, int or float
print(3//2) #floor divison without decimal
print(3/2) #division with decimal
print(abs(-3)) #gives absolute value 
print(round(3.75,1)) #rounds up the value upto deciMAL 1

#LISTS
courses=['history','math','phy','cs']
len(courses) #tells length of list
print(courses)
print(courses[3]) #to access values
print(courses[2:4]) #silcing 
print(courses[-1]) #we use -1 to access the last index,no need to know length
print()
courses.append("chem") #to append at last
courses.insert(1,"eng") #appends at the given index
courses.extend(["deco",'cn']) #appends multiple elements
courses.remove("deco") #removes the given element
popped=courses.pop() #pops the last element
print('poppend el',popped)
courses.reverse() #gives rerverse list
courses.sort() #arrrange in asc
courses.sort(reverse=True) #to arrange in desc
courses.index("chem") #tells the index
sorted_courses=sorted(courses) #.sort() changes the list elements, we use sortted() function so elements are not changed from original list  
for index,courses in enumerate(courses): #to access index and value
  print(index,courses)
listtostring= "".join(courses) #converts the list into string seperated by ""
print('-'.join(courses)) #converts courses into string seperated by -
convertedlist= listtostring.split(" ") #converts string to list when "" occurs
print(convertedlist)
num=[4,2,7,5,9]
min(num)
max(num)
sum(num)
#list are mutable they change by themselves, if 2 list are evaluated same then after changing values both the list value changes
l1=[1,2,3,4,5]
l2=l1
print(f"list one {l1} list two {l2}")
l1[2]=10
print(f"After changing values: {l1} {l2}") #value is automatically updated in l2

#TUPLES- immutable,ordered
t=tuple() #used to create tuple
t1=(2,3,4,)

#List and tuple both is collection of data
#list has [] and tuple is () with optional parthenthesis
#list mutable, tuple immutable
#list takes more memory than tuple objects
#list slow execution and tuple fast
#list less efficient then tuple
#list follows packing and tuple packing and unpacking both

#SETS- unordered,removes duplicate values
set1={'dwija','krishu','mummy','pappa'}
print(set1) #prints different order everytime during execution
set2={'bharat','pinky','mummy','pappa'} 
set1.intersection(set2) #gives intersection
set1.difference(set2) #gives diffrenece
set1.union(set2) #gives combine list of both

#DICTIONARIES
d={'name':'dwija','age':20,'gender':'female','courses':['chem','phy']}
print(d['age']) #to access elemnts
print(d.get("phone no","not present in dict")) #get method returns the value of the key, and if key is not present returns None.....next strings prints when the key is not found
print(d.get('gender','data not found'))
d.update({'name':'dwi','age':21}) #updates the value
del d['gender'] #to delete the key
age= d.pop('age')
print(age,"age key is deleted")
len(d) #tells the length of dictionary
d.keys() #returns all key #dict_keys{['name','age']}
d.values() #dict_values{['dwi',21]} 
d.items() # allows to access key value pair in list, basically converts into the list
for key in d: #gives only key
  print(key)
for key,value in d.items(): #gives key value both
  print(key,value)

#CONDITIONAL STATEMENTS- if else elif 
user='admin'
log=True
#can used not,and or with if
#and- one false then fale, or one true then true, not ma opposite
# None,0,[],(),{},'' evalutes to False

#LOOPs-for while
nums=[1,2,3,4,5]
for num in nums:
  print(num)
  if num==3:
    break #breaks the loop and does not run head of this
for num in nums:
  if num==3:
    print("found")
    continue #willnot print 3
  print(num)
x=0
while True:  #create infinite loop
  if x==4: #creates endpoint for loop
    break
  x+=1
  print(x) #numbers till 3 will be printed