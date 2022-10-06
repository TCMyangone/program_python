import pygame
import sys
from random import randint
pygame.init()
clock = pygame.time.Clock()
FPS = 30
tf = True
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 32, 123))
screenRect = screen.get_rect()

sur = pygame.Surface((10, 10), pygame.HWSURFACE)
sur.fill('pink')
surRect = sur.get_rect()

pygame.display.set_caption('测试')

f = pygame.font.Font(r'C:\Windows\Fonts\simsun.ttc', 50)

text = f.render('你好', True, (255, 255, 255))
textRect = text.get_rect()
screen.blit(text, textRect)

ship_image = pygame.image.load(r'D:\program_python\alien_invasion\images\ship.bmp')
shipRect = ship_image.get_rect()
shipRect.center = screenRect.center


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipRect.x -= 5
            if event.key == pygame.K_RIGHT:
                shipRect.x += 5
            if event.key == pygame.K_UP:
                shipRect.y -= 5
            if event.key == pygame.K_DOWN:
                shipRect.y += 5
            if event.key == pygame.K_SPACE:
                surRect.y -= 10
                tf = False
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sur.fill((r, g, b))
    screen.fill((0, 32, 123))
    screen.blit(ship_image, shipRect)
    if tf:
        surRect.x, surRect.y = shipRect.x, shipRect.y
    screen.blit(sur, surRect)
    pygame.display.flip()