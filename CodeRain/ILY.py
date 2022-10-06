import random
import sys
import pygame
pygame.init()
pyInfo = pygame.display.Info()
width, height = pyInfo.current_w, pyInfo.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
bg_surface = pygame.Surface((width, height), pygame.SRCALPHA)
letter = ['我', '爱', '你', '我', '爱你', '我爱你', '我非常爱你', '我爱你', '我爱', '我', '爱', '你', '我爱你', '爱', '我', '爱你', '我', '我爱', '爱你', '你']
font_ps = 40
font = pygame.font.SysFont('fangsong', 20)
bg_surface.fill(pygame.Color(0, 0, 0, 15))
screen.fill((0, 0, 0))
texts = [font.render(str(i), True, (248, 12, 112)) for i in letter]
colums = int(width / font_ps)
drops = [0 for i in range(colums)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
    pygame.time.delay(50)
    screen.blit(bg_surface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)
        screen.blit(text, (i * font_ps, drops[i] * font_ps))
        drops[i] += 1
        if drops[i] * font_ps > height * 2 or random.random() > 0.93:
            drops[i] = 0
    
    pygame.display.flip()
    