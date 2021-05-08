#importing libraries and stuff
import pygame
import math
import random
import time
#initiates any modules in pygame
pygame.init()
#display
display_height = 600
display_width = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Offline Dinosaur Game 1.7.1')
#for main while loop
crashed = False
#RGB(for display colors)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200) #<--- I used this color for the display color
#speed
clock = pygame.time.Clock()
#sprite images
dinoimg = pygame.image.load('dinowalk0.png')
platformimg = pygame.image.load('dinoground.png')
cactusimg = pygame.image.load('smallcactus1.png')
cloud1img = pygame.image.load('cloud1.png')
cloud2img = pygame.image.load('cloud1.png')
pteradactylimg = pygame.image.load('pteradactyl1.png')
startplatimg = pygame.image.load('start_thing.png')
#sounds
dino_jump = pygame.mixer.Sound('jump_effect_dino.wav')
oof_sound = pygame.mixer.Sound('oof_sound.wav')
#so the sprites can display properly on screen
def dino(x, y):
    gameDisplay.blit(dinoimg, (x, y))
def platform(platx, platy):
    gameDisplay.blit(platformimg, (platx, platy))
def cactus(cactx, cacty):
    gameDisplay.blit(cactusimg, (cactx, cacty))
def cloud1(cloud1x, cloud1y):
    gameDisplay.blit(cloud1img, (cloud1x, cloud1y))
def cloud2(cloud2x, cloud2y):
    gameDisplay.blit(cloud2img, (cloud2x, cloud2y))
def pteradactyl(pterx, ptery):
    gameDisplay.blit(pteradactylimg, (pterx, ptery))
def start_plat(startplatx, startplaty):
    gameDisplay.blit(startplatimg, (startplatx, startplaty))
#so that the dino knows when to stop falling
def jump(y, platy):
    if y > 300:
        return True
    else:
        return False
#collision functions
def collision(x, y, cactx, cacty):
    if coolpoints >= 20:
        return False
    distance = math.sqrt(math.pow(x - cactx, 2) + math.pow(y - cacty, 2))
    if distance < 65:
        return True
    else:
        return False
def ptercollision(x, y, pterx, ptery):
    if coolpoints >= 20:
        return False
    distance2 = math.sqrt(math.pow(x - pterx, 2) + math.pow(y - ptery, 2))
    if distance2 < 50:
        return True
    else:
        return False
#speeding up sprites
def speedup(score, prevscore):
    difference = score - prevscore
    if difference > 3000:
        return True
    else:
        return False
score = 0
prevscore = 0
#x and y pos, other variables
x = 170
y = 300
startplatx = 250
startplaty = 350
startplat_xchange = 0
pterx = 810
ptery = random.randint(150, 250)
cloud1x = 810
cloud1y = random.randint(0, 150)
cloud2x = 810
cloud2y = random.randint(0, 150)
cactx = 810
cacty = 320
platx = 0
platy = 380
y_change = 0
x_change = 0
jumping = True
jump_counter = 0
platx_change = 0
pterx_change = 0
pterx_change2 = 0
cactx_change = 0
cacttimer = random.randint(100, 200)
cactussprite = random.randint(1, 4)
cloud1x_change = 0
cloud2x_change = 0
first_cloudspeed = False
first_firstcloudspeed = True
cloud2x_change2 = 0
cloud1x_change2 = 0
cactx_change2 = 0
platx_change2 = 0
pter = False
timer = 40
pterspritetimer = 40
duck = False
cloud2_move = False
ptertimer = 2000
idle = True
coolpoints = 0
sanic = False
say_sonic = True
time_alive = 0
#keybinds
print("Offline Dinosaur Game Version 1.7")
print("Welcome player.")
print("This is the Chrome Dinosaur Game coded in Python.")
print("x---------------------------------x")
print(" Controls:")
print(" Jump: Space Key or Up Arrow Key")
print(" (Hold It To Jump Higher)")
print(" Duck: Down Arrow Key")
print(" Pause(5 secs): Z Key")
print(" Jump to start.")
print("x---------------------------------x")
#first loop(for starting the game)
#this was made because it was to give the player some time to prepare
while idle:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(dino_jump)
                y_change = -5
                startplat_xchange = 10
        if y < 300:
            idle = False
    startplatx += startplat_xchange
    y += y_change
    gameDisplay.fill(white)
    cloud2(cloud2x, cloud2y)
    cloud1(cloud1x, cloud1y)
    cactus(cactx, cacty)
    pteradactyl(pterx, ptery)
    dino(x, y)
    platform(platx, platy)
    start_plat(startplatx, startplaty)
    pygame.display.update()
    clock.tick(240)
