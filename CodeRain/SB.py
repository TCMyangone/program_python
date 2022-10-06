import random
import sys
import pygame
pygame.init()
pyInfo = pygame.display.Info()
width, height = pyInfo.current_w, pyInfo.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('傻逼')
bg_surface = pygame.Surface((width, height), pygame.SRCALPHA)
letter = ['傻逼', '傻', '大傻逼', '逼']
font_ps = 40
font = pygame.font.SysFont('fangsong', 20)
bg_surface.fill(pygame.Color(0, 0, 0, 15))
screen.fill((0, 0, 0))
texts = [font.render(str(i), True, (248, 216, 12)) for i in letter]
colums = int(width / font_ps)
drops = [0 for i in range(colums)]

while True:
    pygame.time.delay(50)
    screen.blit(bg_surface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)
        screen.blit(text, (i * font_ps, drops[i] * font_ps))
        drops[i] += 1
        if drops[i] * font_ps > height * 2 or random.random() > 0.93:
            drops[i] = 0
    
    pygame.display.flip()
    