import pygame
from pygame.sprite import Sprite

class AilenBullet(Sprite):
    '''对子弹管理的类'''
     
    def __init__(self,ai_settings,screen):
        '''初始化外星人子弹'''
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置到正确位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

        self.color = ai_settings.bullet_color

    def update(self):
        '''向下移动子弹'''
        self.rect.y += 3

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)