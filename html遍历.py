from bs4 import BeautifulSoup
import requests
try:
    r = requests.get("https://python123.io/ws/demo.html")
    r.encoding = r.apparent_encoding
    r.raise_for_status()
    demo = r.text
except:
    print("错误")
soup =BeautifulSoup(demo,"html.parser")
print(soup.prettify())
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)
print(len(soup.body.contents))
print(soup.body.contents[1])