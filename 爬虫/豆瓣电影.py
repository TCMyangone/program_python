import requests


import requests
url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}
params = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

response = requests.get(url=url, params=params, headers=headers)
_ = response.json()
print(_)