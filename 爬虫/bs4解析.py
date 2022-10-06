
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
}
url = 'https://so.gushiwen.cn/guwen/book_46653FD803893E4F7F702BCF1F7CCE17.aspx'
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
list_span = soup.select('.bookcont > ul > span > a')

for i in list_span:
    content_url = str(i['href'])
    content_text = requests.get(url=content_url, headers=headers).text
    new_soup = BeautifulSoup(content_text, 'lxml')
    content = new_soup.find('div', class_='contson').text
    with open('三国演义\\%s.txt'%i.string, 'w', encoding='utf-8') as fp:
        fp.write(content)

print('Over!!')