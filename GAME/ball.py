import sys, pygame
pygame.init()
print(pygame.version.ver)
clock = pygame.time.Clock()
size = width, height = 800, 600
speed = [3, 3]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load(r'D:\program_python\GAME\ball.bmp')
ballrect = ball.get_rect()

while 1:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	elif ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	screen.fill(black)
	pygame.draw.circle(screen, (0, 255, 0), (400, 300), 100, width=10)
	screen.blit(ball, ballrect)
	pygame.display.flip()