'''
将ASCII字符图片打印在终端,代码里的"path"自己替换,颜色可更改
'''
from PIL import Image, ImageFont
import numpy as np
import os
'''
os.path.abspath(path)	返回绝对路径
os.path.dirname(path)	返回文件路径
切换工作目录到当前文件所在目录,因为程序读取用的是相对路径,所以命令窗口的工作目录不在文件所在目录就会报错
'''
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def ascii_art(file):
    '''终端打印ASCII字符图片'''
    
    # 打开图片
    im = Image.open(file)
    # 缩小比例
    sample_rate = 0.08
    #字体对象
    font = ImageFont.truetype(path, size=10)
    #字体的宽高比
    width_height = font.getbbox('x')[2] / font.getbbox('x')[3]
    # 设定新的尺寸，不然太大，工作量也变大，低配电脑容易死机
    # 宽*缩小比例，高*缩小比例*字体的宽高比(不乘以宽高比，生成的图像会被拉长)
    new_im_size = int(im.size[0] * sample_rate), int(im.size[1] * sample_rate * width_height)
    im = im.resize(new_im_size)
    # 将重设尺寸后的图片转换为灰度图，在图片转换为ASCII字符时不需要颜色信息，只需要其灰度信息(值越大越白，越小越黑)，并转换成对应的ASCII字符
    im = im.convert('L')
    # 将灰度图转换成numpy数组
    im = np.array(im)
    # 待转换的ASCII字符数组，由暗到明的排列(看字符像素占比，越高越亮，反之同理)
    symbols = np.array(list(r'.-=ua@'))
    '''
    基本算法:
    将灰度图数组里的值的范围(最小值到最大值)分成几个亮度梯度,梯度数根据ASCII字符数量定,有几个就分成几个梯度(灰度值是从最小值开始的,而不是0,所以下面的公式要减im.min())
    计算每个梯度的数值或范围,用数组的值除以这个数值得到所属梯度(也可以说是ASCII字符数组的索引,要转换成整数)
    最后给ASCII字符数组传递梯度索索引,就将原来灰度图数组里的值全部替换成对应梯度的ASCII字符.
    可以直接打印在控制台,也可以保存为图片
    '''
    levels = (im.max() - im.min()) / symbols.size
    im = ((im - im.min()) / levels).astype(int)
    for i in im:
        for j ,k in enumerate(i):
            if i[j] == symbols.size:
                i[j] -= 1

    ascii = symbols[im]
    lines = '\n'.join(''.join(a) for a in ascii)
    print(lines)
    _ = input('')

ascii_art(path)
