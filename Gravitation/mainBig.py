#importing modules
import pygame
import math
import sys

pygame.init()

#screen variables
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

#variables
mainGame = True
fps =  60

clock = pygame.time.Clock()
images = {}
isPressed = False

#game images
images['icon'] = pygame.image.load("data/icon.png").convert_alpha()
images['bg'] = pygame.image.load("data/bgBig.png").convert_alpha()
images['ball1'] = pygame.image.load("data/ballOneVersion2.png").convert_alpha()
images['ball2'] = pygame.image.load("data/ballTwo.png").convert_alpha()

#ballOne objects
class Ball1:

  def __init__(self):

    self.img = images['ball1']

    self.posCopyX = 150
    self.posCopyY = 400

    self.var = 0.25
    self.collide = 0

    self.mass = 1
    self.velocity = 0

  def showBallOne(self):
    if isPressed:
      self.velocity += self.var
      self.posCopyX += self.var

    self.width = self.img.get_width() /2
    self.height = self.img.get_height() /2
    self.posX = 150 - self.width + self.velocity - self.collide
    self.posY = 400 - self.height

    self.rect = pygame.Rect(self.posX, self.posY, self.img.get_width(),self.img.get_height())
    screen.blit(self.img,(self.posX,self.posY))


#ballOne objects
class Ball2:

  def __init__(self):

    self.img = images['ball2']

    self.posCopyX = 850
    self.posCopyY = 400

    self.collide = 0
    self.var = 6

    self.mass = 1
    self.velocity = 0

  def showBallTwo(self):
    if isPressed:
      self.velocity += self.var
      self.posCopyX -= self.var

    self.width = self.img.get_width() /2
    self.height = self.img.get_height() /2
    self.posX = 850 - self.width - self.velocity + self.collide
    self.posY = 400 - self.height

    self.rect = pygame.Rect(self.posX, self.posY, self.img.get_width(),self.img.get_height())
    screen.blit(self.img,(self.posX,self.posY))

#functions
def drawLine():
  pygame.draw.line(screen, (255,255,255), (ballOne.posCopyX, ballTwo.posCopyY),(ballTwo.posCopyX, ballTwo.posCopyY), 1)

def collision(rect,rect2):
  if rect.colliderect(rect2):
    ballOne.collide = 3
    ballTwo.collide = 3

    ballOne.var = 0
    ballTwo.var = 0

#defining icon and title
pygame.display.set_caption('Gravitation Simulation Big')
pygame.display.set_icon(images['icon'])

images['bg'] = pygame.transform.scale(images['bg'],(screenX,screenY))

#creating objects
ballOne = Ball1()
ballTwo = Ball2()

#game loop
while mainGame:
  screen.blit(images['bg'],(0,0))
  ballOne.showBallOne()
  ballTwo.showBallTwo()
  collision(ballOne.rect,ballTwo.rect)
  drawLine()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      isPressed = True

  clock.tick(fps)
  pygame.display.update()
