import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=5)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "exception"

if __name__=="__main__":
    while(True):
        url="http://www.xxx.cn"
        print(getHTMLText(url))
