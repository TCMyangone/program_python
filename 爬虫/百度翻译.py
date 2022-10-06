import requests
import json
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
name = input('请输入: ')
data = {
    'kw': name
}

response = requests.post(url=url, data=data, headers=headers)
dict = response.json()
with open(name+'.json', 'w', encoding='utf-8') as fp:
    json.dump(obj=dict, fp=fp, ensure_ascii=False)
    
print('Over!')