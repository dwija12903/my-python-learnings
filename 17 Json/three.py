# fetches data from APIs
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read() #reads the content

# converts into json string
data = json.loads(source)

# converts into python string with proper indentation
print(json.dumps(data, indent=2))