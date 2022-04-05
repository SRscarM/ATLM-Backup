'''
ATL MARATHON
NAME: SOURAV
DOC: 4/4/2022
TOPIC: Straight lien motion
'''

#importing modules
import pygame, random
import sys, os, math

pygame.init()
pygame.font.init()

#screen variable
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

#font variables
displayFont = pygame.font.Font(None, 25)

#variables
mainGame = True
fps = 60
clock = pygame.time.Clock()

#importing images
images = {}

images['background'] = pygame.image.load(os.path.join("Data","straightLineMotionBG.png")).convert_alpha()
images['icon'] = pygame.image.load(os.path.join("Data","icon.png")).convert_alpha()
images['ball'] = pygame.image.load(os.path.join("Data","straightLineMotion.png")).convert_alpha()
images['surface'] = pygame.image.load(os.path.join("Data","straightLineMotionGround.png")).convert_alpha()

class Ball:

    def __init__(self):

        self.posX = 0
        self.posY = 0

        self.moveSpeed = 4

    def moveBall(self):

        self.posX += self.moveSpeed

        if self.posX >= 750:
            self.moveSpeed  = -4
        elif self.posX <= 0:
            self.moveSpeed = 4

    def blitBall(self):

        self.moveBall()
        screen.blit(images['ball'],(self.posX,self.posY))

class Surface:

    def __init__(self):

        self.posX = 0
        self.posY = screenY - 100
        self.image = images['surface']

    def blitSurface(self):
        screen.blit(self.image,(self.posX,self.posY))

ball = Ball()
surface = Surface()

pygame.display.set_icon(images['icon'])
pygame.display.set_caption("Motion Of Pendulum")

#game loop
while mainGame:

    screen.blit(images['background'], (0,0))

    ball.blitBall()
    surface.blitSurface()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()