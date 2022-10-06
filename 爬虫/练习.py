import re
import requests
import re
from bs4 import BeautifulSoup
'''<div class="pic">
      <a class="nbg" href="https://book.douban.com/subject/1581309/" onclick="moreurl(this,{i:'0',query:'',subject_id:'1581309',from:'book_subject_search'})">
        <img class="" src="https://img9.doubanio.com/view/subject/s/public/s9788006.jpg" width="90">
      </a>
    </div>
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
}

url = 'https://book.douban.com/series/23602'
page_text = requests.get(url=url, headers=headers).text

def re_p():
    '''正则爬取'''
    index = 1
    ex = r'<div class="pic">[\s\S]*?src="(.*?)"[\s\S]*?</div>'
    r = re.compile(ex, re.M)
    for i in r.findall(page_text):
        image_data = requests.get(url=i, headers=headers).content
        with open('PNG\\%s.jpg'%index, 'wb') as fp:
            fp.write(image_data)
            print('%s.jpg,已保存'%index)
        index += 1
    print('Over!')

def bs4_p():
    '''bs4爬取'''
    index = 1
    soup = BeautifulSoup(page_text, 'lxml')
    list_img = soup.select('.nbg > img')
    for i in list_img:
        image_url = i['src']
        image_data = requests.get(url=str(image_url)).content
        with open('PNG\\%s.jpg'%index, 'wb') as fp:
            fp.write(image_data)
            print('%s.jpg,已保存'%index)
        index += 1
    print('Over!!')
