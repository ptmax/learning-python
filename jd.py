import requests
url="https://www.amazon.cn/dp/B072267FGT/ref=cngwdyfloorv2_recs_0"
kv={'user_agent':'Mozilla/5.0'}
try:
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("exception")
