import random
from random import randint
import sys
import pygame

#初始化pygame
pygame.init()
index = 0
#获取显示对象，自动匹配显示屏分辨率
pyInfo = pygame.display.Info()
width, height = pyInfo.current_w, pyInfo.current_h
#主窗口，也是Surface对象
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
#新建一个Surface对象 Surface类的参数flags：功能标志位，有两个可选参数值 HWSURFACE 和 SRCALPHA，
#前者代表将创建的 Surface 对象存放于显存中，后者表示让图像的每一个像素都包含一个alpha通道
bg_surface = pygame.Surface((width, height), pygame.SRCALPHA)
#以多少像素为一列
font_ps = 18
#字体对象
font = pygame.font.SysFont('fangsong', 20)
#为bg_surface填充颜色，不透明度15(为了实现代码雨逐渐消失的效果)
bg_surface.fill(pygame.Color(0, 0, 0, 15))
#主窗口为黑色
screen.fill((0, 0, 0))
#文本内容列表，元素都是渲染好的文本对象(本质是Surface对象)，其内容是0或1
texts = [font.render(str(i), True, (0, 255, 0)) for i in range(2)]
#计算有多少列代码雨
colums = int(width / font_ps)
#根据列数创建一个列表，元素初始值都为0
drops = [0 for i in range(colums)]
#主循环
while True:
    #事件检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
    #主动设置每次循环延迟50毫秒，不然代码雨速度太快
    pygame.time.delay(50)
    #在主窗口绘制bg_surface，因为bg_face比较透明，每次循环都覆盖一层bg_surface
    #这样就可以实现代码雨逐渐消失的效果
    screen.blit(bg_surface, (0, 0))
    for i in range(len(drops)):
        #从texts中任选一个元素
        text = random.choice(texts)
        #绘制text
        #横坐标i * font_ps，是font_ps的整数倍，这样可以确定绘制在哪一列(i=0就是第一列,i=2就是第二列,以此类推)
        #纵坐标drops[i] * font_ps，drops的元素的初始值都是零，所以从第一行开始
        screen.blit(text, (i * font_ps, drops[i] * font_ps))
        #每循环一次相应元素就加1，一套迭代下来drops所有元素都+1，下一套迭代代码雨就从下一行开始刷，行数逐渐推进
        drops[i] += 1
        #如果行数所在位置的纵坐标大于屏幕的高即超出了屏幕范围，就将其元素值归0，从第一行开始
        if drops[i] * font_ps > height * 2 or random.random() > 0.94:
            drops[i] = 0
    
    pygame.display.flip()
    