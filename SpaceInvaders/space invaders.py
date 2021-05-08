#importing libraries
import pygame
import time
import math
import random
#initiates pygame
pygame.init()
#display width and height
display_width = 800
display_height = 600
#display window
gameDisplay = pygame.display.set_mode((display_width, display_height))#display window hello there
pygame.display.set_caption('Space Invaders Version 1.2')#display caption
#rgb for display color
black = (0, 0, 0)
white = (255, 255, 255)
#clock speed
clock = pygame.time.Clock()
#while loop 1 variable
crashed = False
#sprites
playerImg = pygame.image.load('playerinvader.png')
bullImg = pygame.image.load('bullinvader.png')
invader1Img = pygame.image.load('invaderrow1.png')
invader2Img = pygame.image.load('invaderrow2.png')
invader3Img = pygame.image.load('invaderrow4.png')
invader4Img = pygame.image.load('invaderfree.png')
shield1Img = pygame.image.load('shield1.png')
shield2Img = pygame.image.load('shield1.png')
shield3Img = pygame.image.load('shield1.png')
shield4Img = pygame.image.load('shield1.png')
gamemoverImg = pygame.image.load('gameover.png')
livesImg = pygame.image.load('lives1.png')
benningningImg = pygame.image.load('benningnigsi.jpg')
explosionImg = pygame.image.load('explosion.png')
#sprite displayer things(for general stuff)
def player(x, y):
    gameDisplay.blit(playerImg, (x, y))
def bullet(bullx, bully):
    gameDisplay.blit(bullImg, (bullx, bully))
def enem1bull(e1bullx, e1bully):
    gameDisplay.blit(bullImg, (e1bullx, e1bully))
def enem2bull(e2bullx, e2bully):
    gameDisplay.blit(bullImg, (e2bullx, e2bully))
def enem3bull(e3bullx, e3bully):
    gameDisplay.blit(bullImg, (e3bullx, e3bully))
def enem4bull(e4bullx, e4bully):
    gameDisplay.blit(bullImg, (e4bullx, e4bully))
def enem5bull(e5bullx, e5bully):
    gameDisplay.blit(bullImg, (e5bullx, e5bully))
def shield1(shield1x, shieldy):
    gameDisplay.blit(shield1Img, (shield1x, shieldy))
def shield2(shield2x, shieldy):
    gameDisplay.blit(shield2Img, (shield2x, shieldy))
def shield3(shield3x, shieldy):
    gameDisplay.blit(shield3Img, (shield3x, shieldy))
def shield4(shield4x, shieldy):
    gameDisplay.blit(shield4Img, (shield4x, shieldy))
def gameover(gmx,gmy):
    gameDisplay.blit(gamemoverImg, (gmx, gmy))
def livessprite(livex, livey):
    gameDisplay.blit(livesImg, (livex, livey))
def benningnigsprite(begx, begy):
    gameDisplay.blit(benningningImg, (begx, begy))
def invaderfree(invaderfreex, invaderfreey):
    gameDisplay.blit(invader4Img, (invaderfreex, invaderfreey))
def explosion(ex, ey):
    gameDisplay.blit(explosionImg, (ex, ey))
#row 1 invader displayer
def invader1_6(invader1_6x, invader1_6y):
    gameDisplay.blit(invader1Img, (invader1_6x, invader1_6y))
def invader1_1(invader1_1x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_1x, invader1_1y))
def invader1_2(invader1_2x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_2x, invader1_1y))
def invader1_3(invader1_3x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_3x, invader1_1y))
def invader1_4(invader1_4x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_4x, invader1_1y))
def invader1_5(invader1_5x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_5x, invader1_1y))
def invader1_6real(invader1_6realx, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_6realx, invader1_1y))
def invader1_7(invader1_7x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_7x, invader1_1y))
def invader1_8(invader1_8x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_8x, invader1_1y))
def invader1_9(invader1_9x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_9x, invader1_1y))
def invader1_10(invader1_10x, invader1_1y):
    gameDisplay.blit(invader1Img, (invader1_10x, invader1_1y))
