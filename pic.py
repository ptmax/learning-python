import requests
import os
root="/path/"
url="http://v.youku.com/v_show/id_XMzMyMjYxODI1Ng==.html?spm=a2h0j.8191423.module_basic_relation.5~5!2~5~5!23~5~5~A"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        print(r.status_code)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("file saved")
    else:
        print("file already exists")
except:
    print("error")
