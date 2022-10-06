from PIL import Image, ImageFont, ImageDraw
import numpy as np
import math
def ascii_art(file):
    B = 0.5
    c = 0
    k = math.tan((45 + 44 * c) / 180 * 3.1415926)
    
    im = Image.open(file)
    # 缩小比例
    sample_rate = 0.05
    font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', size=150)
    width_height = font.getbbox('x')[2] / font.getbbox('x')[3]
    # 设定新的尺寸
    new_im_size = int(im.size[0] * sample_rate), int(im.size[1] * sample_rate * width_height)
    im = im.resize(new_im_size)
    im_color = np.array(im)

    im = im.convert('L')
    im = np.array(im)
    
    symbols = np.array(list(r'=ua@'))
    im = ((im - im.min()) / (im.max() - im.min()) * (symbols.size - 1))
    ascii = symbols[im.astype(int)]
    letter_size = font.getbbox('x')
    im_out_size_width = new_im_size[0] * letter_size[2]
    im_out_size_height = new_im_size[1] * letter_size[-1]
    im_out_size = im_out_size_width, im_out_size_height
    bg_color = 'black'
    im_out = Image.new('RGB', tuple(im_out_size), bg_color)
    draw = ImageDraw.Draw(im_out)
    y = 0
    for i, line in enumerate(ascii):
        for j, ch in enumerate(line):
            color = tuple(im_color[i, j])
            draw.text((letter_size[2] * j, y), ch, fill=color, font=font)
            
        y += letter_size[-1]
    im_out.save(r'D:\program_python\\'+'asci.jpg')
    print('Over!')
    # lines = '\n'.join((''.join(r) for r in ascii))
    # print(lines)
    # _ = input('')
ascii_art(r'pillow\image\大伯.jpg')
