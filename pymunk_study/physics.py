
from random import randint
import pygame
import pymunk
import pymunk.pygame_util
import math
import sys

pygame.init()
WIDTH, HEIGHT = 1366, 768
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
balls = []
structures = []

def add_L(space):
    '''创建'L'型的线'''
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)
    
    rotation_limit_body = pymunk.Body(body_type = pymunk.Body.STATIC) # 1
    rotation_limit_body.position = (200,300)

    body = pymunk.Body()
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0) 
    l2 = pymunk.Segment(body, (-150, 0), (-150.0, -50.0), 5.0)
    l1.mass = 10
    l2.mass = 10
    l1.friction = 3
    l2.friction = 3
    l1.elasticity = l2.elasticity = 0.7
    rotation_center_joint = pymunk.PinJoint(
        body, rotation_center_body, (0, 0), (0, 0)
    )
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(
        body, rotation_limit_body, (-100,0), (0,0), 0, 50
    )
    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1, l2

def draw(space, window, draw_options, line):
    window.fill('white')
    if line:
        pygame.draw.line(window, 'black', line[0], line[1], 3)
    space.debug_draw(draw_options)

def calculate_distance(p1, p2):
    '''计算两点间距离'''
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_angle(p1, p2):
    '''求角度'''
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def create_structure(space, width, height):
    '''创建可摧毁建筑'''
    brown = (139, 69, 19, 199)
    rects = [
        [(300, height - 120), (40, 200), brown, 100],
        [(500, height - 120), (40, 200), brown, 100],
        [(400, height - 240), (340, 40), brown, 150],
    ]

    for pos, size, color, mass in rects:
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.color = color
        shape.mass = mass
        shape.elasticity = 0.4
        shape.friction = 0.4
        structures.append(shape)
        space.add(body, shape)


def create_boundaries(space, width, height):
    '''创建边界'''
    rects = [
        [(width/2, height-10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width-10, height/2), (20, height)],
    ]
    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.8
        shape.friction = 3
        space.add(body, shape)

def create_ball(space, radius, mass, pos):
    '''创建一个球'''
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    shape.elasticity = 0.8
    shape.friction = 0.6
    balls.append(shape)
    space.add(body, shape)
    return shape
    

def run(window, width, height):
    '''主运行程序'''
    clock = pygame.time.Clock()
    fps = 144
    dt = 1 / 100
    
    space = pymunk.Space()
    space.gravity = (0, 981)
    draw_options = pymunk.pygame_util.DrawOptions(window)
    create_boundaries(space, width, height)
    create_structure(space, width, height)
    add_L(space)
    pressed_pos = None
    ball = None
    while True:
        line = None
        if ball and pressed_pos:
            line = [pressed_pos, pygame.mouse.get_pos()]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    for structure in structures:
                        space.remove(structure, structure.body)
                    structures.clear()
                    create_structure(space, width, height)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_ball(space, 20, 150, pressed_pos)
                    
                elif pressed_pos:
                    ball.body.body_type = pymunk.Body.DYNAMIC
                    angle = calculate_angle(*line)
                    force = calculate_distance(*line) * 1000
                    fx = math.cos(angle) * force
                    fy = math.sin(angle) * force
                    ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                    pressed_pos = None
                else:
                    space.remove(ball, ball.body)
                    ball = None
                    

        draw(space, window, draw_options, line)
        clock.tick(fps)
        space.step(dt)
        pygame.display.flip()


if __name__ == '__main__':
    run(window, WIDTH, HEIGHT)