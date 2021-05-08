#This game is not finished. This is also my first project w/ pygame, so it is not perfect. I am at the 2nd bossfight right now(i have not added bullets to it.).
#importing functions
import pygame
import time
import random
import math

#initiates pygame
pygame.init()

#display
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

#name of the thing on top
pygame.display.set_caption('Squirrel Shooter 4.0')

#RGBcdd
black = (0, 0, 0)
white = (255, 255, 255)

#speed
clock = pygame.time.Clock()

#variable for while loops
crashed = False

#sprites(the original sprite was a car but i decided to change that.)
backgroundimg = pygame.image.load('background.jpg')
enemy2img = pygame.image.load('milk.png')
squirrelImg = pygame.image.load('squirrel.png')
bullimg = pygame.image.load('costume3.png')
enemy1img = pygame.image.load('milk.png')
enemy1bullimg = pygame.image.load('milk.png')
enemy2bullimg = pygame.image.load('milk.png')
bossimg = pygame.image.load('ufoboss.png')
bossbullimg = pygame.image.load('costume3.png')
bossfightwarnimg = pygame.image.load('bossfight_warning.png')
boss2img = pygame.image.load('boss2.png')
watercupimg = pygame.image.load('watercup.png')
boss2bullimg = pygame.image.load('costume3.png')

#sprite wrappers(so that python will know what coordianate to display an image. for example coordinate x: 420 y: 69)
def enemy1(enemy1x, enemy1y):
    gameDisplay.blit(enemy1img, (enemy1x, enemy1y))

def squirrel(x, y):
    gameDisplay.blit(squirrelImg, (x, y))

def bullet(bullx, bully):
    gameDisplay.blit(bullimg, (bullx, bully))

def enemy1bull(enemy1bullx, enemy1bully):
    gameDisplay.blit(enemy1bullimg, (enemy1bullx, enemy1bully))

def enemy2(enemy2x, enemy2y):
    gameDisplay.blit(enemy2img,(enemy2x, enemy2y))

def enemy2bull(enemy2bullx, enemy2bully):
    gameDisplay.blit(enemy2bullimg, (enemy2bullx ,enemy2bully))

def ufoboss(ufox, ufoy):
    gameDisplay.blit(bossimg, (ufox, ufoy))

def ufobull(ufobullx, ufobully):
    gameDisplay.blit(bossbullimg, (ufobullx, ufobully))

def bossfightwarn(bosswarnx, bosswarny):
    gameDisplay.blit(bossfightwarnimg, (bosswarnx, bosswarny))

def boss2(boss2x, boss2y):
    gameDisplay.blit(boss2img, (boss2x, boss2y))

def watercup(waterx, watery):
    gameDisplay.blit(watercupimg, (waterx, watery))

def boss2bull(bossbull2x, bossbull2y):
    gameDisplay.blit(boss2bullimg, (bossbull2x, bossbull2y))

x = (display_width * 0.45)
y = (display_height * 0.8)
bullet_state = True

#coords, other variables
bossalive = False
boss2x = -24
boss2y = 10000
boss2x_change = 0
boss2y_change = 0
stage = 1
enemy2ybull_change = 0
enemy1bully = -15
x_change = 0
y_change = 0
car_speed = 0
bully = 1000
bullx = x
bull_xchange = 0
bull_ychange = 0
enemy2x = 780
enemy2y = 15
enemy1x = -24
enemy1y = 15
enemy2x_change = 0
enemy2y_change = 0
enemy1_xchange = 0
enemy1_ychange = 0
enemy2bullx = enemy2x
enemy2bully = enemy2y
touchingborder = False
ufox = -24
ufoy = 7000
ufoxchange = 0
ufoychange = 0
goright = True
bossright = True
broadcast_bossfight = True
ufobullychange = 0
bossbullet = True
ufobullx = ufox
ufobully = ufoy
ufobullxchange = 0
bosswarnx = 30
bosswarny = 300
goawaywarn = False
boss2right = False
water_drop = False
dorandomwater = True
waterx = -24
watery = 8764123#just a random number lol
watery_change = 0
bossbullstate2 = True
bossbull2x = -24
bossbull2y = 9013#another weird number
bossbull2x_change = 0
bossbull2y_change = 0

#HP Things
enemy1_health = 10
HP = 150
enemy2_health = 10
boss_health = 20
boss2_health = 300

#number of enemies in stage 1
stage_oneenem_count = 2

enemy1alive = True
enemy1bull_state = True
enemy1bullx = enemy1x
enemy1_bullychange = 0
enemy2bullx = enemy2x
bossalive2 = False
second_broadcast = True

#collision things
def collision(bullx, bully, enemy1x, enemy1y):
    #the "distance =" thing is an equation to calculate the distance of how close the bullet is to the enemy. The math.sqrt calculates the square root of anything inside of the brackets.
    #the math.pow calculates the power of a given equation or singular number by the second arguement(separated by a comma.). This over calculates the distance between the bullet and sprite.
    distance = math.sqrt(math.pow(enemy1x - bullx, 2) + (math.pow(enemy1y - bully, 2)))
    if distance < 37:
        return True
    else:
        return False

