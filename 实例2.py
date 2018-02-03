#taobao.com
import requests
import re

def getHTMLText(url):
    hd={'user-agent':'Chrome/10'}
    try:
        r=requests.get(url,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"),chr(12288))
    for i in range(len(ilt)):
        print(tplt.format(i+1,ilt[i][0],ilt[i][1]),chr(12288))

def main():
    goods='手机'
    depth=3
    start_url='https://s.taobao.com/search?q='
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+goods+'&s='+str(i*44)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)

main()
