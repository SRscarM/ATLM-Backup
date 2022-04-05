'''
ATL MARATHON
NAME: SOURAV
DOC: 31/3/2022
TOPIC: KE AND PE
'''

#importing modules
import pygame
import sys, os

pygame.init()
pygame.font.init()

#screen variable
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

#variables
mainGame = True
fps = 60
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)
smallFont = pygame.font.Font(None,30)

icon = pygame.image.load(os.path.join("icon.png"))

pygame.display.set_icon(icon)
pygame.display.set_caption("FunWithQuads")

class Pointer:

    def __init__(self):

        self.width = 4
        self.colour = (0,0,0)

        self.points = [(0,0),(0,0),(0,0)]

    def blitLine(self):

        self.storagePos()
        pygame.draw.polygon(screen, (0,0,0), self.points, self.width)

    def storagePos(self):

        self.pos = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if self.click[0]:
            self.points.append(self.pos)
        if self.click[2]:
            self.points.pop(0)

def showText(text):
    textImage = font.render(text,True,(0,0,0))

    leftClickImage = smallFont.render("Left Click = Add Vertex", True, (0, 0, 0))
    rightClickImage = smallFont.render("Right Click = Remove Vertex", True, (0, 0, 0))

    posX = screenX/2
    posY = 50

    imageHeight = textImage.get_height()
    imageWidth = textImage.get_width()

    screen.blit(textImage,(posX - imageWidth/2,posY-imageHeight))
    screen.blit(leftClickImage, (20, 800 - 100))
    screen.blit(rightClickImage, (20, 800 - 50))

pointer = Pointer()

#game loop
while mainGame:

    screen.fill((255,255,255))
    pointer.blitLine()

    showText("FUN WITH POLYGONS, MAKE WHAT YOU WANT!")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()


