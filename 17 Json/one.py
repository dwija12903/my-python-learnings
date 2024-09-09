# JSON - javascript object notation
# Data format for storing some information
# Used to- fetch data data from online APIs, configure files and diffrent kind to data stored in system
# independent of javascript was inspired from javascript

import json

people_string='''
{
  "people":
  [
    {
      "name": "John smith",
      "phone": "615-555-7146",
      "email": ["johnsmith@gmail.com","john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "email": null,
      "has_license": true
    }
  ]
}
'''

# to load python from string into json
data = json.loads(people_string)
print(data)
print(type(data))
print(type(data['people']))

# when we convert into json format python datatypes is converted into other form like
# json object is converted into dictionary
# array-->list
# string-->str
# null--> None ,...

# we dump from json to python
for person in data['people']:
  del person['phone']
new_string = json.dumps(data,indent=2,sort_keys=True) #indent is use for format,Sort_keys to sort keys alphabetically
print(new_string)

