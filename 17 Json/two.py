# load method loads file and loads method for string, same goes for dump, dump for fjson file and dumps for string
import json
with open('E:/VS studio/Python/to learn py/17 Json/states.json') as f:
  data =  json.load(f)

for state in data['states']:
  print(state)
  print(state['name'],state['abbreviation'])

for state in data['states']:
  del state['area_codes']
with open('E:/VS studio/Python/to learn py/17 Json/new_states.json','w') as f:
  json.dump(data,f,indent=2)
  print("data dumped into file")
