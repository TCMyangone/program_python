import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''对子弹管理的类'''
     
    def __init__(self,ai_settings,screen,ship):

        
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置到正确位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed
    
    def update(self):
        '''向上发射子弹'''
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
