'''
ATL MARATHON
NAME: SOURAV
DOC: 3/4/2022
TOPIC: Light And Reflection
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
images['surface'] = pygame.image.load(os.path.join("Data","ground.png")).convert_alpha()

class LightRay:

    def __init__(self):

        self.startPosX = 500
        self.startPosY = screenY - 100

        self.endPosFirst = [200,200]
        self.endPosSecond = [200, 200]


        self.width = 3
        self.colour = (255,255,255)

    def changeEndPos(self):
        mousePos = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()

        if mouseClick[0]:
            self.endPosFirst = mousePos

        self.endPosSecond[1] = self.endPosFirst[1]
        self.endPosSecond[0] = ((500 - self.endPosFirst[0]) * 2) + self.endPosFirst[0]

    def blitRay(self):

        self.changeEndPos()

        pygame.draw.line(screen,self.colour,(self.startPosX,self.startPosY),(self.endPosFirst),self.width)
        pygame.draw.line(screen, self.colour, (self.startPosX, self.startPosY), (self.endPosSecond),self.width)

class Surface:

    def __init__(self):

        self.posX = 0
        self.posY = screenY - 100
        self.image = images['surface']

    def blitSurface(self):
        screen.blit(self.image,(self.posX,self.posY))

class MiddleLine:

    def __init__(self):

        self.startPosX = 500
        self.startPosY = 0

        self.endPos = (500, 700)

        self.width = 5
        self.colour = (12, 12, 12)

    def blitLine(self):
        pygame.draw.line(screen,self.colour,(self.startPosX,self.startPosY),self.endPos,self.width)


light = LightRay()
surface = Surface()
middleLine = MiddleLine()

pygame.display.set_icon(images['icon'])
pygame.display.set_caption("Light And Reflection")

#game loop
while mainGame:

    screen.blit(images['background'], (0,0))

    light.blitRay()
    surface.blitSurface()
    middleLine.blitLine()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()