import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''管理飞船的类'''

    def __init__(self,screen,ai_settings):
        '''初始化飞船设置'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，并获取其外切矩形
        self.image = pygame.image.load(r'images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放到窗口底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 在center中储存小数值
        self.center = float(self.rect.centerx)
    
    def update(self):
        '''根据标志移动飞船'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
        
        self.rect.centerx = self.center


    def blitme(self):
        '''绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''将飞船放到屏幕底端中央'''
        self.center = self.screen_rect.centerx