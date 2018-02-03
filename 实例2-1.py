#jd.com
import requests
import re
import time

def getHTMLText(url):
    try:
        hd = {'user-agent': 'Chrome/10'}
        r=requests.get(url,timeout=5,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt=re.findall(r'<i>\d*\.\d*</i>',html)
        tlt=re.findall(r'<em>.*?<font class=\"skcolor_ljg\">',html)
        for i in range(len(plt)):
            price=plt[i].split('<i>')[1].split('</i>')[0]
            title=tlt[i].split('<em>')[1].split('<font class=\"skcolor_ljg\">')[0]
            if(title[0]!='A'):
                continue
            ilt.append([price,title])
    except:
        print("")


def printList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"),chr(12288))
    for i in range(len(ilt)):
        print(tplt.format(i+1,ilt[i][0],ilt[i][1]),chr(12288))

def main():
    url_start='https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&ev=exbrand_Apple%5E&page='
    depth=10
    inlt=[]
    for i in range(depth):
        try:
            url=url_start+str((i+1)*2)
            html=getHTMLText(url)
            time.sleep(5)
            print('爬取page'+(i+1))
            parsePage(inlt,html)
        except:
            continue
    printList(inlt)

main()