#the actual game
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                pygame.mixer.Sound.play(dino_jump)
                if y == 300:
                    # jump y pos change
                    y_change = -5
                    jump_counter += 1
                    # jump counter
                    if jump_counter > 1:
                        print("You have jumped", jump_counter, "times!")
                    if jump_counter == 1:
                        print("You have jumped", jump_counter, "time!")
            if event.key == pygame.K_ESCAPE:
                print("Thank you for playing the game!")
                crashed = True
            if event.key == pygame.K_DOWN:
                duck = True
                y_change = 10
            if event.key == pygame.K_8: #<--- dont look here pls
                coolpoints += 1
            if event.key == pygame.K_z:
                print("You have paused the game for 5 seconds.")
                time.sleep(1)
                print("4 seconds left.")
                time.sleep(1)
                print("3 seconds left.")
                time.sleep(1)
                print("2 seconds left.")
                time.sleep(1)
                print("1 second left.")
                time.sleep(1)
                print("0 seconds left.")
        # if player lifts up key from keyboard
        if event.type == pygame.KEYUP:
            score += 0
            duck = False
            x_change = 0
            y_change = 5
            coolpoints += 0
    # things to make sure dino is in the right x and y pos
    if y > 300:
        y_change = 5
        if jump(y, platy):
            y_change = 0
    if jump(y, platy):
        y = 300
        if y != 300:
            y = 300
    if y < 125:
        y_change = 5
    if platx < -400:
        platx = 30
    #for when the pteradactyl will appear or not
    if pter and ptertimer < 0:
        if pterx < -5000:
            ptery = random.randint(150, 250)
            pterx = 810
    if pter:
        ptertimer -= 0.5
    if pter and ptertimer < 0:
        pterx_change = -10
        ptertimer = 2000
    # sprite changing for dinosaurs
    if timer < 0 and sanic:
        timer = 40
        dinoimg = pygame.image.load('sonic1.png')
    if timer == 20 and sanic:
        dinoimg = pygame.image.load('sonic2.png')
    if timer < 0 and not duck and not sanic:
        timer = 40
        dinoimg = pygame.image.load('dinowalk1.png')
    if timer == 20 and not duck and not sanic:
        dinoimg = pygame.image.load('dinowalk2.png')
    if timer < 0 and duck and not sanic:
        dinoimg = pygame.image.load('dinoduck1.png')
        timer = 40
    if timer == 20 and duck and not sanic:
        dinoimg = pygame.image.load('dinoduck2.png')
    if pterspritetimer < 0:
        pterspritetimer = 40
        pteradactylimg = pygame.image.load('pteradactyl1.png')
    if pterspritetimer == 20:
        pteradactylimg = pygame.image.load('pteradactyl2.png')
    #definently nothing to see here!
    if coolpoints >= 20:
        score += 10000000000000000000000000000000000000000000000000000000000#<---- thats a lotta zeros
        sanic = True
    if coolpoints >= 20 and say_sonic: #dont peak here pls
        print("You are sonic! You clever, sneaky one. You have found the cheat code and now you are immortal.")
        print("Watch how the game breaks(press esc key to quit fyi).")
        say_sonic = False
    # timer for cactus
    if cacttimer < 0:
        if cactx < -50:
            cactx = 810
            cacttimer = random.randint(75, 200)
            cactussprite = random.randint(1, 4)#<-- cactus sprite alternation
            if cactussprite == 1:
                cacty = 320
                cactusimg = pygame.image.load('smallcactus1.png')
            if cactussprite == 2:
                cacty = 320
                cactusimg = pygame.image.load('smallcactus2.png')
            if cactussprite == 3:
                cacty = 300
                cactusimg = pygame.image.load('bigcactus1.png')
            if cactussprite == 4:
                cacty = 300 #i had to change the y pos since the image would look like it was in the ground
                cactusimg = pygame.image.load('bigcactus2.png')
    #original speeds of sprites
    if first_firstcloudspeed:
        cloud1x_change = -0.5
        cactx_change = -5
        platx_change = -5
    if cloud1x < -100:
        cloud1x = 810
        cloud1y = random.randint(0, 150)
    if cloud1x == 400 and not cloud2_move:
        cloud2_move = True
        first_cloudspeed = True
    if cloud2_move:
        if cloud2x < -100:
            cloud2x = 810
            cloud2y = random.randint(0, 150)
    #original speed of cloud2(idk why its in a separate if statement)
    if first_cloudspeed:
        cloud2x_change = -0.5
    #if the player gets hit
    if collision(x, y, cactx, cacty) or ptercollision(x, y, pterx, ptery):
        crashed = True
    #speeding up the game
    if speedup(score, prevscore):
        pter = True
        if pter:
            pterx_change = -7
        first_cloudspeed = False
        first_firstcloudspeed = False
        cloud2x_change2 += -0.06
        cloud1x_change2 += -0.06
        cactx_change2 += -0.6
        platx_change2 += -0.6
        pterx_change2 += -0.6
        prevscore = score
    #timers, display updating, etc
    time_alive += 0.5
    timer -= 1
    pterspritetimer -= 1
    score += 1
    cloud1x += (cloud1x_change + cloud1x_change2)
    cloud2x += (cloud2x_change + cloud2x_change2)
    platx += (platx_change + platx_change2)
    pterx += (pterx_change + pterx_change2)
    cacttimer -= 1
    y += y_change
    x += x_change
    cactx += (cactx_change + cactx_change2)
    # utilization of .blit functions
    gameDisplay.fill(white)
    cloud2(cloud2x, cloud2y)
    cloud1(cloud1x, cloud1y)
    cactus(cactx, cacty)
    pteradactyl(pterx, ptery)
    dino(x, y)
    platform(platx, platy)
    #display updating and fps
    pygame.display.update()
    clock.tick(240)
pygame.mixer.Sound.play(oof_sound)
print("You score was:", score)
print("You were alive for:", time_alive)
print("(This isn't measured in any type of time, it is just a variable)")
time.sleep(0.5)
#quitting python code
pygame.quit()
quit()