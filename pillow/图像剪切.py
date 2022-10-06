'''
图像剪切
'''
from PIL import Image
im = Image.open(r'pillow\image\向日葵.png')
box = 0, 0, 300, 200
print(im.size)
im_crop = im.crop(box)
im_crop.show()