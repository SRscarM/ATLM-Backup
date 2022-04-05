'''
ATL MARATHON
NAME: SOURAV
DOC: 3/4/2022
TOPIC: Motion Of Pendulam
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

images['background'] = pygame.image.load(os.path.join("Data","background.png")).convert_alpha()
images['icon'] = pygame.image.load(os.path.join("Data","icon.png")).convert_alpha()
images['pendulum'] = pygame.image.load(os.path.join("Data","pendulam.png")).convert_alpha()
images['surface'] = pygame.image.load(os.path.join("Data","ground.png")).convert_alpha()

class Pendulum:

    def __init__(self):

        self.posX = 500
        self.posY = 0

        self.maxAngle = [45,-45]
        self.currentAngle = 0
        self.addAngle = 1

        self.numOscillation = 0

        self.image = images['pendulum']

    def rotatePendulum(self, surface, angle):
        rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
        rotatedRect = rotatedSurface.get_rect(center=(self.posX, self.posY))
        return rotatedSurface, rotatedRect

    def blitPendulum(self):

        self.currentAngle += self.addAngle

        if self.currentAngle == self.maxAngle[0]:
            self.addAngle = -(self.addAngle)

        if self.currentAngle == self.maxAngle[1]:
            self.addAngle = -(self.addAngle)

        pendulumRolated, pendulumRotatedRect = self.rotatePendulum(self.image, self.currentAngle)
        screen.blit(pendulumRolated,pendulumRotatedRect)

class Surface:

    def __init__(self):

        self.posX = 0
        self.posY = screenY - 100
        self.image = images['surface']

    def blitSurface(self):
        screen.blit(self.image,(self.posX,self.posY))

pendulum = Pendulum()
surface = Surface()
pendulumRectImage = images['pendulum'].get_rect(center = (pendulum.posX,pendulum.posY))

pygame.display.set_icon(images['icon'])
pygame.display.set_caption("Motion Of Pendulum")

#game loop
while mainGame:

    screen.blit(images['background'], (0,0))

    pendulum.blitPendulum()
    surface.blitSurface()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()