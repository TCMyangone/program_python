from PIL import Image
im_1 = Image.open(r'pillow\image\fly.png')
im_2 = Image.open(r'pillow\image\向日葵.png')
#让蝴蝶图像尺寸和向日葵图像尺寸保持一致,返回了一个新的Image对象
im = im_1.resize(im_2.size)
#blend()只用于RGBA模式的图片，即有alpha通道的图片
im_3 = Image.blend(im, im_2, 0.7)
im_3.show()