from bs4 import BeautifulSoup
import requests
try:
    r=requests.get("https://python123.io/ws/demo.html")
    r.encoding=r.apparent_encoding
    r.raise_for_status()
    demo=r.text
except:
    print("error")
soup = BeautifulSoup(demo, "html.parser")
tag = soup.a.attrs
print(tag)
href=tag['href']
print(href)