import requests
url="http://www.ip138.com/ips138.asp?ip="

try:
    r=requests.get(url+'000.000.000.000')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[7200:7400])
except:
    print("error")