#row 1 collsion
def invader1_1col(bullx, bully, invader1_1x, invader1_1y):
    distance1 = math.sqrt(math.pow(invader1_1x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance1 < 30:
        return True
    else:
        return False
def invader1_2col(bullx, bully, invader1_2x, invader1_1y):
    distance2 = math.sqrt(math.pow(invader1_2x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance2 < 30:
        return True
    else:
        return False
def invader1_3col(bullx, bully, invader1_3x, invader1_1y):
    distance3 = math.sqrt(math.pow(invader1_3x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance3 < 30:
        return True
    else:
        return False
def invader1_4col(bullx, bully, invader1_4x, invader1_1y):
    distance4 = math.sqrt(math.pow(invader1_4x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance4 < 30:
        return True
    else:
        return False
def invader1_5col(bullx, bully, invader1_5x, invader1_1y):
    distance5 = math.sqrt(math.pow(invader1_5x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance5 < 30:
        return True
    else:
        return False
def invader1_6col(bullx, bully, invader1_6realx, invader1_1y):
    distance6 = math.sqrt(math.pow(invader1_6realx - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance6 < 30:
        return True
    else:
        return False
def invader1_7col(bullx, bully, invader1_7x, invader1_1y):
    distance7 = math.sqrt(math.pow(invader1_7x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance7 < 30:
        return True
    else:
        return False
def invader1_8col(bullx, bully, invader1_8x, invader1_1y):
    distance8 = math.sqrt(math.pow(invader1_8x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance8 < 30:
        return True
    else:
        return False
def invader1_9col(bullx, bully, invader1_9x, invader1_1y):
    distance9 = math.sqrt(math.pow(invader1_9x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance9 < 30:
        return True
    else:
        return False
def invader1_10col(bullx, bully, invader1_10x, invader1_1y):
    distance10 = math.sqrt(math.pow(invader1_10x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance10 < 30:
        return True
    else:
        return False
def invader1_11col(bullx, bully, invader1_6x, invader1_1y):
    distance11 = math.sqrt(math.pow(invader1_6x - bullx, 2) + math.pow(invader1_1y - bully, 2))
    if distance11 < 30:
        return True
    else:
        return False
#row2 invaders
def invader2_1(invader2_1x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_1x, invader2_1y))
def invader2_2(invader2_2x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_2x, invader2_1y))
def invader2_3(invader2_3x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_3x, invader2_1y))
def invader2_4(invader2_4x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_4x, invader2_1y))
def invader2_5(invader2_5x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_5x, invader2_1y))
def invader2_6(invader2_6x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_6x, invader2_1y))
def invader2_7(invader2_7x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_7x, invader2_1y))
def invader2_8(invader2_8x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_8x, invader2_1y))
def invader2_9(invader2_9x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_9x, invader2_1y))
def invader2_10(invader2_10x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_10x, invader2_1y))
def invader2_11(invader2_11x, invader2_1y):
    gameDisplay.blit(invader2Img, (invader2_11x, invader2_1y))
#row 2 collision
def invader2_1col(bullx, bully, invader2_1x, invader2_1y):
    distance1a = math.sqrt(math.pow(invader2_1x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance1a < 30:
        return True
    else:
        return False
def invader2_2col(bullx, bully, invader2_2x, invader2_1y):
    distance2a = math.sqrt(math.pow(invader2_2x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance2a < 30:
        return True
    else:
        return False
def invader2_3col(bullx, bully, invader2_3x, invader2_1y):
    distance3a = math.sqrt(math.pow(invader2_3x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance3a < 30:
        return True
    else:
        return False
def invader2_4col(bullx, bully, invader2_4x, invader2_1y):
    distance4a = math.sqrt(math.pow(invader2_4x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance4a < 30:
        return True
    else:
        return False
def invader2_5col(bullx, bully, invader2_5x, invader2_1y):
    distance5a = math.sqrt(math.pow(invader2_5x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance5a < 30:
        return True
    else:
        return False
def invader2_6col(bullx, bully, invader2_6x, invader2_1y):
    distance6a = math.sqrt(math.pow(invader2_6x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance6a < 30:
        return True
    else:
        return False
def invader2_7col(bullx, bully, invader2_7x, invader2_1y):
    distance7a = math.sqrt(math.pow(invader2_7x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance7a < 30:
        return True
    else:
        return False
def invader2_8col(bullx, bully, invader2_8x, invader2_1y):
    distance8a = math.sqrt(math.pow(invader2_8x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance8a < 30:
        return True
    else:
        return False
def invader2_9col(bullx, bully, invader2_9x, invader2_1y):
    distance9a = math.sqrt(math.pow(invader2_9x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance9a < 30:
        return True
    else:
        return False
def invader2_10col(bullx, bully, invader2_10x, invader2_1y):
    distance10a = math.sqrt(math.pow(invader2_10x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance10a < 30:
        return True
    else:
        return False
def invader2_11col(bullx, bully, invader2_11x, invader2_1y):
    distance11a = math.sqrt(math.pow(invader2_11x - bullx, 2) + math.pow(invader2_1y - bully, 2))
    if distance11a < 30:
        return True
    else:
        return False
#row 3 invaders
def invader3_1(invader3_1x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_1x, invader3y))
def invader3_2(invader3_2x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_2x, invader3y))
def invader3_3(invader3_3x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_3x, invader3y))
def invader3_4(invader3_1x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_4x, invader3y))
def invader3_5(invader3_5x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_5x, invader3y))
def invader3_6(invader3_6x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_6x, invader3y))
def invader3_7(invader3_7x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_7x, invader3y))
def invader3_8(invader3_8x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_8x, invader3y))
def invader3_9(invader3_9x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_9x, invader3y))
def invader3_10(invader3_10x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_10x, invader3y))
def invader3_11(invader3_11x, invader3y):
    gameDisplay.blit(invader2Img, (invader3_11x, invader3y))
# row 3 collision
def invader3_1col(bullx, bully, invader3_1x, invader3y):
    distance1b = math.sqrt(math.pow(invader3_1x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance1b < 30:
        return True
    else:
        return False
def invader3_2col(bullx, bully, invader3_2x, invader3y):
    distance2b = math.sqrt(math.pow(invader3_2x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance2b < 30:
        return True
    else:
        return False
def invader3_3col(bullx, bully, invader3_3x, invader3y):
    distance3b = math.sqrt(math.pow(invader3_3x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance3b < 30:
        return True
    else:
        return False
def invader3_4col(bullx, bully, invader3_4x, invader3y):
    distance4b = math.sqrt(math.pow(invader3_4x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance4b < 30:
        return True
    else:
        return False
def invader3_5col(bullx, bully, invader3_5x, invader3y):
    distance5b = math.sqrt(math.pow(invader3_5x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance5b < 30:
        return True
    else:
        return False
def invader3_6col(bullx, bully, invader3_6x, invader3y):
    distance6b = math.sqrt(math.pow(invader3_6x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance6b < 30:
        return True
    else:
        return False
def invader3_7col(bullx, bully, invader3_7x, invader3y):
    distance7b = math.sqrt(math.pow(invader3_7x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance7b < 30:
        return True
    else:
        return False
def invader3_8col(bullx, bully, invader3_8x, invader3y):
    distance8b = math.sqrt(math.pow(invader3_8x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance8b < 30:
        return True
    else:
        return False
def invader3_9col(bullx, bully, invader3_9x, invader3y):
    distance9b = math.sqrt(math.pow(invader3_9x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance9b < 30:
        return True
    else:
        return False
def invader3_10col(bullx, bully, invader3_10x, invader3y):
    distance10b = math.sqrt(math.pow(invader3_10x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance10b < 30:
        return True
    else:
        return False
def invader3_11col(bullx, bully, invader3_11x, invader3y):
    distance11b = math.sqrt(math.pow(invader3_11x - bullx, 2) + math.pow(invader3y - bully, 2))
    if distance11b < 30:
        return True
    else:
        return False
#row 4 invaders
def invader4_1(invader4_1x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_1x, invader4y))
def invader4_2(invader4_2x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_2x, invader4y))
def invader4_3(invader4_3x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_3x, invader4y))
def invader4_4(invader4_4x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_4x, invader4y))
def invader4_5(invader4_5x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_5x, invader4y))
def invader4_6(invader4_6x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_6x, invader4y))
def invader4_7(invader4_7x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_7x, invader4y))
def invader4_8(invader4_8x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_8x, invader4y))
def invader4_9(invader4_9x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_9x, invader4y))
def invader4_10(invader4_10x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_10x, invader4y))
def invader4_11(invader4_11x, invader4y):
    gameDisplay.blit(invader3Img, (invader4_11x, invader4y))
#row 4 collision
def invader4_1col(bullx, bully, invader4_1x, invader4y):
    distance1c = math.sqrt(math.pow(invader4_1x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance1c < 30:
        return True
    else:
        return False
def invader4_2col(bullx, bully, invader4_2x, invader4y):
    distance2c = math.sqrt(math.pow(invader4_2x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance2c < 30:
        return True
    else:
        return False
def invader4_3col(bullx, bully, invader4_3x, invader4y):
    distance3c = math.sqrt(math.pow(invader4_3x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance3c < 30:
        return True
    else:
        return False
def invader4_4col(bullx, bully, invader4_4x, invader4y):
    distance4c = math.sqrt(math.pow(invader4_4x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance4c < 30:
        return True
    else:
        return False
def invader4_5col(bullx, bully, invader4_5x, invader4y):
    distance5c = math.sqrt(math.pow(invader4_5x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance5c < 30:
        return True
    else:
        return False
def invader4_6col(bullx, bully, invader4_6x, invader4y):
    distance6c = math.sqrt(math.pow(invader4_6x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance6c < 30:
        return True
    else:
        return False
def invader4_7col(bullx, bully, invader4_7x, invader4y):
    distance7c = math.sqrt(math.pow(invader4_7x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance7c < 30:
        return True
    else:
        return False
def invader4_8col(bullx, bully, invader4_8x, invader4y):
    distance8c = math.sqrt(math.pow(invader4_8x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance8c < 30:
        return True
    else:
        return False
def invader4_9col(bullx, bully, invader4_9x, invader4y):
    distance9c = math.sqrt(math.pow(invader4_9x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance9c < 30:
        return True
    else:
        return False
def invader4_10col(bullx, bully, invader4_10x, invader4y):
    distance10c = math.sqrt(math.pow(invader4_10x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance10c < 30:
        return True
    else:
        return False
def invader4_11col(bullx, bully, invader4_11x, invader4y):
    distance11c = math.sqrt(math.pow(invader4_11x - bullx, 2) + math.pow(invader4y - bully, 2))
    if distance11c < 30:
        return True
    else:
        return False
#row 5 invaders
def invader5_1(invader5_1x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_1x, invader5y))
def invader5_2(invader5_2x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_2x, invader5y))
def invader5_3(invader5_3x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_3x, invader5y))
def invader5_4(invader5_4x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_4x, invader5y))
def invader5_5(invader5_5x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_5x, invader5y))
def invader5_6(invader5_6x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_6x, invader5y))
def invader5_7(invader5_7x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_7x, invader5y))
def invader5_8(invader5_8x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_8x, invader5y))
def invader5_9(invader5_9x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_9x, invader5y))
def invader5_10(invader5_10x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_10x, invader5y))
def invader5_11(invader5_11x, invader5y):
    gameDisplay.blit(invader3Img, (invader5_11x, invader5y))
#row 5 collision
def invader5_1col(bullx, bully, invader5_1x, invader4y):
    distance1d = math.sqrt(math.pow(invader5_1x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance1d < 30:
        return True
    else:
        return False
def invader5_2col(bullx, bully, invader5_2x, invader4y):
    distance2d = math.sqrt(math.pow(invader5_2x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance2d < 30:
        return True
    else:
        return False
def invader5_3col(bullx, bully, invader5_3x, invader4y):
    distance3d = math.sqrt(math.pow(invader5_3x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance3d < 30:
        return True
    else:
        return False
def invader5_4col(bullx, bully, invader5_4x, invader4y):
    distance4d = math.sqrt(math.pow(invader5_4x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance4d < 30:
        return True
    else:
        return False
def invader5_5col(bullx, bully, invader5_5x, invader4y):
    distance5d = math.sqrt(math.pow(invader5_5x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance5d < 30:
        return True
    else:
        return False
def invader5_6col(bullx, bully, invader5_6x, invader4y):
    distance6d = math.sqrt(math.pow(invader5_6x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance6d < 30:
        return True
    else:
        return False
def invader5_7col(bullx, bully, invader5_7x, invader4y):
    distance7d = math.sqrt(math.pow(invader5_7x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance7d < 30:
        return True
    else:
        return False
def invader5_8col(bullx, bully, invader5_8x, invader4y):
    distance8d = math.sqrt(math.pow(invader5_8x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance8d < 30:
        return True
    else:
        return False
def invader5_9col(bullx, bully, invader5_9x, invader4y):
    distance9d = math.sqrt(math.pow(invader5_9x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance9d < 30:
        return True
    else:
        return False
def invader5_10col(bullx, bully, invader5_10x, invader4y):
    distance10d = math.sqrt(math.pow(invader5_10x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance10d < 30:
        return True
    else:
        return False
def invader5_11col(bullx, bully, invader5_11x, invader4y):
    distance11d = math.sqrt(math.pow(invader5_11x - bullx, 2) + math.pow(invader5y - bully, 2))
    if distance11d < 30:
        return True
    else:
        return False
#shield 1 collision
def shield1col(shield1x, shieldy, e1bullx, e1bully):
    distance1e = math.sqrt(math.pow(shield1x - e1bullx, 2) + math.pow(shieldy - e1bully, 2))
    if distance1e < 60:
        return True
    else:
        return False
def shield1col2(shield1x, shieldy, e2bullx, e2bully):
    distance2e = math.sqrt(math.pow(shield1x - e2bullx, 2) + math.pow(shieldy - e2bully, 2))
    if distance2e < 60:
        return True
    else:
        return False
def shield1col3(shield1x, shieldy, e3bullx, e3bully):
    distance3e = math.sqrt(math.pow(shield1x - e1bullx, 2) + math.pow(shieldy - e3bully, 2))
    if distance3e < 60:
        return True
    else:
        return False
def shield1col4(shield1x, shieldy, e4bullx, e4bully):
    distance4e = math.sqrt(math.pow(shield1x - e4bullx, 2) + math.pow(shieldy - e4bully, 2))
    if distance4e < 60:
        return True
    else:
        return False
def shield1col5(shield1x, shieldy, e5bullx, e5bully):
    distance5e = math.sqrt(math.pow(shield1x - e4bullx, 2) + math.pow(shieldy - e4bully, 2))
    if distance5e < 60:
        return True
    else:
        return False
#shield 2 collision
def shield2col(shield2x, shieldy, e1bullx, e1bully):
    distance1f = math.sqrt(math.pow(shield2x - e1bullx, 2) + math.pow(shieldy - e1bully, 2))
    if distance1f < 60:
        return True
    else:
        return False
def shield2col2(shield2x, shieldy, e2bullx, e2bully):
    distance2f = math.sqrt(math.pow(shield2x - e2bullx, 2) + math.pow(shieldy - e2bully, 2))
    if distance2f < 60:
        return True
    else:
        return False
def shield2col3(shield2x, shieldy, e3bullx, e3bully):
    distance3f = math.sqrt(math.pow(shield2x - e3bullx, 2) + math.pow(shieldy - e3bully, 2))
    if distance3f < 60:
        return True
    else:
        return False
def shield2col4(shield2x, shieldy, e4bullx, e4bully):
    distance4f = math.sqrt(math.pow(shield2x - e4bullx, 2) + math.pow(shieldy - e4bully, 2))
    if distance4f < 60:
        return True
    else:
        return False
def shield2col5(shield2x, shieldy, e5bullx, e5bully):
    distance5f = math.sqrt(math.pow(shield2x - e5bullx, 2) + math.pow(shieldy - e5bully, 2))
    if distance5f < 60:
        return True
    else:
        return False
#shield 3 collision:
def shield3col(shield3x, shieldy, e1bullx, e1bully):
    distance1g = math.sqrt(math.pow(shield3x - e1bullx, 2) + math.pow(shieldy - e1bully, 2))
    if distance1g < 60:
        return True
    else:
        return False
def shield3col2(shield3x, shieldy, e2bullx, e2bully):
    distance2g = math.sqrt(math.pow(shield3x - e2bullx, 2) + math.pow(shieldy - e2bully, 2))
    if distance2g < 60:
        return True
    else:
        return False
def shield3col3(shield3x, shieldy, e3bullx, e3bully):
    distance3g = math.sqrt(math.pow(shield3x - e1bullx, 2) + math.pow(shieldy - e3bully, 2))
    if distance3g < 60:
        return True
    else:
        return False
def shield3col4(shield3x, shieldy, e4bullx, e4bully):
    distance4g = math.sqrt(math.pow(shield3x - e4bullx, 2) + math.pow(shieldy - e4bully, 2))
    if distance4g < 60:
        return True
    else:
        return False
def shield3col5(shield3x, shieldy, e5bullx, e5bully):
    distance5g = math.sqrt(math.pow(shield3x - e5bullx, 2) + math.pow(shieldy - e5bully, 2))
    if distance5g < 60:
        return True
    else:
        return False
#shield 4 collision
def shield4col(shield4x, shieldy, e1bullx, e1bully):
    distance1h = math.sqrt(math.pow(shield4x - e1bullx, 2) + math.pow(shieldy - e1bully, 2))
    if distance1h < 60:
        return True
    else:
        return False
def shield4col2(shield4x, shieldy, e2bullx, e2bully):
    distance2h = math.sqrt(math.pow(shield4x - e2bullx, 2) + math.pow(shieldy - e2bully, 2))
    if distance2h < 60:
        return True
    else:
        return False
def shield4col3(shield4x, shieldy, e3bullx, e3bully):
    distance3h = math.sqrt(math.pow(shield4x - e3bullx, 2) + math.pow(shieldy - e3bully, 2))
    if distance3h < 60:
        return True
    else:
        return False
def shield4col4(shield4x, shieldy, e4bullx, e4bully):
    distance4h = math.sqrt(math.pow(shield4x - e4bullx, 2) + math.pow(shieldy - e4bully, 2))
    if distance4h < 60:
        return True
    else:
        return False
def shield4col5(shield4x, shieldy, e5bullx, e5bully):
    distance5h = math.sqrt(math.pow(shield4x - e5bullx, 2) + math.pow(shieldy - e5bully, 2))
    if distance5h < 60:
        return True
    else:
        return False
#player bullet collision
def playercol(x, y, e1bullx, e1bully):
    distance1i = math.sqrt(math.pow(x - e1bullx, 2) + math.pow(y - e1bully, 2))
    if distance1i < 40:
        return True
    else:
        return False
def playercol2(x, y, e2bullx, e2bully):
    distance2i = math.sqrt(math.pow(x - e2bullx, 2) + math.pow(y - e2bully, 2))
    if distance2i < 40:
        return True
    else:
        return False
def playercol3(x, y, e3bullx, e3bully):
    distance3i = math.sqrt(math.pow(x - e3bullx, 2) + math.pow(y - e3bully, 2))
    if distance3i < 40:
        return True
    else:
        return False
def playercol4(x, y, e4bullx, e4bully):
    distance4i = math.sqrt(math.pow(x - e4bullx, 2) + math.pow(y - e4bully, 2))
    if distance4i < 40:
        return True
    else:
        return False
def playercol5(x, y, e5bullx, e5bully):
    distance5i = math.sqrt(math.pow(x - e5bullx, 2) + math.pow(y - e5bully, 2))
    if distance5i < 40:
        return True
    else:
        return False
#shield bullet col
def shieldbullcol(shield1x, shieldy, bullx, bully):
    distance1j = math.sqrt(math.pow(shield1x - bullx, 2) + math.pow(shieldy - bully, 2))
    if distance1j < 50:
        return True
    else:
        return False
def shieldbullcol2(shield2x, shieldy, bullx, bully):
    distance2j = math.sqrt(math.pow(shield2x - bullx, 2) + math.pow(shieldy - bully, 2))
    if distance2j < 50:
        return True
    else:
        return False
def shieldbullcol3(shield3x, shieldy, bullx, bully):
    distance3j = math.sqrt(math.pow(shield3x - bullx, 2) + math.pow(shieldy - bully, 2))
    if distance3j < 50:
        return True
    else:
        return False
def shieldbullcol4(shield4x, shieldy, bullx, bully):
    distance4j = math.sqrt(math.pow(shield4x - bullx, 2) + math.pow(shieldy - bully, 2))
    if distance4j < 50:
        return True
    else:
        return False
def transition(row1_count, row2_count, row3_count, row4_count, row5_count):
    if row1_count <= 0 and row2_count <= 0 and row3_count <= 0 and row4_count <= 0 and row5_count <= 0:
        return True
    else:
        return False
def freeinvadercol(freeinvaderx, freeinvadery, bullx, bully):
    distance1k = math.sqrt(math.pow(freeinvaderx - bullx, 2) + math.pow(freeinvadery - bully, 2))
    if distance1k < 40:
        return True
    else:
        return False
#disorganised x and y coordinates
invaderfreex = 83904
invaderfreey = 82390
invaderfreex_change = 0
timer8 = 0
invisx = 50
invisx2 = 650
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
bullx = 100000
bully = 384724
bully_change = 0
bullet_state = True
e1bullx = 93174
e1bully = 32942
e1bull_state = False
e1bully_change = 0
e2bullx = 23894
e2bully = 72384
e3bullx = 23475
e3bully = 27945
e4bullx = 83492
e4bully = 23792
e5bullx = 27398
e5bully = 28934
begx = 0
begy = 0
#the invader coords are more organized though
#invader coords and movement pattern
invader1_6x = 650
invader1_6y = 20
invader1_6x_change = 0 #<-- universal x and y changers
invader1_6y_change = 0 #<--(i did name them for row one, colunm 6 but i didnt feel like changing it)
invader1_1x = 50
invader1_1y = 20 #<-- random idea change making the this y the universal y
invader1_2x = 110
invader1_3x = 170
invader1_4x = 230
invader1_5x = 290
invader1_6realx = 350
invader1_7x = 410
invader1_8x = 470
invader1_9x = 530
invader1_10x = 590
#row 2 invaders
invader2_1y = 70
invader2_1x = invader1_1x #the row 2 x posisiton basically equal the x coords of row 2
invader2_2x = invader1_2x
invader2_3x = invader1_3x
invader2_4x = invader1_4x
invader2_5x = invader1_5x
invader2_6x = invader1_6realx
invader2_7x = invader1_7x
invader2_8x = invader1_8x
invader2_9x = invader1_9x
invader2_10x = invader1_10x
invader2_11x = invader1_6x
#row 3 invaders
invader3y = 120
invader3_1x = invader2_1x
invader3_2x = invader2_2x
invader3_3x = invader2_3x
invader3_4x = invader2_4x
invader3_5x = invader2_5x
invader3_6x = invader2_6x
invader3_7x = invader2_7x
invader3_8x = invader2_8x
invader3_9x = invader2_9x
invader3_10x = invader2_10x
invader3_11x = invader2_11x
#row 4 invader pos
invader4y = 165
invader4_1x = invader3_1x
invader4_2x = invader3_2x
invader4_3x = invader3_3x
invader4_4x = invader3_4x
invader4_5x = invader3_5x
invader4_6x = invader3_6x
invader4_7x = invader3_7x
invader4_8x = invader3_8x
invader4_9x = invader3_9x
invader4_10x = invader3_10x
invader4_11x = invader3_11x
#row 5 invader pos
invader5y = 210
invader5_1x = invader4_1x
invader5_2x = invader4_2x
invader5_3x = invader4_3x
invader5_4x = invader4_4x
invader5_5x = invader4_5x
invader5_6x = invader4_6x
invader5_7x = invader4_7x
invader5_8x = invader4_8x
invader5_9x = invader4_9x
invader5_10x = invader4_10x
invader5_11x = invader4_11x
#other stuff
invader1right = True
invader1left = False
movedown = False
timer1 = 0#<-- some timers
timer2 = 0
timer3 = 0
timer4 = 0
timer5 = 0
timer6 = 0
timer7 = 0
timerdown = 0
e2bull_state = False#whether the enemy can shoot a bullet(similar to regular bull_state but with the player)
e3bull_state = False
e4bull_state = False
e5bull_state = False
#count of the invaders on each row
row1_count = 11
row2_count = 11
row3_count = 11
row4_count = 11
row5_count = 11
#shield stuff
shield1x = 100
shieldy = 400
shield2x = 250
shield3x = 500
shield4x = 650
shield1_status = 5
shield2_status = 5
shield3_status = 5
shield4_status = 5
#other stuff
sprite_timer = 0
lives = 3
reset = False
gmx = 400
gmy = 23453
deathtimer = 0
livex = 600
livey = -40
score = 0
font = pygame.font.Font('8bit.ttf', 22) #<--- font for score display
textX = 10
textY = 10
prevscore = 0 #this is for stage 2
stage2 = False #also for stage 2
win = False #if player wins the game!
#other random stuff
benningning = True
goacross = False
ex = 278934
ey = 283490
#other timer lol
timer9 = 0
#brief intro to code
print("x-----------------------------------------x")
print(" Space Invaders Version 1.2 By DrSquid")
print("")
print(" Controls:")
print("")
print(" D or Left Arrow Key: Move Left")
print("")
print(" A or Right Arrow Key: Move Right")
print("")
print(" Spacebar: Shoot")
print("")
print(" Press the space bar to start.")
print("x-----------------------------------------x")
#title screen
while benningning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time.sleep(3)
                benningning = False
    benningnigsprite(begx, begy)
    pygame.display.update()
    clock.tick(60)
#stage 1
while not crashed:
    if reset and lives >= 1: #variable to reset posistions of things
        time.sleep(2)
        x = (display_width * 0.45)
        y = (display_height * 0.8)
        x_change = 0
        y_change = 0
        bullx = 100000
        bully = 384724
        bully_change = 0
        bullet_state = True
        e1bullx = 93174
        e1bully = 32942
        e1bull_state = False
        e1bully_change = 0
        e2bullx = 23894
        e2bully = 72384
        e3bullx = 23475
        e3bully = 27945
        e4bullx = 83492
        e4bully = 23792
        e5bullx = 27398
        e5bully = 28934
        # other stuff
        invader1right = True
        invader1left = False
        movedown = False
        timer1 = 0
        timer2 = 0
        timer3 = 0
        timer4 = 0
        timer5 = 0
        timer6 = 0
        timer7 = 0
        timerdown = 0
        e2bull_state = False
        e3bull_state = False
        e4bull_state = False
        e5bull_state = False
        sprite_timer = 0
        score = 0
        reset = False
    for event in pygame.event.get(): #main loop
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x_change = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state:
                    timer2 = 0
                    bullet_state = False
                    bully = y
                    bully_change = -10
                if not bullet_state:
                    if bully < 1 or timer2 > 30:
                        bully = 93848
                        bullet_state = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_a or pygame.K_d:
                x_change = 0
    if bullet_state:
        bullx = x
    if lives == 2:
        livesImg = pygame.image.load('lives2.png')
    if lives == 1:
        livesImg = pygame.image.load('lives3.png')
    if lives == 0:
        gmy = 200
        gmx = 300
        invader1_6y = -829034
        invader1_1y = -237894
        invader2_1y = -283940
        invader3y = -82355
        invader4y = -28390
        invader5y = -28390
        deathtimer += 1
    if deathtimer == 500: #waits 500 ticks to end the loop
        crashed = True
    if e1bull_state and row1_count > 1:
        timer3 = 0
        e1bullx = random.randint(50, 650)
        e1bully = invader1_1y
        e1bully_change = 10
        e1bull_state = False
    if not e1bull_state:
        if timer3 > 240 and e1bully > 500:
            e1bull_state = True
    if timer8 > 1000:
        goacross = True
        invaderfreex = 0
        invaderfreey = invader1_1y - 50
    if freeinvadercol(invaderfreex, invaderfreey, bullx, bully):
        invaderfreex = 92742
        score += random.randint(100, 200)
    if goacross: #thing for the ufo that gives a lotta points
        invaderfreex_change = 2.5
        timer8 = 0
    if invaderfreex > 700:
        goacross = False
    if e2bull_state and row2_count > 1:
        timer4 = 0
        e2bullx = random.randint(50, 650)
        e2bully = invader2_1y
        e1bully_change = 10
        e2bull_state = False
    if not e2bull_state:
        if timer4 > 360 and e2bully > 500:
            e2bull_state = True
    if e3bull_state and row3_count > 1:
        timer5 = 0
        e3bullx = random.randint(50, 650)
        e3bully = invader3y
        e1bully_change = 10
        e3bull_state = False
    if not e3bull_state:
        if timer5 > 300 and e3bully > 500:
            e3bull_state = True
    if e4bull_state and row4_count > 1:
        e4bull_state = False
        timer6 = 0
        e4bullx = random.randint(50, 650)
        e4bully = invader4y
        e1bully_change = 10
    if not e4bull_state:
        if timer6 > 300 and e4bully > 500:
            e4bull_state = True
    if e5bull_state and row5_count > 1:
        e5bull_state = False
        timer7 = 0
        e5bullx = random.randint(50, 650)
        e5bully = invader5y
        e1bully_change = 10
    if not e5bull_state:
        if timer7 > 300 and e5bully > 500:
            e5bull_state = True
    if invader1right: #if the invaders should move right
        if timer1 > 50:
            invader1_6x_change = 10
            timer1 = 0
        else:
            invader1_6x_change = 0
    if invader1right:
        if invisx2 > 685:
            movedown = True
            invader1right = False
            invader1left = True
    if movedown: #if the invaders should move down
        invader1_6x_change = 0
        timerdown += 1
        invader1_6y_change = 10
        if timerdown > 1:
            timerdown = 0
            invader1_6y_change = 0
            movedown = False
    if invader1left: #if the invaders should move left
        if timer1 > 60:
            invader1_6x_change = -10
            timer1 = 0
        else:
            invader1_6x_change = 0
    if invader1left:
        if invisx < 20:
            movedown = True
            invader1right = True
            invader1left = False
    #shield collision with player bullets(the player can destroy his/her shields)
    if shieldbullcol(shield1x, shieldy, bullx, bully):
        shield1_status -= 1 #shields dont last forever!
        bully = 47921
        bullet_state = False
    if shieldbullcol2(shield2x, shieldy, bullx, bully):
        shield2_status -= 1
        bully = 47921
        bullet_state = False
    if shieldbullcol3(shield3x, shieldy, bullx, bully):
        shield3_status -= 1
        bully = 47921
        bullet_state = False
    if shieldbullcol4(shield4x, shieldy, bullx, bully):
        shield4_status -= 1
        bully = 47921
        bullet_state = False
    #shield 1 col(with enemy bullets)
    if shield1col(shield1x, shieldy, e1bullx, e1bully):
        shield1_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield1col2(shield1x, shieldy, e2bullx, e2bully):
        shield1_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield1col3(shield1x, shieldy, e3bullx, e3bully):
        shield1_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield1col4(shield1x, shieldy, e4bullx, e4bully):
        shield1_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield1col5(shield1x, shieldy, e5bullx, e5bully):
        shield1_status -= 1
        e15ully = 791345
        e5bull_state = False
    if shield1_status == 5: #sprite changing
        shield1Img = pygame.image.load('shield1.png')
    if shield1_status == 3:
        shield1Img = pygame.image.load('shield2.png')
    if shield1_status == 2:
        shield1Img = pygame.image.load('shield3.png')
    if shield1_status == 0:
        shield1x = 3279
    #shield 2 col
    if shield2col(shield2x, shieldy, e1bullx, e1bully):
        shield2_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield2col2(shield2x, shieldy, e2bullx, e2bully):
        shield2_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield2col3(shield2x, shieldy, e3bullx, e3bully):
        shield2_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield2col4(shield2x, shieldy, e4bullx, e4bully):
        shield2_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield2col5(shield2x, shieldy, e5bullx, e5bully):
        shield2_status -= 1
        e5bully = 791345
        e5bull_state = False
    if shield2_status == 5:
        shield2Img = pygame.image.load('shield1.png')
    if shield2_status == 3:
        shield2Img = pygame.image.load('shield2.png')
    if shield2_status == 2:
        shield2Img = pygame.image.load('shield3.png')
    if shield2_status == 0:
        shield2x = 3279
    #shield 3 col
    if shield3col(shield3x, shieldy, e1bullx, e1bully):
        shield3_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield3col2(shield3x, shieldy, e2bullx, e2bully):
        shield3_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield3col3(shield3x, shieldy, e3bullx, e3bully):
        shield3_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield3col4(shield3x, shieldy, e4bullx, e4bully):
        shield3_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield3col5(shield3x, shieldy, e5bullx, e5bully):
        shield3_status -= 1
        e5bully = 791345
        e5bull_state = False
    if shield3_status == 5:
        shield3Img = pygame.image.load('shield1.png')
    if shield3_status == 3:
        shield3Img = pygame.image.load('shield2.png')
    if shield3_status == 2:
        shield3Img = pygame.image.load('shield3.png')
    if shield3_status == 0:
        shield3x = 3279
    #shield 4 col
    if shield4col(shield4x, shieldy, e1bullx, e1bully):
        shield4_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield4col2(shield4x, shieldy, e2bullx, e2bully):
        shield4_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield4col3(shield4x, shieldy, e3bullx, e3bully):
        shield4_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield4col4(shield4x, shieldy, e4bullx, e4bully):
        shield4_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield4col5(shield4x, shieldy, e5bullx, e5bully):
        shield4_status -= 1
        e5bully = 791345
        e5bull_state = False
    if shield4_status == 5:
        shield4Img = pygame.image.load('shield1.png')
    if shield4_status == 3:
        shield4Img = pygame.image.load('shield2.png')
    if shield4_status == 2:
        shield4Img = pygame.image.load('shield3.png')
    if shield4_status == 0:
        shield4x = 3279
    if sprite_timer > 120: #sprite changing for invaders
        invader1Img = pygame.image.load('invaderrow1_2.png')
        invader2Img = pygame.image.load('invaderrow2_2.png')
        invader3Img = pygame.image.load('invaderrow4_2.png')
    if sprite_timer > 240:
        invader1Img = pygame.image.load('invaderrow1.png')
        invader2Img = pygame.image.load('invaderrow2.png')
        invader3Img = pygame.image.load('invaderrow4.png')
        sprite_timer = 0
    #if player gets hit by bullets
    if playercol(x, y, e1bullx, e1bully):
        x = 28523 #makes the player disapear
        lives -= 1 #subtracts a life
        reset = True #resets coords and etc.
    if playercol2(x, y, e2bullx, e2bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol3(x, y, e3bullx, e3bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol4(x, y, e4bullx, e4bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol5(x, y, e5bullx, e5bully):
        x = 28523
        lives -= 1
        reset = True
    #row 1 collision
    if timer9 > 5:
        ey = 327984
        ex = 283945
    if invader1_1col(bullx, bully, invader1_1x, invader1_1y) and not invader2_1col(bullx, bully, invader2_1x, invader1_1y):
        timer9 = 0 #sets timer 9 to 0
        ex = invader1_1x #sets explosions sprite to equal pos of invader
        ey = invader1_1y
        invader1_1x = 8748459 #makes invader disappear
        score += 30 #adds to the score
        row1_count -= 1 #subtracts from the row count
    if invader1_2col(bullx, bully, invader1_2x, invader1_1y) and not invader2_2col(bullx, bully, invader2_2x, invader1_1y):
        timer9 = 0
        ex = invader1_2x
        ey = invader1_1y
        invader1_2x = 3829034
        score += 30
        row1_count -= 1
    if invader1_3col(bullx, bully, invader1_3x, invader1_1y) and not invader2_3col(bullx, bully, invader2_3x, invader1_1y):
        timer9 = 0
        ex = invader1_3x
        ey = invader1_1y
        invader1_3x = 823942
        score += 30
        row1_count -= 1
    if invader1_4col(bullx, bully, invader1_4x, invader1_1y) and not invader2_4col(bullx, bully, invader2_4x, invader1_1y):
        timer9 = 0
        ex = invader1_4x
        ey = invader1_1y
        invader1_4x = 823424
        score += 30
        row1_count -= 1
    if invader1_5col(bullx, bully, invader1_5x, invader1_1y) and not invader2_5col(bullx, bully, invader2_5x, invader1_1y):
        timer9 = 0
        ex = invader1_5x
        ey = invader1_1y
        invader1_5x = 284197
        score += 30
        row1_count -= 1
    if invader1_6col(bullx, bully, invader1_6realx, invader1_1y) and not invader2_6col(bullx, bully, invader2_6x, invader1_1y):
        timer9 = 0
        ex = invader1_6realx
        ey = invader1_1y
        invader1_6realx = 832904
        score += 30
        row1_count -= 1
    if invader1_7col(bullx, bully, invader1_7x, invader1_1y) and not invader2_7col(bullx, bully, invader2_7x, invader1_1y):
        timer9 = 0
        ex = invader1_7x
        ey = invader1_1y
        invader1_7x = 829348
        score += 30
        row1_count -= 1
    if invader1_8col(bullx, bully, invader1_8x, invader1_1y) and not invader2_8col(bullx, bully, invader2_8x, invader1_1y):
        timer9 = 0
        ex = invader1_8x
        ey = invader1_1y
        invader1_8x = 823442
        score += 30
        row1_count -= 1
    if invader1_9col(bullx, bully, invader1_9x, invader1_1y) and not invader2_9col(bullx, bully, invader2_9x, invader1_1y):
        timer9 = 0
        ex = invader1_9x
        ey = invader1_1y
        invader1_9x = 384234
        score += 30
        row1_count -= 1
    if invader1_10col(bullx, bully, invader1_10x, invader1_1y) and not invader2_10col(bullx, bully, invader2_10x, invader1_1y):
        timer9 = 0
        ex = invader1_10x
        ey = invader1_1y
        invader1_10x = 817234
        score += 30
        row1_count -= 1
    if invader1_11col(bullx, bully, invader1_6x, invader1_1y) and not invader2_11col(bullx, bully, invader2_11x, invader1_1y):
        timer9 = 0
        ex = invader1_6x
        ey = invader1_1y
        invader1_6x = 234984
        score += 30
        row1_count -= 1
    #row 2 collsion
    if invader2_1col(bullx, bully, invader2_1x, invader2_1y) and not invader3_1col(bullx, bully, invader3_1x, invader3y):
        timer9 = 0
        ex = invader2_1x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_1x = 3284533
    if invader2_2col(bullx, bully, invader2_2x, invader2_1y) and not invader3_2col(bullx, bully, invader3_2x, invader3y):
        timer9 = 0
        ex = invader2_2x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_2x = -23404
    if invader2_3col(bullx, bully, invader2_3x, invader2_1y) and not invader3_3col(bullx, bully, invader3_3x, invader3y):
        timer9 = 0
        ex = invader2_3x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_3x = -22345
    if invader2_4col(bullx, bully, invader2_4x, invader2_1y) and not invader3_4col(bullx, bully, invader3_4x, invader3y):
        timer9 = 0
        ex = invader2_4x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_4x = -23245
    if invader2_5col(bullx, bully, invader2_5x, invader2_1y) and not invader3_5col(bullx, bully, invader3_5x, invader3y):
        timer9 = 0
        ex = invader2_5x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_5x = -32459
    if invader2_6col(bullx, bully, invader2_6x, invader2_1y) and not invader3_6col(bullx, bully, invader3_6x, invader3y):
        timer9 = 0
        ex = invader2_6x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_6x = -23895
    if invader2_7col(bullx, bully, invader2_7x, invader2_1y) and not invader3_7col(bullx, bully, invader3_7x, invader3y):
        timer9 = 0
        ex = invader2_7x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_7x = -29542
    if invader2_8col(bullx, bully, invader2_8x, invader2_1y) and not invader3_8col(bullx, bully, invader3_8x, invader3y):
        timer9 = 0
        ex = invader2_8x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_8x = -24359
    if invader2_9col(bullx, bully, invader2_9x, invader2_1y) and not invader3_9col(bullx, bully, invader3_9x, invader3y):
        timer9 = 0
        ex = invader2_9x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_9x = -24580
    if invader2_10col(bullx, bully, invader2_10x, invader2_1y) and not invader3_10col(bullx, bully, invader3_10x, invader3y):
        timer9 = 0
        ex = invader2_10x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_10x = -34652
    if invader2_11col(bullx, bully, invader2_11x, invader2_1y) and not invader3_11col(bullx, bully, invader3_11x, invader3y):
        timer9 = 0
        ex = invader2_11x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_11x = -81732
    if invader3_1col(bullx, bully, invader3_1x, invader3y) and not invader4_1col(bullx, bully, invader4_1x, invader4y):
        timer9 = 0
        ex = invader3_1x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_1x = -82345
    if invader3_2col(bullx, bully, invader3_2x, invader3y) and not invader4_2col(bullx, bully, invader4_2x, invader4y):
        timer9 = 0
        ex = invader3_2x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_2x = -84342
    if invader3_3col(bullx, bully, invader3_3x, invader3y) and not invader4_3col(bullx, bully, invader4_4x, invader4y):
        timer9 = 0
        ex = invader3_2x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_3x = -82345
    if invader3_4col(bullx, bully, invader3_4x, invader3y) and not invader4_4col(bullx, bully, invader4_5x, invader4y):
        timer9 = 0
        ex = invader3_3x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_4x = -82345
    if invader3_5col(bullx, bully, invader3_5x, invader3y) and not invader4_5col(bullx, bully, invader4_6x, invader4y):
        timer9 = 0
        ex = invader3_4x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_5x = -82345
    if invader3_6col(bullx, bully, invader3_6x, invader3y) and not invader4_6col(bullx, bully, invader4_7x, invader4y):
        timer9 = 0
        ex = invader3_5x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_6x = -82345
    if invader3_7col(bullx, bully, invader3_7x, invader3y) and not invader4_7col(bullx, bully, invader4_8x, invader4y):
        timer9 = 0
        ex = invader3_6x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_7x = -82345
    if invader3_8col(bullx, bully, invader3_8x, invader3y) and not invader4_8col(bullx, bully, invader4_9x, invader4y):
        timer9 = 0
        ex = invader3_7x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_8x = -82345
    if invader3_9col(bullx, bully, invader3_9x, invader3y) and not invader4_9col(bullx, bully, invader4_10x, invader4y):
        timer9 = 0
        ex = invader3_9x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_9x = -82345
    if invader3_10col(bullx, bully, invader3_10x, invader3y) and not invader4_10col(bullx, bully, invader4_10x, invader4y):
        timer9 = 0
        ex = invader3_10x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_10x = -82345
    if invader3_11col(bullx, bully, invader3_11x, invader3y) and not invader4_11col(bullx, bully, invader4_11x, invader4y):
        timer9 = 0
        ex = invader3_11x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_11x = -82345
    if invader4_1col(bullx, bully, invader4_1x, invader4y) and not invader5_1col(bullx, bully, invader5_1x, invader5y):
        timer9 = 0
        ex = invader4_1x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_1x = -82345
    if invader4_2col(bullx, bully, invader4_2x, invader4y) and not invader5_2col(bullx, bully, invader5_2x, invader5y):
        timer9 = 0
        ex = invader4_2x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_2x = -82345
    if invader4_3col(bullx, bully, invader4_3x, invader4y) and not invader5_3col(bullx, bully, invader5_3x, invader5y):
        timer9 = 0
        ex = invader4_3x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_3x = -82345
    if invader4_4col(bullx, bully, invader4_4x, invader4y) and not invader5_4col(bullx, bully, invader5_4x, invader5y):
        timer9 = 0
        ex = invader4_4x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_4x = -82345
    if invader4_5col(bullx, bully, invader4_5x, invader4y) and not invader5_5col(bullx, bully, invader5_5x, invader5y):
        timer9 = 0
        ex = invader4_5x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_5x = -82345
    if invader4_6col(bullx, bully, invader4_6x, invader4y) and not invader5_6col(bullx, bully, invader5_6x, invader5y):
        timer9 = 0
        ex = invader4_6x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_6x = -82345
    if invader4_7col(bullx, bully, invader4_7x, invader4y) and not invader5_7col(bullx, bully, invader5_7x, invader5y):
        timer9 = 0
        ex = invader4_7x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_7x = -82345
    if invader4_8col(bullx, bully, invader4_8x, invader4y) and not invader5_8col(bullx, bully, invader5_8x, invader5y):
        timer9 = 0
        ex = invader4_8x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_8x = -82345
    if invader4_9col(bullx, bully, invader4_9x, invader4y) and not invader5_9col(bullx, bully, invader5_9x, invader5y):
        timer9 = 0
        ex = invader4_9x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_9x = -82345
    if invader4_10col(bullx, bully, invader4_10x, invader4y) and not invader5_10col(bullx, bully, invader5_10x, invader5y):
        timer9 = 0
        ex = invader4_10x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_10x = -82345
    if invader4_11col(bullx, bully, invader4_11x, invader4y) and not invader5_11col(bullx, bully, invader5_11x, invader5y):
        timer9 = 0
        ex = invader4_11x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_11x = -82345
    if invader5_1col(bullx, bully, invader5_1x, invader5y):
        timer9 = 0
        ex = invader5_1x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_1x = -82345
    if invader5_2col(bullx, bully, invader5_2x, invader5y):
        timer9 = 0
        ex = invader5_2x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_2x = -82345
    if invader5_3col(bullx, bully, invader5_3x, invader5y):
        timer9 = 0
        ex = invader5_3x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_3x = -82345
    if invader5_4col(bullx, bully, invader5_4x, invader5y):
        timer9 = 0
        ex = invader5_4x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_4x = -82345
    if invader5_5col(bullx, bully, invader5_5x, invader5y):
        timer9 = 0
        ex = invader5_5x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_5x = -82345
    if invader5_6col(bullx, bully, invader5_6x, invader5y):
        timer9 = 0
        ex = invader5_6x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_6x = -82345
    if invader5_7col(bullx, bully, invader5_7x, invader5y):
        timer9 = 0
        ex = invader5_7x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_7x = -82345
    if invader5_8col(bullx, bully, invader5_8x, invader5y):
        timer9 = 0
        ex = invader5_8x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_8x = -82345
    if invader5_9col(bullx, bully, invader5_9x, invader5y):
        timer9 = 0
        ex = invader5_9x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_9x = -82345
    if invader5_10col(bullx, bully, invader5_10x, invader5y):
        timer9 = 0
        ex = invader5_10x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_10x = -82345
    if invader5_11col(bullx, bully, invader5_11x, invader5y):
        timer9 = 0
        ex = invader5_11x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        sety = True
        bully = 82394
        bully_change = 10
        invader5_11x = -82345
    if transition(row1_count, row2_count, row3_count, row4_count, row5_count):
        crashed = True
        stage2 = True
    #display updating and stuff
    x += x_change
    timer1 += 1 #<-- timers!
    timer2 += 1
    timer3 += 1
    timer4 += 1
    timer5 += 1
    timer6 += 1
    timer7 += 1
    timer8 += 1
    timer9 += 1
    sprite_timer += 1
    #x and y changing
    invisx += invader1_6x_change
    invisx2 += invader1_6x_change
    invader1_6x += invader1_6x_change
    invader1_6y += invader1_6y_change
    invader1_1x += invader1_6x_change
    invader1_1y += invader1_6y_change
    invader1_2x += invader1_6x_change
    invader1_3x += invader1_6x_change
    invader1_4x += invader1_6x_change
    invader1_5x += invader1_6x_change
    invader1_6realx += invader1_6x_change
    invader1_7x += invader1_6x_change
    invader1_8x += invader1_6x_change
    invader1_9x += invader1_6x_change
    invader1_10x += invader1_6x_change
    invader2_1y += invader1_6y_change
    invader2_1x += invader1_6x_change
    invader2_2x += invader1_6x_change
    invader2_3x += invader1_6x_change
    invader2_4x += invader1_6x_change
    invader2_5x += invader1_6x_change
    invader2_6x += invader1_6x_change
    invader2_7x += invader1_6x_change
    invader2_8x += invader1_6x_change
    invader2_9x += invader1_6x_change
    invader2_10x += invader1_6x_change
    invader2_11x += invader1_6x_change
    invader3y += invader1_6y_change
    invader3_1x += invader1_6x_change
    invader3_2x += invader1_6x_change
    invader3_3x += invader1_6x_change
    invader3_4x += invader1_6x_change
    invader3_5x += invader1_6x_change
    invader3_6x += invader1_6x_change
    invader3_7x += invader1_6x_change
    invader3_8x += invader1_6x_change
    invader3_9x += invader1_6x_change
    invader3_10x += invader1_6x_change
    invader3_11x += invader1_6x_change
    invader4_1x += invader1_6x_change
    invader4_2x += invader1_6x_change
    invader4_3x += invader1_6x_change
    invader4_4x += invader1_6x_change
    invader4_5x += invader1_6x_change
    invader4_6x += invader1_6x_change
    invader4_7x += invader1_6x_change
    invader4_8x += invader1_6x_change
    invader4_9x += invader1_6x_change
    invader4_10x += invader1_6x_change
    invader4_11x += invader1_6x_change
    invader4y += invader1_6y_change
    invader5_1x += invader1_6x_change
    invader5_2x += invader1_6x_change
    invader5_3x += invader1_6x_change
    invader5_4x += invader1_6x_change
    invader5_5x += invader1_6x_change
    invader5_6x += invader1_6x_change
    invader5_7x += invader1_6x_change
    invader5_8x += invader1_6x_change
    invader5_9x += invader1_6x_change
    invader5_10x += invader1_6x_change
    invader5_11x += invader1_6x_change
    invader5y += invader1_6y_change
    ex += invader1_6x_change
    ey += invader1_6y_change
    e1bully += e1bully_change
    e2bully += e1bully_change
    e3bully += e1bully_change
    e4bully += e1bully_change
    e5bully += e1bully_change
    invaderfreex += invaderfreex_change
    bully += bully_change
    #display color filling
    gameDisplay.fill(black)
    #utilization of the .blit functions
    invader1_6(invader1_6x, invader1_6y)
    invader1_1(invader1_1x, invader1_1y)
    invader1_2(invader1_2x, invader1_1y)
    invader1_3(invader1_3x, invader1_1y)
    invader1_4(invader1_4x, invader1_1y)
    invader1_5(invader1_5x, invader1_1y)
    invader1_6real(invader1_6realx, invader1_1y)
    invader1_7(invader1_7x, invader1_1y)
    invader1_8(invader1_8x, invader1_1y)
    invader1_9(invader1_9x, invader1_1y)
    invader1_10(invader1_10x, invader1_1y)
    invader2_1(invader2_1x, invader2_1y)
    invader2_2(invader2_2x, invader2_1y)
    invader2_3(invader2_3x, invader2_1y)
    invader2_4(invader2_4x, invader2_1y)
    invader2_5(invader2_5x, invader2_1y)
    invader2_6(invader2_6x, invader2_1y)
    invader2_7(invader2_7x, invader2_1y)
    invader2_8(invader2_8x, invader2_1y)
    invader2_9(invader2_9x, invader2_1y)
    invader2_10(invader2_10x, invader2_1y)
    invader2_11(invader2_11x, invader2_1y)
    invader3_1(invader3_1x, invader3y)
    invader3_2(invader3_2x, invader3y)
    invader3_3(invader3_3x, invader3y)
    invader3_4(invader3_4x, invader3y)
    invader3_5(invader3_5x, invader3y)
    invader3_6(invader3_6x, invader3y)
    invader3_7(invader3_7x, invader3y)
    invader3_8(invader3_8x, invader3y)
    invader3_9(invader3_9x, invader3y)
    invader3_10(invader3_10x, invader3y)
    invader3_11(invader3_11x, invader3y)
    invader4_1(invader4_1x, invader4y)
    invader4_2(invader4_2x, invader4y)
    invader4_3(invader4_3x, invader4y)
    invader4_4(invader4_4x, invader4y)
    invader4_5(invader4_5x, invader4y)
    invader4_6(invader4_6x, invader4y)
    invader4_7(invader4_7x, invader4y)
    invader4_8(invader4_8x, invader4y)
    invader4_9(invader4_9x, invader4y)
    invader4_10(invader4_10x, invader4y)
    invader4_11(invader4_11x, invader4y)
    invader5_1(invader5_1x, invader5y)
    invader5_2(invader5_2x, invader5y)
    invader5_3(invader5_3x, invader5y)
    invader5_4(invader5_4x, invader5y)
    invader5_5(invader5_5x, invader5y)
    invader5_6(invader5_6x, invader5y)
    invader5_7(invader5_7x, invader5y)
    invader5_8(invader5_8x, invader5y)
    invader5_9(invader5_9x, invader5y)
    invader5_10(invader5_10x, invader5y)
    invader5_11(invader5_11x, invader5y)
    invaderfree(invaderfreex, invaderfreey)
    explosion(ex, ey)
    enem1bull(e1bullx, e1bully)
    enem2bull(e2bullx, e2bully)
    enem3bull(e3bullx, e2bully)
    enem5bull(e5bullx, e5bully)
    shield1(shield1x, shieldy)
    shield2(shield2x, shieldy)
    shield3(shield3x, shieldy)
    shield4(shield4x, shieldy)
    livessprite(livex, livey)
    #i had problems with showing score so i put the function here instead of a "def" thing
    score_show = font.render("Score: " + str(score), True ,(white))
    gameDisplay.blit(score_show, (textX, textY))
    gameover(gmx, gmy)
    player(x, y)
    bullet(bullx, bully)
    #display updates
    pygame.display.update()
    #fps
    clock.tick(60)
prevscore = score #<-- sets the previous score to the score
if stage2: #<---- not much is changed here compared to stage 1. There will be less dev notes here.
    invisx = 50
    invisx2 = 650
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    bullx = 100000
    bully = 384724
    bully_change = 0
    bullet_state = True
    e1bullx = 93174
    e1bully = 32942
    e1bull_state = False
    e1bully_change = 0
    e2bullx = 23894
    e2bully = 72384
    e3bullx = 23475
    e3bully = 27945
    e4bullx = 83492
    e4bully = 23792
    e5bullx = 27398
    e5bully = 28934
    # invader coords and movement pattern
    invader1_6x = 650
    invader1_6y = 20
    invader1_6x_change = 0  # <-- universal x and y changers
    invader1_6y_change = 0  # <--(i did name them for row one, colunm 6 but i didnt feel like changing it)
    invader1_1x = 50
    invader1_1y = 20  # <-- random idea change making the this y the universal y
    invader1_2x = 110
    invader1_3x = 170
    invader1_4x = 230
    invader1_5x = 290
    invader1_6realx = 350
    invader1_7x = 410
    invader1_8x = 470
    invader1_9x = 530
    invader1_10x = 590
    # row 2 invaders
    invader2_1y = 70
    invader2_1x = invader1_1x
    invader2_2x = invader1_2x
    invader2_3x = invader1_3x
    invader2_4x = invader1_4x
    invader2_5x = invader1_5x
    invader2_6x = invader1_6realx
    invader2_7x = invader1_7x
    invader2_8x = invader1_8x
    invader2_9x = invader1_9x
    invader2_10x = invader1_10x
    invader2_11x = invader1_6x
    # row 3 invaders
    invader3y = 120
    invader3_1x = invader2_1x
    invader3_2x = invader2_2x
    invader3_3x = invader2_3x
    invader3_4x = invader2_4x
    invader3_5x = invader2_5x
    invader3_6x = invader2_6x
    invader3_7x = invader2_7x
    invader3_8x = invader2_8x
    invader3_9x = invader2_9x
    invader3_10x = invader2_10x
    invader3_11x = invader2_11x
    # row 4 invader pos
    invader4y = 165
    invader4_1x = invader3_1x
    invader4_2x = invader3_2x
    invader4_3x = invader3_3x
    invader4_4x = invader3_4x
    invader4_5x = invader3_5x
    invader4_6x = invader3_6x
    invader4_7x = invader3_7x
    invader4_8x = invader3_8x
    invader4_9x = invader3_9x
    invader4_10x = invader3_10x
    invader4_11x = invader3_11x
    # row 5 invader pos
    invader5y = 210
    invader5_1x = invader4_1x
    invader5_2x = invader4_2x
    invader5_3x = invader4_3x
    invader5_4x = invader4_4x
    invader5_5x = invader4_5x
    invader5_6x = invader4_6x
    invader5_7x = invader4_7x
    invader5_8x = invader4_8x
    invader5_9x = invader4_9x
    invader5_10x = invader4_10x
    invader5_11x = invader4_11x
    # other stuff
    invader1right = True
    invader1left = False
    movedown = False
    timer1 = 0
    timer2 = 0
    timer3 = 0
    timer4 = 0
    timer5 = 0
    timer6 = 0
    timer7 = 0
    timerdown = 0
    e2bull_state = False
    e3bull_state = False
    e4bull_state = False
    e5bull_state = False
    row1_count = 11
    row2_count = 11
    row3_count = 11
    row4_count = 11
    row5_count = 11
    shield1x = 100
    shieldy = 400
    shield2x = 250
    shield3x = 500
    shield4x = 650
    shield1_status = 5
    shield2_status = 5
    shield3_status = 5
    shield4_status = 5
    sprite_timer = 0
    reset = False
    gmx = 400
    gmy = 23453
    deathtimer = 0
    livex = 600
    livey = -40
    score = 0
    font = pygame.font.Font('8bit.ttf', 22)
    textX = 10
    textY = 10
    timer8 = 0
    score = prevscore
    reset = True
while stage2:
    if reset and lives >= 1:
        time.sleep(2)
        x = (display_width * 0.45)
        y = (display_height * 0.8)
        x_change = 0
        y_change = 0
        bullx = 100000
        bully = 384724
        bully_change = 0
        bullet_state = True
        e1bullx = 93174
        e1bully = 32942
        e1bull_state = False
        e1bully_change = 0
        e2bullx = 23894
        e2bully = 72384
        e3bullx = 23475
        e3bully = 27945
        e4bullx = 83492
        e4bully = 23792
        e5bullx = 27398
        e5bully = 28934
        # other stuff
        invader1right = True
        invader1left = False
        movedown = False
        timer1 = 0
        timer2 = 0
        timer3 = 0
        timer4 = 0
        timer5 = 0
        timer6 = 0
        timer7 = 0
        timerdown = 0
        e2bull_state = False
        e3bull_state = False
        e4bull_state = False
        e5bull_state = False
        sprite_timer = 0
        score = prevscore
        reset = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage2 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x_change = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state:
                    timer2 = 0
                    bullet_state = False
                    bully = y
                    bully_change = -10
                if not bullet_state:
                    if bully < 1 or timer2 > 60:
                        bully = 93848
                        bullet_state = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_a or pygame.K_d:
                x_change = 0
    if timer8 > 1000:
        goacross = True
        invaderfreex = 0
        invaderfreey = invader1_1y - 50
    if goacross:
        invaderfreex_change = 2.5
        timer8 = 0
    if invaderfreex > 700:
        goacross = False
    if freeinvadercol(invaderfreex, invaderfreey, bullx, bully):
        invaderfreex = 92742
        score += random.randint(100, 200)
    if bullet_state:
        bullx = x
    if lives == 2:
        livesImg = pygame.image.load('lives2.png')
    if lives == 1:
        livesImg = pygame.image.load('lives3.png')
    if lives == 0:
        gmy = 200
        gmx = 300
        invader1_6y = -829034
        invader1_1y = -237894
        invader2_1y = -283940
        invader3y = -82355
        invader4y = -28390
        invader5y = -28390
        deathtimer += 1
    if deathtimer == 500:
        crashed = True
    if e1bull_state and row1_count > 1:
        timer3 = 0
        e1bullx = random.randint(50, 650)
        e1bully = invader1_1y
        e1bully_change = 10
        e1bull_state = False
    if not e1bull_state:
        if timer3 > 120 and e1bully > 500:
            e1bull_state = True
    if e2bull_state and row2_count > 1:
        timer4 = 0
        e2bullx = random.randint(50, 650)
        e2bully = invader2_1y
        e1bully_change = 10
        e2bull_state = False
    if not e2bull_state:
        if timer4 > 180 and e2bully > 500:
            e2bull_state = True
    if e3bull_state and row3_count > 1:
        timer5 = 0
        e3bullx = random.randint(50, 650)
        e3bully = invader3y
        e1bully_change = 10
        e3bull_state = False
    if not e3bull_state:
        if timer5 > 150 and e3bully > 500:
            e3bull_state = True
    if e4bull_state and row4_count > 1:
        e4bull_state = False
        timer6 = 0
        e4bullx = random.randint(50, 650)
        e4bully = invader4y
        e1bully_change = 10
    if not e4bull_state:
        if timer6 > 150 and e4bully > 500:
            e4bull_state = True
    if e5bull_state and row5_count > 1:
        e5bull_state = False
        timer7 = 0
        e5bullx = random.randint(50, 650)
        e5bully = invader5y
        e1bully_change = 10
    if not e5bull_state:
        if timer7 > 150 and e5bully > 500:
            e5bull_state = True
    if invader1right:
        if timer1 > 50:
            invader1_6x_change = 10
            timer1 = 0
        else:
            invader1_6x_change = 0
    if invader1right:
        if invisx2 > 685:
            movedown = True
            invader1right = False
            invader1left = True
    if movedown:
        invader1_6x_change = 0
        timerdown += 1
        invader1_6y_change = 10
        if timerdown > 1:
            timerdown = 0
            invader1_6y_change = 0
            movedown = False
    if invader1left:
        if timer1 > 60:
            invader1_6x_change = -10
            timer1 = 0
        else:
            invader1_6x_change = 0
    if invader1left:
        if invisx < 20:
            movedown = True
            invader1right = True
            invader1left = False
    if shieldbullcol(shield1x, shieldy, bullx, bully):
        shield1_status -= 1
        bully = 47921
        bullet_state = False
    if shieldbullcol2(shield2x, shieldy, bullx, bully):
        shield2_status -= 1
        bully = 47921
        bullet_state = False
    if shieldbullcol3(shield3x, shieldy, bullx, bully):
        shield3_status -= 1
        bully = 47921
        bullet_state = False
    if shieldbullcol4(shield4x, shieldy, bullx, bully):
        shield4_status -= 1
        bully = 47921
        bullet_state = False
   #yd98ty9rr
    #shield 1 col
    if shield1col(shield1x, shieldy, e1bullx, e1bully):
        shield1_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield1col2(shield1x, shieldy, e2bullx, e2bully):
        shield1_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield1col3(shield1x, shieldy, e3bullx, e3bully):
        shield1_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield1col4(shield1x, shieldy, e4bullx, e4bully):
        shield1_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield1col5(shield1x, shieldy, e5bullx, e5bully):
        shield1_status -= 1
        e15ully = 791345
        e5bull_state = False
    if shield1_status == 5:
        shield1Img = pygame.image.load('shield1.png')
    if shield1_status == 3:
        shield1Img = pygame.image.load('shield2.png')
    if shield1_status == 2:
        shield1Img = pygame.image.load('shield3.png')
    if shield1_status == 0:
        shield1x = 3279
    #shield 2 col
    if shield2col(shield2x, shieldy, e1bullx, e1bully):
        shield2_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield2col2(shield2x, shieldy, e2bullx, e2bully):
        shield2_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield2col3(shield2x, shieldy, e3bullx, e3bully):
        shield2_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield2col4(shield2x, shieldy, e4bullx, e4bully):
        shield2_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield2col5(shield2x, shieldy, e5bullx, e5bully):
        shield2_status -= 1
        e5bully = 791345
        e5bull_state = False
    if shield2_status == 5:
        shield2Img = pygame.image.load('shield1.png')
    if shield2_status == 3:
        shield2Img = pygame.image.load('shield2.png')
    if shield2_status == 2:
        shield2Img = pygame.image.load('shield3.png')
    if shield2_status == 0:
        shield2x = 3279
    #shield 3 col
    if shield3col(shield3x, shieldy, e1bullx, e1bully):
        shield3_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield3col2(shield3x, shieldy, e2bullx, e2bully):
        shield3_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield3col3(shield3x, shieldy, e3bullx, e3bully):
        shield3_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield3col4(shield3x, shieldy, e4bullx, e4bully):
        shield3_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield3col5(shield3x, shieldy, e5bullx, e5bully):
        shield3_status -= 1
        e5bully = 791345
        e5bull_state = False
    if shield3_status == 5:
        shield3Img = pygame.image.load('shield1.png')
    if shield3_status == 3:
        shield3Img = pygame.image.load('shield2.png')
    if shield3_status == 2:
        shield3Img = pygame.image.load('shield3.png')
    if shield3_status == 0:
        shield3x = 3279
    #shield 4 col
    if shield4col(shield4x, shieldy, e1bullx, e1bully):
        shield4_status -= 1
        e1bully = 791345
        e1bull_state = False
    if shield4col2(shield4x, shieldy, e2bullx, e2bully):
        shield4_status -= 1
        e2bully = 791345
        e2bull_state = False
    if shield4col3(shield4x, shieldy, e3bullx, e3bully):
        shield4_status -= 1
        e3bully = 791345
        e3bull_state = False
    if shield4col4(shield4x, shieldy, e4bullx, e4bully):
        shield4_status -= 1
        e4bully = 791345
        e4bull_state = False
    if shield4col5(shield4x, shieldy, e5bullx, e5bully):
        shield4_status -= 1
        e5bully = 791345
        e5bull_state = False
    if shield4_status == 5:
        shield4Img = pygame.image.load('shield1.png')
    if shield4_status == 3:
        shield4Img = pygame.image.load('shield2.png')
    if shield4_status == 2:
        shield4Img = pygame.image.load('shield3.png')
    if shield4_status == 0:
        shield4x = 3279
    if sprite_timer > 120:
        invader1Img = pygame.image.load('invaderrow1_2.png')
        invader2Img = pygame.image.load('invaderrow2_2.png')
        invader3Img = pygame.image.load('invaderrow4_2.png')
    if sprite_timer > 240:
        invader1Img = pygame.image.load('invaderrow1.png')
        invader2Img = pygame.image.load('invaderrow2.png')
        invader3Img = pygame.image.load('invaderrow4.png')
        sprite_timer = 0
    if playercol(x, y, e1bullx, e1bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol2(x, y, e2bullx, e2bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol3(x, y, e3bullx, e3bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol4(x, y, e4bullx, e4bully):
        x = 28523
        lives -= 1
        reset = True
    if playercol5(x, y, e5bullx, e5bully):
        x = 28523
        lives -= 1
        reset = True
    #row 1 collision
    if timer9 > 5:
        ey = 327984
        ex = 283945
    if invader1_1col(bullx, bully, invader1_1x, invader1_1y) and not invader2_1col(bullx, bully, invader2_1x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_1x
        ey = invader1_1y
        invader1_1x = 8748459
        score += 30
        row1_count -= 1
    if invader1_2col(bullx, bully, invader1_2x, invader1_1y) and not invader2_2col(bullx, bully, invader2_2x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_2x
        ey = invader1_1y
        invader1_2x = 3829034
        score += 30
        row1_count -= 1
    if invader1_3col(bullx, bully, invader1_3x, invader1_1y) and not invader2_3col(bullx, bully, invader2_3x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_3x
        ey = invader1_1y
        invader1_3x = 823942
        score += 30
        row1_count -= 1
    if invader1_4col(bullx, bully, invader1_4x, invader1_1y) and not invader2_4col(bullx, bully, invader2_4x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_4x
        ey = invader1_1y
        invader1_4x = 823424
        score += 30
        row1_count -= 1
    if invader1_5col(bullx, bully, invader1_5x, invader1_1y) and not invader2_5col(bullx, bully, invader2_5x,
                                                              invader1_1y):
        timer9 = 0
        ex = invader1_5x
        ey = invader1_1y
        invader1_5x = 284197
        score += 30
        row1_count -= 1
    if invader1_6col(bullx, bully, invader1_6realx, invader1_1y) and not invader2_6col(bullx, bully, invader2_6x,
                                                                                       invader1_1y):
        timer9 = 0
        ex = invader1_6realx
        ey = invader1_1y
        invader1_6realx = 832904
        score += 30
        row1_count -= 1
    if invader1_7col(bullx, bully, invader1_7x, invader1_1y) and not invader2_7col(bullx, bully, invader2_7x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_7x
        ey = invader1_1y
        invader1_7x = 829348
        score += 30
        row1_count -= 1
    if invader1_8col(bullx, bully, invader1_8x, invader1_1y) and not invader2_8col(bullx, bully, invader2_8x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_8x
        ey = invader1_1y
        invader1_8x = 823442
        score += 30
        row1_count -= 1
    if invader1_9col(bullx, bully, invader1_9x, invader1_1y) and not invader2_9col(bullx, bully, invader2_9x,
                                                                                   invader1_1y):
        timer9 = 0
        ex = invader1_9x
        ey = invader1_1y
        invader1_9x = 384234
        score += 30
        row1_count -= 1
    if invader1_10col(bullx, bully, invader1_10x, invader1_1y) and not invader2_10col(bullx, bully, invader2_10x,
                                                                                      invader1_1y):
        timer9 = 0
        ex = invader1_10x
        ey = invader1_1y
        invader1_10x = 817234
        score += 30
        row1_count -= 1
    if invader1_11col(bullx, bully, invader1_6x, invader1_1y) and not invader2_11col(bullx, bully, invader2_11x,
                                                                                     invader1_1y):
        timer9 = 0
        ex = invader1_6x
        ey = invader1_1y
        invader1_6x = 234984
        score += 30
        row1_count -= 1
    # row 2 collsion
    if invader2_1col(bullx, bully, invader2_1x, invader2_1y) and not invader3_1col(bullx, bully, invader3_1x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_1x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_1x = 3284533
    if invader2_2col(bullx, bully, invader2_2x, invader2_1y) and not invader3_2col(bullx, bully, invader3_2x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_2x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_2x = -23404
    if invader2_3col(bullx, bully, invader2_3x, invader2_1y) and not invader3_3col(bullx, bully, invader3_3x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_3x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_3x = -22345
    if invader2_4col(bullx, bully, invader2_4x, invader2_1y) and not invader3_4col(bullx, bully, invader3_4x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_4x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_4x = -23245
    if invader2_5col(bullx, bully, invader2_5x, invader2_1y) and not invader3_5col(bullx, bully, invader3_5x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_5x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_5x = -32459
    if invader2_6col(bullx, bully, invader2_6x, invader2_1y) and not invader3_6col(bullx, bully, invader3_6x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_6x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_6x = -23895
    if invader2_7col(bullx, bully, invader2_7x, invader2_1y) and not invader3_7col(bullx, bully, invader3_7x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_7x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_7x = -29542
    if invader2_8col(bullx, bully, invader2_8x, invader2_1y) and not invader3_8col(bullx, bully, invader3_8x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_8x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_8x = -24359
    if invader2_9col(bullx, bully, invader2_9x, invader2_1y) and not invader3_9col(bullx, bully, invader3_9x,
                                                                                   invader3y):
        timer9 = 0
        ex = invader2_9x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_9x = -24580
    if invader2_10col(bullx, bully, invader2_10x, invader2_1y) and not invader3_10col(bullx, bully, invader3_10x,
                                                                                      invader3y):
        timer9 = 0
        ex = invader2_10x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_10x = -34652
    if invader2_11col(bullx, bully, invader2_11x, invader2_1y) and not invader3_11col(bullx, bully, invader3_11x,
                                                                                      invader3y):
        timer9 = 0
        ex = invader2_11x
        ey = invader2_1y
        bullet_state = False
        score += 20
        row2_count -= 1
        bully = 82394
        bully_change = 10
        invader2_11x = -81732
    if invader3_1col(bullx, bully, invader3_1x, invader3y) and not invader4_1col(bullx, bully, invader4_1x, invader4y):
        timer9 = 0
        ex = invader3_1x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_1x = -82345
    if invader3_2col(bullx, bully, invader3_2x, invader3y) and not invader4_2col(bullx, bully, invader4_2x, invader4y):
        timer9 = 0
        ex = invader3_2x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_2x = -84342
    if invader3_3col(bullx, bully, invader3_3x, invader3y) and not invader4_3col(bullx, bully, invader4_4x, invader4y):
        timer9 = 0
        ex = invader3_2x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_3x = -82345
    if invader3_4col(bullx, bully, invader3_4x, invader3y) and not invader4_4col(bullx, bully, invader4_5x, invader4y):
        timer9 = 0
        ex = invader3_3x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_4x = -82345
    if invader3_5col(bullx, bully, invader3_5x, invader3y) and not invader4_5col(bullx, bully, invader4_6x, invader4y):
        timer9 = 0
        ex = invader3_4x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_5x = -82345
    if invader3_6col(bullx, bully, invader3_6x, invader3y) and not invader4_6col(bullx, bully, invader4_7x, invader4y):
        timer9 = 0
        ex = invader3_5x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_6x = -82345
    if invader3_7col(bullx, bully, invader3_7x, invader3y) and not invader4_7col(bullx, bully, invader4_8x, invader4y):
        timer9 = 0
        ex = invader3_6x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_7x = -82345
    if invader3_8col(bullx, bully, invader3_8x, invader3y) and not invader4_8col(bullx, bully, invader4_9x, invader4y):
        timer9 = 0
        ex = invader3_7x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_8x = -82345
    if invader3_9col(bullx, bully, invader3_9x, invader3y) and not invader4_9col(bullx, bully, invader4_10x, invader4y):
        timer9 = 0
        ex = invader3_9x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_9x = -82345
    if invader3_10col(bullx, bully, invader3_10x, invader3y) and not invader4_10col(bullx, bully, invader4_10x,                                                          invader4y):
        timer9 = 0
        ex = invader3_10x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_10x = -82345
    if invader3_11col(bullx, bully, invader3_11x, invader3y) and not invader4_11col(bullx, bully, invader4_11x,
                                                                                    invader4y):
        timer9 = 0
        ex = invader3_11x
        ey = invader3y
        bullet_state = False
        score += 20
        row3_count -= 1
        bully = 82394
        bully_change = 10
        invader3_11x = -82345
    if invader4_1col(bullx, bully, invader4_1x, invader4y) and not invader5_1col(bullx, bully, invader5_1x, invader5y):
        timer9 = 0
        ex = invader4_1x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_1x = -82345
    if invader4_2col(bullx, bully, invader4_2x, invader4y) and not invader5_2col(bullx, bully, invader5_2x, invader5y):
        timer9 = 0
        ex = invader4_2x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_2x = -82345
    if invader4_3col(bullx, bully, invader4_3x, invader4y) and not invader5_3col(bullx, bully, invader5_3x, invader5y):
        timer9 = 0
        ex = invader4_3x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_3x = -82345
    if invader4_4col(bullx, bully, invader4_4x, invader4y) and not invader5_4col(bullx, bully, invader5_4x, invader5y):
        timer9 = 0
        ex = invader4_4x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_4x = -82345
    if invader4_5col(bullx, bully, invader4_5x, invader4y) and not invader5_5col(bullx, bully, invader5_5x, invader5y):
        timer9 = 0
        ex = invader4_5x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_5x = -82345
    if invader4_6col(bullx, bully, invader4_6x, invader4y) and not invader5_6col(bullx, bully, invader5_6x, invader5y):
        timer9 = 0
        ex = invader4_6x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_6x = -82345
    if invader4_7col(bullx, bully, invader4_7x, invader4y) and not invader5_7col(bullx, bully, invader5_7x, invader5y):
        timer9 = 0
        ex = invader4_7x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_7x = -82345
    if invader4_8col(bullx, bully, invader4_8x, invader4y) and not invader5_8col(bullx, bully, invader5_8x, invader5y):
        timer9 = 0
        ex = invader4_8x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_8x = -82345
    if invader4_9col(bullx, bully, invader4_9x, invader4y) and not invader5_9col(bullx, bully, invader5_9x, invader5y):
        timer9 = 0
        ex = invader4_9x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_9x = -82345
    if invader4_10col(bullx, bully, invader4_10x, invader4y) and not invader5_10col(bullx, bully, invader5_10x,
                                                                                    invader5y):
        timer9 = 0
        ex = invader4_10x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_10x = -82345
    if invader4_11col(bullx, bully, invader4_11x, invader4y) and not invader5_11col(bullx, bully, invader5_11x,
                                                                                    invader5y):
        timer9 = 0
        ex = invader4_11x
        ey = invader4y
        bullet_state = False
        score += 10
        row4_count -= 1
        bully = 82394
        bully_change = 10
        invader4_11x = -82345
    if invader5_1col(bullx, bully, invader5_1x, invader5y):
        timer9 = 0
        ex = invader5_1x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_1x = -82345
    if invader5_2col(bullx, bully, invader5_2x, invader5y):
        timer9 = 0
        ex = invader5_2x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_2x = -82345
    if invader5_3col(bullx, bully, invader5_3x, invader5y):
        timer9 = 0
        ex = invader5_3x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_3x = -82345
    if invader5_4col(bullx, bully, invader5_4x, invader5y):
        timer9 = 0
        ex = invader5_4x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_4x = -82345
    if invader5_5col(bullx, bully, invader5_5x, invader5y):
        timer9 = 0
        ex = invader5_5x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_5x = -82345
    if invader5_6col(bullx, bully, invader5_6x, invader5y):
        timer9 = 0
        ex = invader5_6x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_6x = -82345
    if invader5_7col(bullx, bully, invader5_7x, invader5y):
        timer9 = 0
        ex = invader5_7x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_7x = -82345
    if invader5_8col(bullx, bully, invader5_8x, invader5y):
        timer9 = 0
        ex = invader5_8x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_8x = -82345
    if invader5_9col(bullx, bully, invader5_9x, invader5y):
        timer9 = 0
        ex = invader5_9x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_9x = -82345
    if invader5_10col(bullx, bully, invader5_10x, invader5y):
        timer9 = 0
        ex = invader5_10x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        bully = 82394
        bully_change = 10
        invader5_10x = -82345
    if invader5_11col(bullx, bully, invader5_11x, invader5y):
        timer9 = 0
        ex = invader5_11x
        ey = invader5y
        bullet_state = False
        score += 10
        row5_count -= 1
        sety = True
        bully = 82394
        bully_change = 10
        invader5_11x = -82345
    if transition(row1_count, row2_count, row3_count, row4_count, row5_count):
        stage2 = False
        win = True
    x += x_change
    timer1 += 1
    timer2 += 1
    timer3 += 1
    timer4 += 1
    timer5 += 1
    timer6 += 1
    timer7 += 1
    timer8 += 1
    timer9 += 1
    sprite_timer += 1
    invisx += invader1_6x_change
    invisx2 += invader1_6x_change
    invader1_6x += invader1_6x_change
    invader1_6y += invader1_6y_change
    invader1_1x += invader1_6x_change
    invader1_1y += invader1_6y_change
    invader1_2x += invader1_6x_change
    invader1_3x += invader1_6x_change
    invader1_4x += invader1_6x_change
    invader1_5x += invader1_6x_change
    invader1_6realx += invader1_6x_change
    invader1_7x += invader1_6x_change
    invader1_8x += invader1_6x_change
    invader1_9x += invader1_6x_change
    invader1_10x += invader1_6x_change
    invader2_1y += invader1_6y_change
    invader2_1x += invader1_6x_change
    invader2_2x += invader1_6x_change
    invader2_3x += invader1_6x_change
    invader2_4x += invader1_6x_change
    invader2_5x += invader1_6x_change
    invader2_6x += invader1_6x_change
    invader2_7x += invader1_6x_change
    invader2_8x += invader1_6x_change
    invader2_9x += invader1_6x_change
    invader2_10x += invader1_6x_change
    invader2_11x += invader1_6x_change
    invader3y += invader1_6y_change
    invader3_1x += invader1_6x_change
    invader3_2x += invader1_6x_change
    invader3_3x += invader1_6x_change
    invader3_4x += invader1_6x_change
    invader3_5x += invader1_6x_change
    invader3_6x += invader1_6x_change
    invader3_7x += invader1_6x_change
    invader3_8x += invader1_6x_change
    invader3_9x += invader1_6x_change
    invader3_10x += invader1_6x_change
    invader3_11x += invader1_6x_change
    invader4_1x += invader1_6x_change
    invader4_2x += invader1_6x_change
    invader4_3x += invader1_6x_change
    invader4_4x += invader1_6x_change
    invader4_5x += invader1_6x_change
    invader4_6x += invader1_6x_change
    invader4_7x += invader1_6x_change
    invader4_8x += invader1_6x_change
    invader4_9x += invader1_6x_change
    invader4_10x += invader1_6x_change
    invader4_11x += invader1_6x_change
    invader4y += invader1_6y_change
    invader5_1x += invader1_6x_change
    invader5_2x += invader1_6x_change
    invader5_3x += invader1_6x_change
    invader5_4x += invader1_6x_change
    invader5_5x += invader1_6x_change
    invader5_6x += invader1_6x_change
    invader5_7x += invader1_6x_change
    invader5_8x += invader1_6x_change
    invader5_9x += invader1_6x_change
    invader5_10x += invader1_6x_change
    invader5_11x += invader1_6x_change
    invader5y += invader1_6y_change
    invaderfreex += invaderfreex_change
    e1bully += e1bully_change
    e2bully += e1bully_change
    e3bully += e1bully_change
    e4bully += e1bully_change
    bully += bully_change
    gameDisplay.fill(black)
    invader1_6(invader1_6x, invader1_6y)
    invader1_1(invader1_1x, invader1_1y)
    invader1_2(invader1_2x, invader1_1y)
    invader1_3(invader1_3x, invader1_1y)
    invader1_4(invader1_4x, invader1_1y)
    invader1_5(invader1_5x, invader1_1y)
    invader1_6real(invader1_6realx, invader1_1y)
    invader1_7(invader1_7x, invader1_1y)
    invader1_8(invader1_8x, invader1_1y)
    invader1_9(invader1_9x, invader1_1y)
    invader1_10(invader1_10x, invader1_1y)
    invader2_1(invader2_1x, invader2_1y)
    invader2_2(invader2_2x, invader2_1y)
    invader2_3(invader2_3x, invader2_1y)
    invader2_4(invader2_4x, invader2_1y)
    invader2_5(invader2_5x, invader2_1y)
    invader2_6(invader2_6x, invader2_1y)
    invader2_7(invader2_7x, invader2_1y)
    invader2_8(invader2_8x, invader2_1y)
    invader2_9(invader2_9x, invader2_1y)
    invader2_10(invader2_10x, invader2_1y)
    invader2_11(invader2_11x, invader2_1y)
    invader3_1(invader3_1x, invader3y)
    invader3_2(invader3_2x, invader3y)
    invader3_3(invader3_3x, invader3y)
    invader3_4(invader3_4x, invader3y)
    invader3_5(invader3_5x, invader3y)
    invader3_6(invader3_6x, invader3y)
    invader3_7(invader3_7x, invader3y)
    invader3_8(invader3_8x, invader3y)
    invader3_9(invader3_9x, invader3y)
    invader3_10(invader3_10x, invader3y)
    invader3_11(invader3_11x, invader3y)
    invader4_1(invader4_1x, invader4y)
    invader4_2(invader4_2x, invader4y)
    invader4_3(invader4_3x, invader4y)
    invader4_4(invader4_4x, invader4y)
    invader4_5(invader4_5x, invader4y)
    invader4_6(invader4_6x, invader4y)
    invader4_7(invader4_7x, invader4y)
    invader4_8(invader4_8x, invader4y)
    invader4_9(invader4_9x, invader4y)
    invader4_10(invader4_10x, invader4y)
    invader4_11(invader4_11x, invader4y)
    invader5_1(invader5_1x, invader5y)
    invader5_2(invader5_2x, invader5y)
    invader5_3(invader5_3x, invader5y)
    invader5_4(invader5_4x, invader5y)
    invader5_5(invader5_5x, invader5y)
    invader5_6(invader5_6x, invader5y)
    invader5_7(invader5_7x, invader5y)
    invader5_8(invader5_8x, invader5y)
    invader5_9(invader5_9x, invader5y)
    invader5_10(invader5_10x, invader5y)
    invader5_11(invader5_11x, invader5y)
    invaderfree(invaderfreex, invaderfreey)
    explosion(ex, ey)
    enem1bull(e1bullx, e1bully)
    enem2bull(e2bullx, e2bully)
    enem3bull(e3bullx, e2bully)
    enem5bull(e5bullx, e5bully)
    shield1(shield1x, shieldy)
    shield2(shield2x, shieldy)
    shield3(shield3x, shieldy)
    shield4(shield4x, shieldy)
    livessprite(livex, livey)
    #i had problems with showing score so i put the function here instead of a "def" thing
    score_show = font.render("Score: " + str(score), True ,(white))
    gameDisplay.blit(score_show, (textX, textY))
    gameover(gmx, gmy)
    player(x, y)
    bullet(bullx, bully) #<--- rtx 3080
    pygame.display.update()
    clock.tick(60)
if win: #<-- if you somehow manage to beat stage 2
    print("You win!")
    print("Your final score was:", score)
pygame.quit() #<--- quits pygame
quit() #<-- quits code
#general kenobi.