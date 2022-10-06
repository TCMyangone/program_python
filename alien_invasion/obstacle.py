import pygame
class Obstacle():
    '''管理障碍物的类'''

    def __init__(self,screen,ai_settings,ship):
        '''初始化障碍物'''
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = self.screen.get_rect()
        self.obstacle_width = self.screen_rect.width / 5
        self.obstacle_height = 10
        

        # 创建一个障碍物并将其放到合适位置
        self.rect = pygame.Rect(0,0,self.obstacle_width,
            self.obstacle_height)
        self.rect.bottom = self.screen_rect.height - 2 * ship.rect.height - 20 
        self.rect.centerx = self.screen_rect.centerx

        self.color = 44,100,251

    def draw_obstacle(self):
        pygame.draw.rect(self.screen,self.color,self.rect)