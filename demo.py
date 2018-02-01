import requests
try:
    r=requests.get("https://python123.io/ws/demo.html")
    r.raise_for_status()
    demo=r.text
    print(demo)
except:
    print("error")