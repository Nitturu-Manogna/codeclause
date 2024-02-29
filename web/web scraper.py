import requests
from bs4 import BeautifulSoup

req=requests.get("https://timesofindia.indiatimes.com")

soup=BeautifulSoup(req.content,"html.parser")

#get title of website
res=soup.title
print(res.get_text())

#get text inside website
print(soup.get_text())

#get html code
print(soup.prettify())

