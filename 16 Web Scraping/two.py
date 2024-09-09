# to extract from website/url
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.zillow.com/').text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())

match = soup.find('article') #finds that tag
print(match.prettify())

csv_file = open('cms_scraper.csv','w')
writer = csv.writer(csv_file)
writer.writerow(['headline','summary','links'])

headline=match.h2.a.text
summary = match.find('div',class_='enerty') #finds within article tag
print(summary.p.text)

video_src= match.find('iframe',class_='youtube-player')['src']
print(video_src) #gives the whole tag
# to acess any attribute inside a tag write in dictionary
video_id = video_src.split('/')[4]#splits value in list based ont he character i specified #[] is the index to access
video_id = video_id.split('?')[0]

writer.writerow(headline,summary,video_id)
csv_file.close()