def collision2(bullx, bully, enemy2x, enemy2y):
    distance = math.sqrt(math.pow(enemy2x - bullx, 2) + (math.pow(enemy2y - bully, 2)))
    if distance < 37:
        return True
    else:
        return False

def enemcollision(enemy1bullx, enemy1bully, x, y):
    distance2 = math.sqrt(math.pow(x - enemy1bullx, 2) + (math.pow(y - enemy1bully, 2)))
    if distance2 < 80:
        return True
    else:
        return False

def enemcollision(enemy2bullx, enemy2bully, x, y):
    distance2 = math.sqrt(math.pow(x - enemy2bullx, 2) + (math.pow(y - enemy2bully, 2)))
    if distance2 < 80:
        return True
    else:
        return False

def bosscollision(bullx, bully, ufox, ufoy):
    distance3 = math.sqrt(math.pow(ufox - bullx, 2) + (math.pow(ufoy - bully, 2)))
    if distance3 < 100:
        return True
    else:
        return False

def playerbosscollision(ufobullx, ufobully, x, y):
    distance4 = math.sqrt(math.pow(x - ufobullx, 2) + (math.pow(y - ufobully, 2)))
    if distance4 < 80:
        return True
    else:
        return False

def water_needed(HP):
    if HP <= 14:
        return True
    else:
        return False

def waterplayer(waterx, watery, x, y):
    distance5 = math.sqrt(math.pow(x - waterx, 2) + math.pow(y - watery, 2))
    if distance5 < 50:
        return True
    else:
        return False

def boss2collision(boss2x, boss2y, bullx, bully):
    distance6 = math.sqrt(math.pow(boss2x - bullx, 2) + math.pow(boss2y - bully, 2))
    if distance6 < 100:
        return True
    else:
        return False

def playerboss2collision(x, y, bossbull2x, bossbull2y):
    distance7 = math.sqrt(math.pow(x - bossbull2x, 2) + math.pow(y - bossbull2y, 2))
    if distance7 < 80:
        return True
    else:
        return False

