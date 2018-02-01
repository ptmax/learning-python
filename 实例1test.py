import requests
from bs4 import BeautifulSoup
import bs4

url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
try:
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("错误")

soup=BeautifulSoup(r.text,"html.parser")
for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
        tds = tr.find_all('td')
        print(tds[1])
        print(tds[3])
