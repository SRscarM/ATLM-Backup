'''
ATL MARATHON
NAME: SOURAV
DOC: 31/3/2022
TOPIC: KE AND PE
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
images['ground'] = pygame.image.load(os.path.join("Data","ground.png")).convert_alpha()
images['player'] = pygame.image.load(os.path.join("Data","player.png")).convert_alpha()
images['icon'] = pygame.image.load(os.path.join("Data","icon.png")).convert_alpha()

class Player:

    def __init__(self):
        self.images = images['player']

        self.posX = 50
        self.posY = 50

        self.height = self.images.get_height()
        self.width = self.images.get_width()

        self.screenBoarderLeft = 0
        self.screenBoarderRight = screenX - 50

        self.downVel = 0.4
        self.moveVel = 0.06
        self.maxFallSpeed = 10
        self.maxMoveSpeed = 6

        self.velocity = 0
        self.mass = 5
        self.gravity = 0

        self.airTimer = 0
        self.jumpForce = -8

        self.moveRight = False
        self.moveLeft = False

    def movePlayer(self):

        self.distanceFromGround = (700 - (self.posY + 25))/100

        self.gravity += self.downVel
        self.posY += self.gravity

        self.storeGarvity = self.gravity

        if self.gravity >= self.maxFallSpeed:
            self.gravity = self.maxFallSpeed

        self.playerRect = pygame.Rect(self.posX, self.posY, self.width, self.height)

        if self.moveRight == True and self.posX < self.screenBoarderRight:

            self.velocity += self.moveVel
            self.posX += self.velocity

            if self.velocity >= self.maxMoveSpeed:
                self.velocity = self.maxMoveSpeed

        elif self.moveLeft == True and self.posX > self.screenBoarderLeft:

            self.velocity += self.moveVel
            self.posX -= self.velocity

            if self.velocity >= self.maxMoveSpeed:
                self.velocity = self.maxMoveSpeed

        elif self.moveLeft == False and self.moveRight == False:
            self.velocity = 0

    def blitPlayer(self):

        self.movePlayer()
        screen.blit(self.images,(self.posX, self.posY))

class Ground:

    def __init__(self):
        self.images = images['ground']
        self.posX = 0
        self.posY = screenY - self.images.get_height()

        self.height = self.images.get_height()
        self.width = self.images.get_width()

    def blitGround(self):
        self.groundRect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        screen.blit(self.images,(self.posX, self.posY))

class Platform:

    def __init__(self):

        self.posX = 300
        self.posY = 500

        self.height = 20
        self.width = 400

        self.colour = (12,12,12)

        self.rectOne = pygame.Rect((self.posX,self.posY),(self.width,self.height))
        self.rectTwo = pygame.Rect((self.posX, self.posY - 200), (self.width, self.height))

    def blitPlatform(self):
        pygame.draw.rect(screen,self.colour,self.rectOne)
        pygame.draw.rect(screen, self.colour, self.rectTwo)

player = Player()
ground = Ground()
platform = Platform()

def collision(playerRect,groundRect,platformRectOne,platformRectTwo):

  if playerRect.colliderect(groundRect):
      player.gravity = 0
      player.downVel = 0
      player.airTimer = 0

  elif playerRect.colliderect(platformRectOne):
      player.gravity = 0
      player.downVel = 0
      player.airTimer = 0

  elif playerRect.colliderect(platformRectTwo):
      player.gravity = 0
      player.downVel = 0
      player.airTimer = 0

  else:
      player.downVel = 0.2
      player.airTimer += 1

def showText(K,P):
  KEimage = displayFont.render(("KE = " + K + " J"), True, (255,255,255))
  PEimage = displayFont.render(("PE = " + P + " J"), True, (255,255,255))

  playerVelocity = displayFont.render(("Player's Velocity = " + str(round(player.velocity))), True, (255, 255, 255))
  playerHeight = displayFont.render(("Player's Height = " + str(round(player.distanceFromGround))), True, (255, 255, 255))
  playerMass = displayFont.render(("Player's Mass = " + str(player.mass)), True, (255, 255, 255))

  screen.blit(KEimage,(20,20))
  screen.blit(PEimage, (20, 60))

  screen.blit(playerVelocity, (20, 100))
  screen.blit(playerHeight, (20, 140))
  screen.blit(playerMass, (20, 180))

pygame.display.set_icon(images['icon'])
pygame.display.set_caption("KE/PE Simulation")

#game loop
while mainGame:

    screen.blit(images['background'], (0,0))

    player.blitPlayer()
    ground.blitGround()
    platform.blitPlatform()

    collision(player.playerRect,ground.groundRect,platform.rectOne,platform.rectTwo)

    if player.gravity != 0:
        KineticEnergy = str(round(player.mass * (player.storeGarvity * player.storeGarvity)/2))
    else:
        KineticEnergy = str(round(player.mass * (player.velocity * player.velocity)/2))

    PotentialEnergy = str(round(player.mass * 9.8 * player.distanceFromGround))

    showText(KineticEnergy,PotentialEnergy)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                player.moveRight = True
            if event.key == pygame.K_a:
                player.moveLeft = True

            if event.key == pygame.K_SPACE:
                if player.airTimer < 6:
                    player.gravity = player.jumpForce

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                player.moveRight = False
            if event.key == pygame.K_a:
                player.moveLeft = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()