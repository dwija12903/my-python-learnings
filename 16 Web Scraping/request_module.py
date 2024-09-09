# request module is use to extract http information from websites
# it is good for getting info. but not good for parsing info.
# for parsing we use beautiful soups
import requests
r = requests.get('https://xkcd.com/353/')

print(dir(r)) # tells attributes and methods taht we can accces from r
# print(help(r)) 

# executes whole html script of given url 
print(r.text)

# to get the image
r1 = requests.get('https://imgs.xkcd.com/comics/python.png')
r1.text #gives us the bytes of image file
with open('comic.png','wb') as f:
    f.write(r1.content)

print(r1.status_code) #200 is success, 300 redirects, 400 client errors, 500 server errors
print(r1.ok) #if status code<400, then true
print(r1.headers)#gives all the headers

payload = {'page': 2, 'count': 25}
r2 = requests.get('https://httpbin.org/get',params=payload)
print(r2.text)
print(r2.url)

payload1 = {'username': 'dwija','password':'test'} 
r3 = requests.post('https://httpbin.org/post',params=payload1)
print(r3.json()) #creates python dictionary from json data