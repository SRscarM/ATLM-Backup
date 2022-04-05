'''
ATL MARATHON
NAME: SOURAV
DOC: 4/4/2022
TOPIC: Circular motion
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
images['circle'] = pygame.image.load(os.path.join("Data","circularMotion.png")).convert_alpha()
images['surface'] = pygame.image.load(os.path.join("Data","circularGround.png")).convert_alpha()

class Circle:

  def __init__(self):

    self.addAngle = 0
    self.image = images['circle']
    self.positionX = (screenX / 2) + 5
    self.positionY = (screenY / 2) - 15

  def rotateCircle(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitCircle(self):
    self.addAngle += 1
    circleRotated,circleRotatedRect = self.rotateCircle(self.image, self.addAngle)
    screen.blit(circleRotated,circleRotatedRect)

class Surface:

    def __init__(self):

        self.posX = 0
        self.posY = screenY - 100
        self.image = images['surface']

    def blitSurface(self):
        screen.blit(self.image,(self.posX,self.posY))

pygame.display.set_icon(images['icon'])
pygame.display.set_caption("Motion Of Pendulum")

surface = Surface()
circle = Circle()

circleRectImage = images['circle'].get_rect(center = (circle.positionX,circle.positionY))

#game loop
while mainGame:

    screen.blit(images['background'], (0,0))

    circle.blitCircle()
    surface.blitSurface()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()