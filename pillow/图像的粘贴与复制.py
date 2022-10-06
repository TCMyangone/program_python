from PIL import Image
im = Image.open(r'pillow\image\向日葵.png')
im_new = Image.new('L', (200, 100), 100)
im_copy = im.copy()
im_crop = im_copy.crop((0, 0, 200, 200))
im_copy.paste(im_crop, (100, 100, 300, 200), im_new)
im_copy.show()