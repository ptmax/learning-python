import requests
kv = {'wd':'Python'}
url="http://www.baidu.com"
try:
    r=requests.get(url,params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("error")
