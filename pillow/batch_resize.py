'''
批量修改图片尺寸
'''
from PIL import Image
import os
path = r'C:\Users\TcidCratman\Documents\ShareX\Screenshots\2022-10\\'
#列出当前目录下的所有文件名，返回一个list对象
fileName = os.listdir(path)
size = 350, 350
#os.path.exists判断path对应文件或目录是否存在，返回True或False
if not os.path.exists(r'pillow\ImageNew\\'):
    os.mkdir(r'pillow\ImageNew')
for img in fileName:
    old = Image.open(path+img)
    new = old.resize(size)
    new.save(r'pillow\ImageNew\\'+img)
    print(img + '已处理完成')
