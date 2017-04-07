import pygame, sys
from pygame.locals import *

pygame.init()

SCREEN_SIZE = (380, 480)
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

#COLORS
white = (255,255,255)
black = (0,0,0)

#SHAPES
shape1 = [
            [0,0,0],
            [0,1,0],
            [1,1,1]
        ]
shape2 = [
            [0,0,0],
            [0,0,1],
            [1,1,1]
        ]
shape3 = [
            [1,1],
            [1,1]
        ]
shape4 = [
            [0,1,0],
            [1,1,0],
            [1,0,0]
        ]
shape5 = [
            [0,0,0],
            [1,0,0],
            [1,1,1]
        ]
shape6 = [
            [1,0,0],
            [1,1,0],
            [0,1,0]
        ]
shape7 = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [1,1,1,1]
        ]

#MAP
tetrismap = [[0  for _ in range(9)] for _ in range(16)]

class Shape:
    def __init__(self, shape):
        self.shape = shape
        self.length = len(self.shape)
        self.size = 30
        self.width = max([ar.count(1) if ar[-1] != 1 else 3 for ar in self.shape]) * self.size
        self.movex = 0
        self.movey = 0
        self.x = 0
        self.y = 0
        self.speed = 50
        self.right = False
        self.left = False
        self.stop = False
    def rotate(self):
        mat = [line[:] for line in self.shape]
        for i in range(self.length):
            for j in range(self.length):
                mat[j][self.length-1-i] = self.shape[i][j]
        self.shape = [line[:] for line in mat]
        self.width = max([ar.count(1) if ar[-1] != 1 else 3 for ar in self.shape]) * self.size
    def update(self, dt):
        if not self.stop:
            self.movey += self.speed * dt
            if int(self.movey) % 30 == 0:
                self.y = int(self.movey)
            if self.right:
                self.movex = 30
                self.right = not self.right
            if self.left:
                self.movex = -30
                self.left = not self.left
            self.x = max(0, min(self.x + self.movex, 270 - self.width))
            self.movex = 0
                
    def draw(self):
        for row in range(self.length):
            for col in range(self.length):
                if self.shape[row][col]:
                    pygame.draw.rect(screen, white,
                                     (col*self.size+1 + self.x,row*self.size+1 + self.y,
                                      self.size-1,self.size-1))

s1 = Shape(shape5)

while True:
    if pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                s1.rotate()
            if event.key == K_RIGHT:
                s1.right = True
            if event.key == K_LEFT:
                s1.left = True
            
    screen.fill(black)
    
    pygame.draw.line(screen, white, (273, 0), (273, SCREEN_SIZE[1]))

    dt = clock.tick() / 1000

    if not s1.stop:
        s1.update(dt)
    s1.draw()

    pygame.display.update()

