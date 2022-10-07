from PIL import Image, ImageFont, ImageDraw
import numpy as np
def ascii_art(file):
    '''生成ASCII字符图片'''
    
    # 打开图片
    im = Image.open(file)
    # 缩小比例
    sample_rate = 0.05
    #字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', size=10)
    #字体的宽高比
    width_height = font.getbbox('x')[2] / font.getbbox('x')[3]
    # 设定新的尺寸，不然太大，工作量也变大，低配电脑容易死机
    # 宽*缩小比例，高*缩小比例*字体的宽高比(不乘以宽高比，生成的图像会被拉长)
    new_im_size = int(im.size[0] * sample_rate), int(im.size[1] * sample_rate * width_height)
    im = im.resize(new_im_size)
    # 将重设尺寸的图片转换为numpy数组，里面存有其颜色信息(RGB,RGBA,L等),通常是RGB，RGBA的三维数组
    im_color = np.array(im)
    # 将重设尺寸后的图片转换为灰度图，在图片转换为ASCII字符时不需要颜色信息，只需要其灰度信息(值越大越白，越小越黑)，并转换成对应的ASCII字符
    im = im.convert('L')
    # 将灰度图转换成numpy数组
    im = np.array(im)
    # 待转换的ASCII字符数组，由暗到明的排列(看字符像素占比，越高越亮，反之同理)
    symbols = np.array(list(r'=ua@'))
    '''
    基本算法:
    将灰度图数组里的值的范围(最小值到最大值)分成几个亮度梯度,梯度数根据ASCII字符数量定,有几个就分成几个梯度(灰度值是从最小值开始的,而不是0,所以下面的公式要减im.min())
    计算每个梯度的数值或范围,用数组的值除以这个数值得到所属梯度(也可以说是ASCII字符数组的索引,要转换成整数)
    最后给ASCII字符数组传递梯度索索引,就将原来灰度图数组里的值全部替换成对应梯度的ASCII字符.
    可以直接打印在控制台,也可以保存为图片
    '''
    levels = (im.max() - im.min()) / (symbols.size - 1)
    im = ((im - im.min()) / levels).astype(int)
    ascii = symbols[im]

    # 这里用图片输出字符图片，所以要创建一个图像做背景
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
    im_out.save(path)
    print('Over!')

ascii_art(path)
