import pygame
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
    '''显示游戏得分信息的类'''

    def __init__(self,ai_settings,screen,stars):
        '''初始化显示得分涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stars = stars

        # 显示得分信息时使用的字体设置
        self.text_color = (235,28,39)
        self.font = pygame.font.SysFont(None, 48)

        # 准备包含得分的图像
        self.prep_score(stars)
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self,stars):
        '''将得分信息渲染为图像'''
        score_str = format(stars.score,',')
        self.score_image = self.font.render('Score: '+score_str,True,self.text_color)
        self.score_rect = self.score_image.get_rect()

        # 将得分信息放在右上角
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        '''将最高得分渲染为图像'''
        high_score_star = format(self.stars.high_score,',')
        self.high_score_image = self.font.render('High score: '+high_score_star,True,self.text_color)

        # 将最高得分放在屏幕中央顶部
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        '''将等级渲染为图像'''
        self.level_image = self.font.render(('Level: '+str(self.stars.level)),
            True,self.text_color)

        # 将等级放在当前得分到达下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stars.ship_left):
            ship = Ship(self.screen,self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        '''绘制得分信息和最高得分信息'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)