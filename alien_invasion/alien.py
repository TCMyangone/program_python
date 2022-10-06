import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,ai_settings,screen):
        '''初始化外星人设置'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像,并设置rect属性
        self.image = pygame.image.load(r'images\aline_ship.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附件
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人的小数值位置
        self.x = float(self.rect.x)


    def blitme(self):
        '''绘制外星人'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''向右移动外星人'''
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        '''检测外星人是否处于边缘，如果是就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        

