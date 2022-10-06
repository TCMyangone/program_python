import sys, pygame
from pygame.constants import FULLSCREEN
from bullet import Bullet
from alien import Alien
from time import sleep


# ============================================================================================================
def check_events(ship, ai_settings, bullets, screen, stars, play_button, aliens, sb, alien_bullets):
    """处理键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, ship, event, screen, bullets, aliens, alien_bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stars, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, sb,
                              alien_bullets)


# noinspection SpellCheckingInspection
def check_keydown_events(ai_settings, ship, event, screen, bullets, aliens, alien_bullets):
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 飞船向左移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，将其添加到编组中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_f:
        screen = pygame.display.set_mode((ai_settings.screen_width,
                                          ai_settings.screen_height), FULLSCREEN, 32)
    elif event.key == pygame.K_g:
        screen = pygame.display.set_mode((ai_settings.screen_width,
                                          ai_settings.screen_height), 0, 32)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 停止飞船向右移动
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 飞船停止向左移动
        ship.moving_left = False


# ============================================================================================================
def ship_hit(ai_settings, stars, screen, ship, aliens, bullets, sb, alien_bullets):
    """响应被外星人撞到的飞船"""
    if stars.ship_left > 0:
        # 将ship生命值-1
        stars.ship_left -= 1
        sb.prep_ships()
        # 清空外星人编组和子弹编组
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        # 创建一行新的外星人，并将飞船放在屏幕底端中央
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        ai_settings.ship_hit = False
        # 暂停
        sleep(0.5)
    else:
        stars.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stars, sb):
    """检查是否诞生了新的最高分"""
    if stars.score > stars.high_score:
        with open('high_score.txt', 'w') as fl:
            fl.write(str(stars.score))
        stars.high_score = stars.score
        sb.prep_high_score()


# ============================================================================================================

def check_play_button(stars, play_button, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, sb,
                      alien_bullets):
    """在玩家单击play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stars.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stars.reset_stars()
        stars.game_active = True
        # 重置游戏动态设置
        ai_settings.initialize_dynamic_settings()

        # 重置记分牌图像
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_score(stars)
        sb.prep_ships()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


def play_button_jh(play_button):
    """如果鼠标在play按钮上，将会与按钮交互"""
    m_x, m_y = pygame.mouse.get_pos()
    if play_button.rect.collidepoint(m_x, m_y):
        play_button.rect.width, play_button.rect.height = 205, 55
        play_button.rect.center = play_button.screen_rect.center
    if not play_button.rect.collidepoint(m_x, m_y):
        play_button.rect.width, play_button.rect.height = 200, 50
        play_button.rect.center = play_button.screen_rect.center


# ============================================================================================================

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没达到限制，就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def wear_bullets_alien(aliens, AilenBullet, alien_bullets, ai_settings, screen):
    """为每个外星人装上子弹"""
    for alien in aliens.sprites():
        new_alien_bullets = AilenBullet(ai_settings, screen)
        new_alien_bullets.rect.centerx = alien.rect.centerx
        new_alien_bullets.rect.bottom = alien.rect.bottom
        alien_bullets.add(new_alien_bullets)


def alien_bullets_y(alien_bullets, screen):
    """向下自动外星人子弹"""
    alien_bullets.update()
    screen_rect = screen.get_rect()
    for bullet in alien_bullets.copy():
        if bullet.rect.bottom >= screen_rect.bottom:
            alien_bullets.remove(bullet)


def fire(aliens, AilenBullet, alien_bullets, ai_settings, screen, alien):
    """控制外星人发射子弹"""
    now = pygame.time.get_ticks()
    now_1 = pygame.time.get_ticks()
    # 储存时间余数
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 冷却7秒后就发射子弹 
    if now % 7000 in time:
        # 若7秒后，就停止外星人移动，并让其发射子弹
        wear_bullets_alien(aliens, AilenBullet, alien_bullets, ai_settings, screen)


# ============================================================================================================
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其加入到当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    '''创建一个外星人，并计算每行可容纳多少人'''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_numbers_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_numbers_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - 3 * alien_height - 2 * ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时就采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人整体下移,并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens, ship, stars, screen, bullets, sb, alien, alien_bullets):
    """检测是否有外星人处于屏幕边缘，并更新整群外星人的位置"""
    aliens.update()
    check_fleet_edges(ai_settings, aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stars, screen, ship, aliens, bullets, sb, alien_bullets)
    # 检查是否有外星人到达屏幕底部
    check_aliens_bottom(ai_settings, stars, screen, ship, aliens, bullets, sb, alien_bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stars, sb):
    '''响应子弹和外星人的碰撞'''
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions.values():
            stars.score += ai_settings.alien_points * len(alien)
            sb.prep_score(stars)
        check_high_score(stars, sb)
    if len(aliens) == 0:
        # 删除现有子弹并创建一群新外星人,加快游戏节奏
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stars.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, aliens, ship)


def check_aliens_bottom(ai_settings, stars, screen, ship, aliens, bullets, sb, alien_bullets):
    '''检测是否有外星人到达屏幕底部'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞倒一样处理
            ship_hit(ai_settings, stars, screen, ship, aliens, bullets, sb, alien_bullets)
            sleep(0.5)
            break


# ============================================================================================================
def check_bullet_obstacle_collisions(obs, bullets, alien_bullets):
    '''检测玩家子弹和外星人子弹与障碍物的碰撞'''
    collisions = pygame.sprite.spritecollide(obs, bullets, True)
    collisions_alien = pygame.sprite.spritecollide(obs, alien_bullets, True)


def check_alien_bullet_collisions(ship, alien_bullets, ai_settings, stars, screen, aliens, bullets, sb):
    '''检测外星人子弹与玩家飞船的碰撞'''
    collide = pygame.sprite.spritecollide(ship, alien_bullets, False)
    if collide:
        ship_hit(ai_settings, stars, screen, ship, aliens, bullets, sb, alien_bullets)


def update_bullets(bullets, aliens, ai_settings, screen, ship, stars, sb):
    # 更新子弹位置
    # 删除已消失的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stars, sb)


# ============================================================================================================
def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stars, sb, obs, alien_bullets):
    '''更新屏幕'''
    # 填充屏幕颜色
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    if stars.game_active:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
    # 绘制外星人子弹
    for bullet in alien_bullets.sprites():
        bullet.draw()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 绘制障碍物
    obs.draw_obstacle()
    # 绘制记分牌
    sb.show_score()
    # 如果游戏处于非活动状态就绘制play按钮
    if not stars.game_active:
        play_button.draw_button()
    # 与play按钮交互
    play_button_jh(play_button)
    # 不断更新屏幕内容
    pygame.display.flip()
