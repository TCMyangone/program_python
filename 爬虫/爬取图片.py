import requests
import re

page = '/page/2'
url = r'https://www.biacgn.com/archives/tag/%e7%94%b5%e8%84%91%e5%a3%81%e7%ba%b8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
}
r = re.compile(r'<a  href=\"https://www\.biacgn\.com/archives/.*src="(.*?)".*</a>', re.M)
index = 0
for j in range(1, 20):
    page = '/page/%s'%j
    if j == 1:
        page_text = requests.get(url=url, headers=headers).text
    else:
        new_url = url + page
        page_text = requests.get(url=new_url, headers=headers).text

    for i in r.findall(page_text):
        image_data = requests.get(url=i).content
        with open('PNG\\'+str(index)+'.jpg', 'wb') as fp:
            fp.write(image_data)
        index += 1

print('Over!')
