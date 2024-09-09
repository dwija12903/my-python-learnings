#NAMED TUPLES- lightweight object works like tuple but more readable 
colors=(55,155,255) #normal tuple
print(colors[0]) #excecution
# we used namedtuples instaed of dictionaries beacuse tuples are immutable, means cant change value, and dictionary requries more colors, it gives redability and functionality
from collections import namedtuple
Color=namedtuple('Color',['red','green','blue'])
color=Color(55,155,255)
print(color.red)
white=Color(255,255,255)
print(white.blue)