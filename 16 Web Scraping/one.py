#web scraping- prasing all the contents from website and pulling out only the information that you want
# request lib- used to fetch website
# we dont need parser till we have a good html code written
# there are diffrent types of parsers, xml parser, html5lib parser,etc

from bs4 import BeautifulSoup
# import requests
#example1: print out article website and summaries
with open('E:/VS studio/Python/to learn py/16Web Scraping/simple.html') as html_file:
  soup = BeautifulSoup(html_file,'lxml') #bs obj
print(soup) #all html content
print(soup.prettify()) #all html content with proper indentation

match = soup.title #to access title tag of html content
print(match)
match1 = soup.title.text #only text of title
print(match1)

match2 = soup.div #access first div tag 
print(match2)
match3 = soup.find('div',class_='footer') #to access particular div by class/id
print(match3)

article = soup.find('div',class_='article') #first div of class article
headline = article.h2.a.text
print(headline)
summary = article.p.text #access <p> tag
print(summary)

article1 = soup.find_all('div',class_='article') #instead of returing 1st tag it returns a list of matching arguments
for article in article1:
  headline = article.h2.text
  print("Headline= ",headline)
  summary = article.p.text
  print("Summary= ",summary)

# extracting url from pages
for link in soup.find_all('a'):
  print(link.get('href'))

# to extract all text from url
print(soup.get_text())