import requests
name = input('请输入:')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
param = {
    'query': name
}
url = 'https://www.sogou.com/web'
response = requests.get(url, param, headers=headers)
page_text = response.text
with open(name+'.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('爬取成功')