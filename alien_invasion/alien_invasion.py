from scoreboard import Scoreboard
import os
import pygame
from pygame.constants import FULLSCREEN
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stars import GameStars
from button import Button
from obstacle import Obstacle
from alien_bullets import AilenBullet
from alien import Alien
import os

'''
os.path.abspath(path)	返回绝对路径
os.path.dirname(path)	返回文件路径
切换工作目录到当前文件所在目录,因为程序读取用的是相对路径,所以命令窗口的工作目录不在文件所在目录就会报错
'''
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # 屏幕居中显示
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), FULLSCREEN, 32)

    pygame.display.set_caption('外星入侵')

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    # 创建一个储存子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)
    # 创建一个用于统计游戏信息的实例
    stars = GameStars(ai_settings)
    # 创建一个play按钮
    play_button = Button(screen, ai_settings, 'Play')
    # 创建一个记分牌
    sb = Scoreboard(ai_settings, screen, stars)
    # 创建一个障碍物
    obs = Obstacle(screen, ai_settings, ship)
    # 创建一个储存外星人子弹的编组
    alien_bullets = Group()
    alien = Alien(ai_settings, screen)

    # 游戏的主循环
    while True:
        # 响应键盘和鼠标事件
        gf.check_events(ship, ai_settings, bullets, screen, stars, play_button, aliens, sb, alien_bullets)
        # 如果游戏处于活动状态才运行以下内容
        if stars.game_active:
            # 移动飞船
            ship.update()
            # 更新子弹位置并删除已消失子弹 
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, stars, sb)
            # 冷却过后，为外星人装上子弹
            gf.fire(aliens, AilenBullet, alien_bullets, ai_settings, screen, alien)
            # 更新外星人子弹位置并删除已消失子弹 
            gf.alien_bullets_y(alien_bullets, screen)
            # 检测是否有外星人处于屏幕边缘，并更新整群外星人的位置
            gf.update_aliens(ai_settings, aliens, ship, stars, screen, bullets, sb, alien, alien_bullets)
            # 检测玩家子弹和外星人子弹与障碍物的碰撞
            gf.check_bullet_obstacle_collisions(obs, bullets, alien_bullets)
            # 检测外星人子弹与玩家飞船的碰撞
            gf.check_alien_bullet_collisions(ship, alien_bullets, ai_settings, stars, screen, aliens, bullets, sb)
        # 更新屏幕内容
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stars, sb, obs, alien_bullets)


run_game()
_ = input('sda')