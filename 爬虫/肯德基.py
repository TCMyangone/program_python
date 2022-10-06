from email import header
import requests


import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': 1,
    'pageSize': 10,
    'op': 'keyword',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
response = requests.post(url=url, data=data, headers=headers)
print(response.text)