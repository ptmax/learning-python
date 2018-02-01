import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    demo=r.text
except:
    print("error")
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

