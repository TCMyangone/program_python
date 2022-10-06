import pygame
import math
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d

class PyramidDemo:
    def __init__(self):
        self.running = True
        self.drawing = True
        self.w, self.h = 600, 600
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()

        ### Init pymunk and create space
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.space.sleep_time_threshold = 0.3
        ### ground
        shape = pymunk.Segment(self.space.static_body, (5, 100), (595, 100), 1.0)
        shape.friction = 1.0
        self.space.add(shape)

        ### pyramid
        x = Vec2d(-270, 7.5) + (300, 100)
        y = Vec2d(0, 0)
        deltaX = Vec2d(0.5625, 1.1) * 20
        deltaY = Vec2d(1.125, 0.0) * 20

        for i in range(25):
            y = Vec2d(*x)
            for j in range(i, 25):
                size = 10
                points = [(-size, -size), (-size, size), (size, size), (size, -size)]
                mass = 1.0
                moment = pymunk.moment_for_poly(mass, points, (0, 0))
                body = pymunk.Body(mass, moment)
                body.position = y
                shape = pymunk.Poly(body, points)
                shape.friction = 1
                self.space.add(body, shape)

                y += deltaY

            x += deltaX

        ### draw options for drawing
        pymunk.pygame_util.positive_y_is_up = True
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
    
    def create_ball(self, space, radius, mass, pos):
        '''创建一个球'''
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.mass = mass
        shape.color = (255, 0, 0, 100)
        shape.elasticity = 0.8
        shape.friction = 0.6
        space.add(body, shape)
        return shape
    
    def calculate_distance(self, p1, p2):
        '''计算两点间距离'''
        return math.sqrt((p1[0] - p2[0])**2 + ((self.h - p1[1]) - (self.h - p2[1]))**2)

    def calculate_angle(self, p1, p2):
        '''求角度'''
        return math.atan2((self.h - p2[1]) - (self.h - p1[1]), p2[0] - p1[0])

    def run(self):
        self.pressed_pos = None
        self.ball = None
        while self.running:
            self.line = None
            if self.ball and self.pressed_pos:
                self.line = [self.pressed_pos, pygame.mouse.get_pos()]
            self.loop()

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(self.screen, "box2d_pyramid.png")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.drawing = not self.drawing
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.ball:
                    self.pressed_pos = self.pressed_pos_x, self.pressed_pos_y = pygame.mouse.get_pos()
                    self.ball = self.create_ball(self.space, 10, 10, (self.pressed_pos_x, self.h - self.pressed_pos_y))
                    
                elif self.pressed_pos:
                    self.ball.body.body_type = pymunk.Body.DYNAMIC
                    angle = self.calculate_angle(*self.line)
                    force = self.calculate_distance(*self.line) * 100
                    fx = math.cos(angle) * force
                    fy = math.sin(angle) * force
                    self.ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                    self.pressed_pos = None
                else:
                    self.space.remove(self.ball, self.ball.body)
                    self.ball = None

        fps = 144
        dt = 1.0 / fps
        self.space.step(dt)
        if self.drawing:
            self.draw()

        ### Tick clock and update fps in title
        self.clock.tick(fps)
        pygame.display.set_caption("fps: " + str(self.clock.get_fps()))

    def draw(self):
        ### Clear the screen
        self.screen.fill(pygame.Color("white"))
        if self.line:
            pygame.draw.line(self.screen, 'black', self.line[0], self.line[1], 3)

        ### Draw space
        self.space.debug_draw(self.draw_options)

        ### All done, lets flip the display
        pygame.display.flip()


def main():
    demo = PyramidDemo()
    demo.run()


if __name__ == "__main__":
    main()