#the game itself
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #keybinds(edit if you want)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -6
            elif event.key == pygame.K_d:
                x_change = 6
            #shooting requires button mashing(of space key)
            elif event.key == pygame.K_SPACE:
                #player bullets
                if bullet_state == True:
                    bullet_state = False
                    print("Bullet Shot.")
                    bully = 480
                    bull_ychange = -10
                if bullet_state == False:
                    #for the bullet cooldown to end.
                    if bully <= 120:
                        bullet_state = True
                        bully = 1000
            #if player presses escape key
            elif event.key == pygame.K_ESCAPE:
                crashed = True

        #when key from keyboard is lifted
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                x_change = 0
                y_change = 0
    #if enemy1 gets hit by player
    if collision(bullx, bully, enemy1x, enemy1y):
        enemy1_health = enemy1_health - 2
        if enemy1_health < 1:
            enemy1y = 69420#nice
            enemy1_health = 10
            stage_oneenem_count = stage_oneenem_count - 1
    if collision2(bullx, bully, enemy2x, enemy2y):
        enemy2_health = enemy2_health - 2
        if enemy2_health < 1:
            enemy2y = 6000
            enemy2_health = 10
            stage_oneenem_count = stage_oneenem_count - 1
    #whether the player can shoot or not
    if bullet_state:
        bullx = x

    #If you need water
    if water_needed(HP) and dorandomwater and not water_drop:
        waterx = random.randint(-24, 680)
        watery = 0
        water_drop = True
        dorandomwater = False

    if water_drop:
        watery_change = 2.5
        if water_drop == 650:
            watery = 6000
            dorandomwater = True
            water_drop = False
    #regen!
    if waterplayer(waterx, watery, x, y):
        HP += 4

    #if player gets hit
    if enemcollision(enemy1bullx, enemy1bully, x, y):
        HP = HP - 1
        if HP < 1:
            HP = 0
            crashed = True
            print("You died!")
    if enemcollision(enemy2bullx, enemy2bully, x, y):
        HP = HP - 2
        if HP < 1:
            HP = 0
            crashed = True
            print("You died!")

    #if player leaves area
    if x < -65:
        x_change = 5
        x_change = 1
    if x > 770:
        x_change = -5
        x_change = -1

    #enemy1 movement
    if goright:
        enemy1_xchange = 4
    if enemy1x == 780:
        goright = False
    if goright == False and enemy1x > -14:
        enemy1_xchange = -4
    if enemy1x < -14:
        goright = True

    # enemy2 movement
    if goright:
        enemy2x_change = -4
    if enemy2x == -14:
        goright = False
    if goright == False and enemy1x < 780:
        enemy2x_change = 4
    if enemy2x == 780:
        goright = True

    #enemy 1 bullets
    if enemy1bull_state == True:
        enemy1_bully = enemy1y
        enemy1_bullychange = 7
        enemy1bull_state = False
    if not enemy1bull_state:
        if enemy1bully > 500:
            enemy1bully = enemy1y
            enemy1bullx = enemy1x
            enemy1bull_state = True

    #enemy2 bullets
    if enemy1bull_state == True:
        enemy2ybull_change = 7
        enemy1bull_state = False
    if not enemy1bull_state:
        if enemy2bully > 500:
            enemy2bully = enemy2y
            enemy2bullx = enemy2x
            enemy1bull_state = True
    #boss1 movement
    if bossalive and not broadcast_bossfight:
        if bossright:
            ufoxchange = 4
        if ufox == 680:
            bossright = False
        if not bossright and ufox == 680:
            ufoxchange = -4
        if ufox < -14:
            bossright = True

    #end of stage 1
    if stage_oneenem_count == 0:
        stage = 2

    if stage == 2:
        bossalive = True
    #broadcasting bossfight!
    if broadcast_bossfight and bossalive:
        broadcast_bossfight = False
        print("Incoming Bossfight!")
        time.sleep(1)
        print("Incoming Bossfight!")
        time.sleep(1)
        print("Incoming Bossfight!")
        time.sleep(1)
        ufoy = 15
        bossright = True

    #if boss1 gets hit
    if bosscollision(bullx, bully, ufox, ufoy):
        boss_health = boss_health - 1
        if boss_health <= 0:
            ufoy = 1000
            bossalive = False

    #boss1 bullets
    if bossalive and not broadcast_bossfight:
        if bossbullet == True:
            ufobullychange = 10
            bossbullet = False
        if not bossbullet:
            if ufobully > 500:
                ufobully = ufoy
                ufobullx = ufox + 20
                bossbullet = True
    #if player gets hit by boss
    if bossalive and not broadcast_bossfight:
        if playerbosscollision(x, y, ufobullx, ufobully):
            HP = HP - 2
            if HP < 1:
                HP = 0
                print("You died!")
                crashed = True
    #if the first boss dies
    if not bossalive and not broadcast_bossfight:
        bossalive2 = True

    #broadcasting 2nd bossfight
    if bossalive2 and second_broadcast:
        print("2nd boss is alive")
        time.sleep(1)
        print("Warning.")
        time.sleep(1)
        print("Prepare for the second bossfight.")
        second_broadcast = False
        bossbullstate2 = True
        boss2x = -24
        boss2y = -15

    #2nd boss movement
    if bossalive2 and not second_broadcast:
        if boss2right:
            boss2x_change = 6
        if boss2x == 678:
            boss2right = False
        if not boss2right and boss2x == 678:
            boss2x_change = -6
        if boss2x < -12:
            boss2right = True
    # boss2bullets bullets
    if bossalive2 and not second_broadcast:
        if bossbullstate2 == True:
            bossbull2y_change = 12
            if bossbull2y > 500:
                bossbullstate2 = False
        if not bossbullstate2:
            if enemy2bully > 500:
                bossbull2y = boss2y
                bossbull2x = boss2x
                bossbullstate2 = True

    #if boss2 gets hit by player
    if boss2collision(boss2x, boss2y, bullx, bully):
        boss2_health = boss2_health -2
        if boss2_health < 1:
            boss2y = 7364
            print("You won!")

    #if player gets hit by boss
    if playerboss2collision(x, y, bossbull2x, bossbull2y):
        HP = HP - 2
        if HP < 1:
            crashed = True
            print("You died!")

    #display updating and stuff
    gameDisplay.blit(backgroundimg, [0, 0]) #couldn't get this to work using a sprite. I had to search the internet for a solution.
    watercup(waterx, watery)
    boss2bull(bossbull2x, bossbull2y)
    x += x_change
    y += y_change
    bossbull2x += bossbull2x_change
    bossbull2y += bossbull2y_change
    watercup(waterx, watery)
    watery += watery_change
    boss2x += boss2x_change
    boss2y += boss2y_change
    boss2(boss2x, boss2y)
    ufobully += ufobullychange
    ufobullx += ufobullxchange
    ufobull(ufobullx, ufobully)
    ufox += ufoxchange
    ufoy += ufoychange
    enemy2bully += enemy2ybull_change
    enemy2x += enemy2x_change
    bully += bull_ychange
    enemy1x += enemy1_xchange
    enemy1bully += enemy1_bullychange
    print(HP)
    print(boss2_health)
    squirrel(x, y)
    ufoboss(ufox, ufoy)
    enemy2bull(enemy2bullx, enemy2bully)
    bullet(bullx, bully)
    enemy2(enemy2x, enemy2y)
    enemy1(enemy1x, enemy1y)
    enemy1bull(enemy1bullx, enemy1bully)
    pygame.display.update()
    clock.tick(240)

pygame.quit()
quit()