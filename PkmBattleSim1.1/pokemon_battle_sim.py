import pygame
import math
import random
import time

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Pokemon Battle Sim Version 1.1')
pick_a_team = True

protagnists = ["Red", "Leaf", "Brendan", "May", "Lucas", "Dawn"]
red = ["Pikachu", "Charizard", "Venusaur", "Blastoise", "Snorlax", "Lapras"]
leaf = ["Venusaur", "Jolteon", "Wigglytuff", "Ninetales", "Gengar", "Slowbro"]
brendan = ["Swampert", "Shiftry", "Swellow", "Camerupt", "Aggron", "Grumpig"]
may = ["Blaziken", "Tropius", "Swellow", "Raichu", "Pelipper", "Magcargo"]
lucas = ["Torterra", "Alakazam", "Clefable", "Magmortar", "Luxray", "Garchomp"]
dawn = ["Piplup", "Buneary", "Pachirisu", "Mamoswine", "Typhlosion", "Togekiss"]
enemteam = []

pikachu_moves = ["Thunderbolt", "Iron Tail"]
charizard_moves = ["Flamethrower", "Dragon Pulse"]
venusaur_moves = ["Petal Blizzard", "Outrage"]
jolteon_moves = ["Thunderbolt", "Bite"]
blastoise_moves = ["Hydro Pump", "Surf"]
wigglytuff_moves = ["Psychic", "Thunder Punch"]
snorlax_moves = ["Headbutt", "Earthquake"]
lapras_moves = ["Ice Beam", "Hydro Pump"]
ninetails_moves = ["Flamethrower", "Headbutt"]
gengar_moves = ["Thunder Punch", "Sucker Punch"]
slowbro_moves = ["Ice Beam", "Surf"]
swampert_moves = ["Earthquake", "Hydro Pump"]
shirfty_moves = ["Razor Leaf", "Air Cutter"]
swellow_moves = ["Hurricane", "Steel Wing"]
camerupt_moves = ["Flamethrower", "Earthquake"]
aggron_moves = ["Headbutt", "Surf"]
grumpig_moves = ["Psychic", "Shadow Ball"]
blaziken_moves = ["Flamethrower", "Close Combat"]
tropius_moves = ["Razor Leaf", "Headbutt"]
raichu_moves = ["Thunderbolt", "Surf"]
pelipper_moves = ["Hydro Pump", "Hurricane"]
magcargo_moves = ["Flamethrower", "Earthquake"]
torterra_moves = ["Earthquake", "Bite"]
alakazam_moves = ["Psychic", "Dazzling Gleam"]
clefable_moves = ["Moonblast", "Thunder Punch"]
magmortar_moves = ["Flamethrower", "Earthquake"]
luxray_moves = ["Thunderbolt", "Play Rough"]
garchomp_moves = ["Dragon Pulse", "Iron Head"]
piplup_moves = ["Hydro Pump", "Water Pulse"]
buneary_moves = ["Thunder Punch", "Ice Beam"]
pachirisu_moves = ["Thunderbolt", "Bite"]
mamoswine_moves = ["Ice Beam", "Earthquake"]
typhlosion_moves = ["Flamethrower", "Thunder Punch"]
togekiss_moves = ["Psychic", "Dazzling Gleam"]

black = (60, 32, 18)
attacks = []

#sprites
playerImg = ""
pickedImg = ""
backgroundImg = pygame.image.load('battlebackground11.png')
battlemImg = ""
option1Img = pygame.image.load('attackpkm.png')
option2Img = pygame.image.load('runaway.png')
cursorImg = pygame.image.load('cursor.png')
battlemusic = pygame.mixer.Sound('battle_music.wav')
def picked(pickedx, pickedy):
    gameDisplay.blit(pickedImg, (pickedx, pickedy))
def enemy1(enemx1, enem1y):
    gameDisplay.blit(enemImg, (enemx1, enem1y))
def bg(bgx, bgy):
    gameDisplay.blit(backgroundImg, (bgx, bgy))
def intro(ix, iy):
    gameDisplay.blit(introImg, (ix, iy))
def battleem(bex, bey):
    gameDisplay.blit(battlemImg, (bex, bey))
def plpkm(plpkmx, plpkmy):
    gameDisplay.blit(plpkmImg, (plpkmx, plpkmy))
def enempkm(enempkmx, enempkmy):
    gameDisplay.blit(enempkmImg, (enempkmx, enempkmy))
def op1(op1x, op1y):
    gameDisplay.blit(option1Img, (op1x, op1y))
def op2(op2x, op1y):
    gameDisplay.blit(option2Img, (op2x, op1y))
def cursor(cx, cy):
    gameDisplay.blit(cursorImg, (cx, cy))
def choice1col(cx, cy, op1x, op1y):
    distance1 = math.sqrt(math.pow(op1x - (cx - 85), 2) + math.pow(op1y - (cy - 45), 2))
    if distance1 < 90:
        return True
    else:
        return False
def choice2col(cx, cy, op2x, op1y):
    distance2 = math.sqrt(math.pow(op2x - (cx - 30), 2) + math.pow(op1y - (cy - 45), 2))
    if distance2 < 90:
        return True
    else:
        return False

pickedx = 0
pickedy = 0
enempkmx = 0
enempkmy = 0
enempkmImg = ""
bgx = 0
bgy = 0
bex = 0
bey = 335
ix = 720

while pick_a_team:
    team = input("Pick a Player(red/leaf/brendan/may/lucas/dawn): ")
    if team.lower() == "red":
        print("Looks like you picked", team+".")
        del protagnists[0]
        person = "red"
        team = red
        iy = 150
        pickedImg = pygame.image.load('redpicked.png')
        introImg = pygame.image.load('redintro1.png')
        pick_a_team = False
    elif team.lower() == "leaf":
        print("Looks like you picked", team + ".")
        person = "leaf"
        iy = 90
        team = leaf
        pickedImg = pygame.image.load('leafpicked.png')
        introImg = pygame.image.load('leafintro1.png')
        del protagnists[1]
        pick_a_team = False
    elif team.lower() == "brendan":
        print("Looks like you picked", team + ".")
        person = "brendan"
        pickedImg = pygame.image.load('brendanpicked.png')
        introImg = pygame.image.load('brendanintro1.png')
        iy = 135
        del protagnists[2]
        team = brendan
        pick_a_team = False
    elif team.lower() == "may":
        person = "may"
        print("Looks like you picked", team + ".")
        del protagnists[3]
        iy = 160
        pickedImg = pygame.image.load('maypicked.png')
        introImg = pygame.image.load('mayintro1.png')
        team = may
        pick_a_team = False
    elif team.lower() == "lucas":
        person = "lucas"
        print("Looks like you picked", team + ".")
        iy = 100
        pickedImg = pygame.image.load('lucaspicked.png')
        introImg = pygame.image.load('lucasintro1.png')
        team = lucas
        del protagnists[4]
        pick_a_team = False
    elif team.lower() == "dawn":
        person = "dawn"
        print("Looks like you picked", team + ".")
        iy = 100
        pickedImg = pygame.image.load('dawnpicked.png')
        introImg = pygame.image.load('dawnintro1.png')
        team = dawn
        del protagnists[5]
        pick_a_team = False
    else:
        print("Invalid input.")
picked_person = True
gameDisplay = pygame.display.set_mode((800, 600))
timer1 = 0
while picked_person:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if timer1 > 300:
        pickedx = 829304
    if timer1 > 310:
        picked_person = False
    timer1 += 1
    picked(pickedx, pickedy)
    pygame.display.update()
    clock.tick(60)
print("Your team consists of:", team)
enemy = protagnists[random.randint(0, 4)]
if enemy == "Red":
    enemteam = red
    enemImg = pygame.image.load('red.png')
    battlemImg = pygame.image.load('battlered.png')
if enemy == "Leaf":
    enemteam = leaf
    enemImg = pygame.image.load('leaf.png')
    battlemImg = pygame.image.load('battleleaf.png')
if enemy == "Brendan":
    enemteam = brendan
    enemImg = pygame.image.load('brendan.png')
    battlemImg = pygame.image.load('battlebrendan.png')
if enemy == "May":
    enemteam = may
    enemImg = pygame.image.load('may.png')
    battlemImg = pygame.image.load('battlemay.png')
if enemy == "Lucas":
    enemteam = lucas
    enemImg = pygame.image.load('lucas.png')
    battlemImg = pygame.image.load('battlelucas.png')
if enemy == "Dawn":
    enemteam = dawn
    enemImg = pygame.image.load('dawn.png')
    battlemImg = pygame.image.load('battledawn.png')
time.sleep(1)
print("It appears that you are going to fight", enemy+".")
time.sleep(1)
print("They have a team of:", enemteam)
time.sleep(1)
battleIntro = True
intro2 = False
ix_change = 0
enemx1_change = 0
enemx1 = 0
enem1y = 0
pickedx = 2132
pickedy = 1782
battle = False
gameDisplay = pygame.display.set_mode((950, 445))
pygame.mixer.Sound.play(battlemusic, loops=1819779)
if enemy == "Red" or enemy == "Leaf" or enemy == "Brendan" or enemy == "May":
    enemx1 = -300
    enem1y = -125
pressspace = False
while battleIntro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pressspace:
                battleIntro = False
                intro2 = True
    ix_change = -5
    if ix == 100:
        ix_change = 0
        pressspace = True
    if enemy == "Dawn" or enemy == "Lucas":
        enemx1_change = 5
        enem1y = 0
        if enemx1 == 600:
            enemx1_change = 0
    if enemy == "Red" or enemy == "Leaf" or enemy == "Brendan" or enemy == "May":
        enemx1_change = 5
        if enemx1 == 340:
            enemx1_change = 0
    ix += ix_change
    enemx1 += enemx1_change
    pickedx = 2132
    pickedy = 1782
    bg(bgx, bgy)
    battleem(bex, bey)
    enemy1(enemx1, enem1y)
    intro(ix, iy)
    pygame.display.update()
    clock.tick(60)
iy_change = 0
timer2 = 0
pokemon_used = team[0]
enem_pokemon_used = enemteam[0]
changeintrosprite = True
print("You have sent out", pokemon_used + "!")
while intro2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if changeintrosprite:
        if person == "red":
            if timer2 == 20:
                iy = 155
                introImg = pygame.image.load('redintro2.png')
            if timer2 == 40:
                introImg = pygame.image.load('redintro3.png')
            if timer2 == 60:
                introImg = pygame.image.load('redintro4.png')
            if timer2 > 40:
                ix_change = -5
                enemx1_change = 5
        if person == "leaf":
            if timer2 == 20:
                iy = 155
                introImg = pygame.image.load('leafintro2.png')
            if timer2 == 40:
                introImg = pygame.image.load('leafintro3.png')
            if timer2 == 60:
                introImg = pygame.image.load('leafintro4.png')
            if timer2 > 40:
                ix_change = -5
                enemx1_change = 5
        if person == "brendan":
            if timer2 == 20:
                iy = 135
                introImg = pygame.image.load('brendanintro2.png')
            if timer2 == 40:
                introImg = pygame.image.load('brendanintro3.png')
            if timer2 == 60:
                introImg = pygame.image.load('brendanintro4.png')
            if timer2 == 70:
                introImg = pygame.image.load('brendanintro5.png')
                iy = 140
            if timer2 > 40:
                ix_change = -5
                enemx1_change = 5
        if person == "may":
            if timer2 == 20:
                iy = 160
                introImg = pygame.image.load('mayintro2.png')
            if timer2 == 40:
                introImg = pygame.image.load('mayintro3.png')
            if timer2 == 60:
                introImg = pygame.image.load('mayintro4.png')
            if timer2 == 70:
                introImg = pygame.image.load('mayintro5.png')
            if timer2 > 40:
                ix_change = -5
                enemx1_change = 5
        if person == "lucas":
            if timer2 == 40:
                iy = 140
                introImg = pygame.image.load('lucasintro2.png')
            if timer2 > 40:
                ix_change = -5
                enemx1_change = 5
        if person == "dawn":
            if timer2 == 40:
                iy = 120
                introImg = pygame.image.load('dawnintro2.png')
            if timer2 > 40:
                ix_change = -5
                enemx1_change = 5
        if ix == -300:
            changeintrosprite = False
        if not changeintrosprite:
            battle = True
            intro2 = False
    timer2 += 1
    ix += ix_change
    enemx1 += enemx1_change
    iy += iy_change
    pickedx = 2132
    pickedy = 1782
    bg(bgx, bgy)
    battleem(bex, bey)
    enemy1(enemx1, enem1y)
    intro(ix, iy)
    pygame.display.update()
    clock.tick(60)
plpkmImg = ""
plspeed = 0
platk = 0
plHP = 819203
ix_change = 0
enemx1_change = 0
plpkmx = ""
plpkmy = ""
enem_speed = 0
enem_atk = 0
enem_HP = 712893
enempkmx = 600
enempkmy = 90
op1x = 490
op2x = 750
op1y = 355
cx = 400
cy = 300
c_change = 0
cy_change = 0
choice = ""
change_op = False
option = 1
attack = False
move = ""
damage = 0
reset = True
enemreset = True
enem_attack = ""
enem_attacks = ""
atk_timer = 0
timer_reset = False
counter = False
not_effective = False
pldef = 0
enemdef = 0
plpkm_count = 6
enempkm_count = 6
textX = 40
textY = 360
text2X = 10
text2Y = 10
text3Y = 70
pkm_used = ""
font = pygame.font.Font('8bit.ttf', 35)
font2 = pygame.font.Font('8bit.ttf', 23)
text4x = 450
text5x = 700
text4y = 372894
text6x = 800
text6y = 10
enem_atk_type = ""
atk_type = ""
enem_types = ""
types = ""
text7x = 178231
text7y = 82831023
plpkmx_change = 0
enempkmx_change = 0
player_animation2 = False
enemy_animation = False
enemy_animation2 = False
supereffective = False
score_show = font.render(str(pokemon_used) + " used " + move + "!", True, (black))
score_show6 = font.render("Its Super Effective!", True, (black))
score_show7 = font2.render("Its Not Very Effective...", True, (black))
player_animation = False
while battle: #main battle loop
    try:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cy_change = -5
                if event.key == pygame.K_DOWN:
                    cy_change = 5
                if event.key == pygame.K_RIGHT:
                    c_change = 5
                if event.key == pygame.K_LEFT:
                    c_change = -5
                if event.key == pygame.K_m:
                    reset = True
                    enemreset = True
                if event.key == pygame.K_SPACE:
                    # for choice 1(run or attack?)
                    if choice1col(cx, cy, op1x, op1y) and option == 1:
                        choice = "attack"
                        option = 2
                        change_op = True
                        atk_timer = 0
                        cx = 400
                        cy = 300
                    if choice2col(cx, cy, op2x, op1y) and option == 1:
                        choice = "run"
                        atk_timer = 0
                        cx = 400
                        cy = 300
                    # for choice 2(attack1/attack2)
                    if choice1col(cx, cy, op1x, op1y) and option == 2:
                        choice = "attack1"
                        battlemImg = pygame.image.load('whatdoyoudo2.jpg')
                        op1y = 347289
                        textX = 40
                        textY = 360
                        attack = True
                        atk_timer = 0
                        enem_attack = enem_attacks[random.randint(0, 1)]
                        text4x = 450
                        text5x = 700
                        text4y = 273894
                    if choice2col(cx, cy, op2x, op1y) and option == 2 and option != 1:
                        choice = "attack2"
                        textX = 40
                        textY = 360
                        attack = True
                        op1y = 347289
                        text4x = 450
                        text5x = 700
                        text4y = 823049
                        battlemImg = pygame.image.load('whatdoyoudo2.jpg')
                        atk_timer = 0
                        enem_attack = enem_attacks[random.randint(0, 1)]
            if event.type == pygame.KEYUP:
                cy_change = 0
                c_change = 0
        atk_timer += 1
        if option == 1:
            textY = 28934
            battlemImg = pygame.image.load('whatdoyoudo.jpg')
            option1Img = pygame.image.load('attackpkm.png')
            option2Img = pygame.image.load('runaway.png')
            op1x = 490
            op2x = 750
            op1y = 355
            text4x = 450
            text5x = 700
            text4y = 829348
            text6x = 8234
            text6y = 10
            supereffective = False
            not_effective = False
        if choice == "attack" and change_op and option == 2:
            op1x = 450
            op2x = 669
            text4x = 450
            text5x = 700
            text4y = 375
            option1Img = pygame.image.load('attack1.jpg')
            option2Img = pygame.image.load('attack2.jpg')
            change_op = False
        if choice == "run":
            print("You take the L.")
            quit()
            change_op = False
        if atk_timer > 360 and counter and plspeed >= enem_speed:
            enemy_animation2 = True

            supereffective = False
            not_effective = False
            if enem_attack == "Thunderbolt":
                enem_atk_type = "Electric"
                damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Camerupt":
                    damage *= 0
                if enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Togekiss":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Pikachu":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Iron Tail":
                enem_atk_type = "Steel"
                damage = int((random.randint(70, 100) + enem_atk + pldef) / 3)
                if pokemon_used == "Charizard" or pokemon_used == "Magmortar" or pokemon_used == "Swampert" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Typhlosion" or pokemon_used == "Garchomp" or pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
                if pokemon_used == "Clefable" or pokemon_used == "Wigglytuff" or pokemon_used == "Gengar" or pokemon_used == "Slowbro" or pokemon_used == "Mamoswine" or pokemon_used == "Togekiss" or pokemon_used == "Lapras":
                    damage *= 2
                    supereffective = True
            if enem_attack == "Flamethrower":
                enem_atk_type = "Fire"
                damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                if pokemon_used == "Venusaur" or pokemon_used == "Torterra" or pokemon_used == "Shirfty" or pokemon_used == "Tropius" or pokemon_used == "Aggron":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Piplup" or pokemon_used == "Blastoise" or pokemon_used == "Typhlosion" or pokemon_used == "Charizard" or pokemon_used == "Ninetails" or pokemon_used == "Camerupt" or pokemon_used == "Magmortar" or pokemon_used == "Blaziken" or pokemon_used == "Garchomp":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Dragon Pulse":
                enem_atk_type = "Dragon"
                damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                if pokemon_used == "Garchomp":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Wigglytuff" or pokemon_used == "Clefable":
                    damage *= 0
            if enem_attack == "Petal Blizzard":
                enem_atk_type = "Grass"
                damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                if pokemon_used == "Piplup" or pokemon_used == "Blastoise" or pokemon_used == "Swampert":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Typhlosion" or pokemon_used == "Charizard" or pokemon_used == "Ninetails" or pokemon_used == "Camerupt" or pokemon_used == "Magmortar" or pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Outrage":
                enem_atk_type = "Dragon"
                damage = int((random.randint(80, 120) + enem_atk + pldef) / 3)
                if pokemon_used == "Garchomp":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Wigglytuff" or pokemon_used == "Clefable":
                    damage *= 0
            if enem_attack == "Bite":
                enem_atk_type = "Dark"
                damage = int((random.randint(60, 80) + enem_atk + pldef) / 3)
                if pokemon_used == "Grumpig" or pokemon_used == "Alakazam" or pokemon_used == "Gengar":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Blaziken" or pokemon_used == "Clefable" or pokemon_used == "Wigglytuff":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Hydro Pump":
                enem_atk_type = "Water"
                damage = int((random.randint(90, 110) + enem_atk + pldef) / 3)
                if pokemon_used == "Charizard" or pokemon_used == "Blaziken" or pokemon_used == "Typhlosion" or pokemon_used == "Camerupt" or pokemon_used == "Magcargo" or pokemon_used == "Magmortar" or pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Venusaur" or pokemon_used == "Pelipper" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Lapras":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Surf":
                enem_atk_type = "Water"
                damage = int((random.randint(80, 100) + enem_atk + pldef) / 3)
                if pokemon_used == "Charizard" or pokemon_used == "Blaziken" or pokemon_used == "Typhlosion" or pokemon_used == "Camerupt" or pokemon_used == "Magcargo" or pokemon_used == "Magmortar" or pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Venusaur" or pokemon_used == "Pelipper" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Lapras":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Psychic":
                enem_atk_type = "Psychic"
                damage = int((random.randint(80, 100) + enem_atk + pldef) / 3)
                if pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Grumpig" or pokemon_used == "Aggron" or pokemon_used == "Alakazam":
                    damage = int(damage / 2)
                    not_effective = True
                if pokemon_used == "Shirfty":
                    damage *= 0
            if enem_attack == "Thunder Punch":
                enem_atk_type = "Electric"
                damage = int((random.randint(55, 75) + enem_atk + pldef) / 3)
                if pokemon_used == "Garchomp" or pokemon_used == "Swampert" or pokemon_used == "Camerupt":
                    damage *= 0
                if pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Slowbro" or pokemon_used == "Swellow" or pokemon_used == "Pelipper" or pokemon_used == "Charizard" or pokemon_used == "Togekiss":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Jolteon" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Venusaur" or pokemon_used == "Shirfty" or pokemon_used == "Aggron" or pokemon_used == "Raichu" or pokemon_used == "Luxray" or pokemon_used == "Pachirisu" or pokemon_used == "Pikachu":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Headbutt":
                enem_atk_type = "Normal"
                damage = int((random.randint(80, 90) + enem_atk + pldef) / 3)
                if pokemon_used == "Aggron" or pokemon_used == "Torterra" or pokemon_used == "Mamoswine":
                    damage = int(damage / 2)
                    not_effective = True
                if pokemon_used == "Gengar":
                    damage *= 0
            if enem_attack == "Earthquake":
                enem_atk_type = "Ground"
                damage = int((random.randint(90, 110) + enem_atk + pldef) / 3)
                if pokemon_used == "Gengar" or pokemon_used == "Aggron" or pokemon_used == "Pikachu" or pokemon_used == "Pachirisu" or pokemon_used == "Jolteon" or pokemon_used == "Luxray" or pokemon_used == "Raichu" or pokemon_used == "Garchomp" or pokemon_used == "Camerupt" or pokemon_used == "Blaziken" or pokemon_used == "Magcargo" or pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Charizard" or pokemon_used == "Swellow" or pokemon_used == "Tropius" or pokemon_used == "Togekiss":
                    damage *= 0
            if enem_attack == "Ice Beam":
                enem_atk_type = "Ice"
                damage = int((random.randint(80, 100) + enem_atk + pldef) / 3)
                if pokemon_used == "Swellow" or pokemon_used == "Tropius" or pokemon_used == "Venusaur" or pokemon_used == "Togekiss":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Magmortar" or pokemon_used == "Camerupt" or pokemon_used == "Typhlosion" or pokemon_used == "Aggron" or pokemon_used == "Lapras" or pokemon_used == "Slowbro":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Sucker Punch":
                enem_atk_type = "Dark"
                damage = int((random.randint(75, 80) + enem_atk + pldef) / 3)
                if pokemon_used == "Grumpig" or pokemon_used == "Alakazam" or pokemon_used == "Gengar":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Blaziken" or pokemon_used == "Clefable" or pokemon_used == "Wigglytuff":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Razor Leaf":
                enem_atk_type = "Grass"
                damage = int((random.randint(75, 85) + enem_atk + pldef) / 3)
                if pokemon_used == "Piplup" or pokemon_used == "Blastoise" or pokemon_used == "Swampert":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Typhlosion" or pokemon_used == "Charizard" or pokemon_used == "Ninetails" or pokemon_used == "Camerupt" or pokemon_used == "Magmortar" or pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Air Cutter":
                enem_atk_type = "Flying"
                damage = int((random.randint(65, 80) + enem_atk + pldef) / 3)
                if pokemon_used == "Venusaur" or pokemon_used == "Blaziken" or pokemon_used == "Tropius" or pokemon_used == "Torterra":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Pikachu" or pokemon_used == "Jolteon" or pokemon_used == "Pachirisu" or pokemon_used == "Luxray":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Hurricane":
                enem_atk_type = "Flying"
                damage = int((random.randint(95, 115) + enem_atk + pldef) / 3)
                if pokemon_used == "Venusaur" or pokemon_used == "Blaziken" or pokemon_used == "Tropius" or pokemon_used == "Torterra":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Pikachu" or pokemon_used == "Jolteon" or pokemon_used == "Pachirisu" or pokemon_used == "Luxray":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Steel Wing":
                enem_atk_type = "Steel"
                damage = int((random.randint(75, 85) + enem_atk + pldef) / 3)
                if pokemon_used == "Charizard" or pokemon_used == "Magmortar" or pokemon_used == "Swampert" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Typhlosion" or pokemon_used == "Garchomp" or pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
                if pokemon_used == "Clefable" or pokemon_used == "Wigglytuff" or pokemon_used == "Gengar" or pokemon_used == "Slowbro" or pokemon_used == "Mamoswine" or pokemon_used == "Togekiss" or pokemon_used == "Lapras":
                    damage *= 2
                    supereffective = True
            if enem_attack == "Shadow Ball":
                enem_atk_type = "Dark"
                damage = int((random.randint(70, 80) + enem_atk + pldef / 3))
                if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Close Combat":
                enem_atk_type = "Fighing"
                damage = int((random.randint(100, 120) + enem_atk + pldef) / 3)
                if pokemon_used == "Buneary" or pokemon_used == "Aggron" or pokemon_used == "Slowbro" or pokemon_used == "Lapras" or pokemon_used == "Mamoswine" or pokemon_used == "Snorlax":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Tropius" or pokemon_used == "Swellow" or pokemon_used == "Clefable" or pokemon_used == "Grumpig" or pokemon_used == "Togekiss" or pokemon_used == "Alakazam":
                    damage = int(damage / 2)
                    not_effective = True
                if pokemon_used == "Gengar":
                    damage *= 0
            if enem_attack == "Moonblast":
                enem_atk_type = "Fairy"
                damage = int((random.randint(75, 95) + enem_atk + pldef) / 3)
                if pokemon_used == "Garchomp" or pokemon_used == "Shirfty":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Aggron" or pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Play Rough":
                enem_atk_type = "Fairy"
                damage = int((random.randint(75, 90) + enem_atk + pldef) / 3)
                if pokemon_used == "Garchomp" or pokemon_used == "Shirfty":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Aggron" or pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Dazzling Gleam":
                enem_atk_type = "Fairy"
                damage = int((random.randint(65, 80) + enem_atk + pldef) / 3)
                if pokemon_used == "Garchomp" or pokemon_used == "Shirfty":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Aggron" or pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                    damage = int(damage / 2)
                    not_effective = True
            if enem_attack == "Iron Head":
                enem_atk_type = "Steel"
                damage = int((random.randint(65, 80) + enem_atk + pldef) / 3)
                if pokemon_used == "Charizard" or pokemon_used == "Magmortar" or pokemon_used == "Swampert" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Typhlosion" or pokemon_used == "Garchomp" or pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
                if pokemon_used == "Clefable" or pokemon_used == "Wigglytuff" or pokemon_used == "Gengar" or pokemon_used == "Slowbro" or pokemon_used == "Mamoswine" or pokemon_used == "Togekiss" or pokemon_used == "Lapras":
                    damage *= 2
                    supereffective = True
            if enem_attack == "Water Pulse":
                enem_atk_type = "Water"
                damage = int((random.randint(80, 90) + enem_atk + pldef) / 3)
                if pokemon_used == "Charizard" or pokemon_used == "Blaziken" or pokemon_used == "Typhlosion" or pokemon_used == "Camerupt" or pokemon_used == "Magcargo" or pokemon_used == "Magmortar" or pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if pokemon_used == "Venusaur" or pokemon_used == "Pelipper" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Lapras":
                    damage = int(damage / 2)
                    not_effective = True
            score_show = font.render(enem_pokemon_used + " used " + enem_attack + "!", True, (black))
            plHP -= damage
            counter = False
        if atk_timer > 360 and counter and plspeed < enem_speed:
            player_animation2 = True

            supereffective = False
            not_effective = False
            if choice == "attack1":
                move = attacks[0]
            if choice == "attack2":
                move = attacks[1]
            if move == "Thunderbolt":
                atk_type = "Electric"
                damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Camerupt":
                    damage *= 0
                if enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Togekiss":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Pikachu":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Iron Tail":
                atk_type = "Steel"
                damage = int((random.randint(70, 100) + platk + enemdef) / 3)
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
                if enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Lapras":
                    damage *= 2
                    supereffective = True
            if move == "Flamethrower":
                atk_type = "Fire"
                damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Tropius" and enem_pokemon_used == "Aggron":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Piplup" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Ninetails" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Garchomp":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Dragon Pulse":
                atk_type = "Dragon"
                damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Clefable":
                    damage *= 0
            if move == "Petal Blizzard":
                atk_type = "Grass"
                damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                if enem_pokemon_used == "Piplup" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Swampert":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Ninetails" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Outrage":
                atk_type = "Dragon"
                damage = int((random.randint(80, 120) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Clefable":
                    damage *= 0
            if move == "Bite":
                atk_type = "Dark"
                damage = int((random.randint(60, 80) + platk + enemdef) / 3)
                if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Hydro Pump":
                atk_type = "Water"
                damage = int((random.randint(90, 110) + platk + enemdef) / 3)
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Lapras":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Surf":
                atk_type = "Water"
                damage = int((random.randint(80, 100) + platk + enemdef) / 3)
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Lapras":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Psychic":
                atk_type = "Psychic"
                damage = int((random.randint(80, 100) + platk + enemdef) / 3)
                if enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Alakazam":
                    damage = int(damage / 2)
                    not_effective = True
                if enem_pokemon_used == "Shirfty":
                    damage *= 0
            if move == "Thunder Punch":
                atk_type = "Electric"
                damage = int((random.randint(55, 75) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Camerupt":
                    damage *= 0
                if enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Togekiss":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Pikachu":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Headbutt":
                atk_type = "Normal"
                damage = int((random.randint(80, 90) + platk + enemdef) / 3)
                if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Mamoswine":
                    damage = int(damage / 2)
                    not_effective = True
                if enem_pokemon_used == "Gengar":
                    damage *= 0
            if move == "Earthquake":
                atk_type = "Ground"
                damage = int((random.randint(90, 110) + platk + enemdef) / 3)
                if enem_pokemon_used == "Gengar" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Pikachu" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Togekiss":
                    damage *= 0
            if move == "Ice Beam":
                atk_type = "Ice"
                damage = int((random.randint(80, 100) + platk + enemdef) / 3)
                if enem_pokemon_used == "Swellow" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Togekiss":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Lapras" or enem_pokemon_used == "Slowbro":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Sucker Punch":
                atk_type = "Dark"
                damage = int((random.randint(75, 80) + platk + enemdef) / 3)
                if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Razor Leaf":
                atk_type = "Grass"
                damage = int((random.randint(75, 85) + platk + enemdef) / 3)
                if enem_pokemon_used == "Piplup" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Swampert":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Ninetails" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Air Cutter":
                atk_type = "Flying"
                damage = int((random.randint(65, 80) + platk + enemdef) / 3)
                if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Torterra":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Pikachu" or enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Luxray":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Hurricane":
                atk_type = "Flying"
                damage = int((random.randint(95, 115) + platk + enemdef) / 3)
                if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Torterra":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Pikachu" or enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Luxray":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Steel Wing":
                atk_type = "Steel"
                damage = int((random.randint(75, 85) + platk + enemdef) / 3)
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
                if enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Lapras":
                    damage *= 2
                    supereffective = True
            if move == "Shadow Ball":
                atk_type = "Dark"
                damage = int((random.randint(70, 80) + platk + enemdef / 3))
                if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Close Combat":
                atk_type = "Fighting"
                damage = int((random.randint(100, 120) + platk + enemdef) / 3)
                if enem_pokemon_used == "Buneary" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Lapras" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Snorlax":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Tropius" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Alakazam":
                    damage = int(damage / 2)
                    not_effective = True
                if enem_pokemon_used == "Gengar":
                    damage *= 0
            if move == "Moonblast":
                atk_type = "Fairy"
                damage = int((random.randint(75, 95) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Shirfty":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Play Rough":
                atk_type = "Fairy"
                damage = int((random.randint(75, 90) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Shirfty":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Dazzling Gleam":
                atk_type = "Fairy"
                damage = int((random.randint(65, 80) + platk + enemdef) / 3)
                if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Shirfty":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                    damage = int(damage / 2)
                    not_effective = True
            if move == "Iron Head":
                atk_type = "Steel"
                damage = int((random.randint(65, 80) + platk + enemdef) / 3)
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Blaziken":
                    damage = int(damage / 2)
                    not_effective = True
                if enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Lapras":
                    damage *= 2
                    supereffective = True
            if move == "Water Pulse":
                atk_type = "Water"
                damage = int((random.randint(80, 90) + enem_atk + pldef) / 3)
                if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Ninetails":
                    damage *= 2
                    supereffective = True
                if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Lapras":
                    damage = int(damage / 2)
                    not_effective = True

            enem_HP -= damage
            counter = False
        if attack:
            text4x = 450
            text5x = 700
            text4y = 823049
            if choice == "attack1":
                move = attacks[0]
            if choice == "attack2":
                move = attacks[1]
            if plspeed >= enem_speed:
                player_animation = True

                score_show = font.render(pokemon_used + " used " + move + "!", True, (black))
                if move == "Thunderbolt":
                    atk_type = "Electric"
                    damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Camerupt":
                        damage *= 0
                    if enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Togekiss":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Pikachu":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Iron Tail":
                    atk_type = "Steel"
                    damage = int((random.randint(70, 100) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                    if enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Lapras":
                        damage *= 2
                        supereffective = True
                if move == "Flamethrower":
                    atk_type = "Fire"
                    damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Tropius" and enem_pokemon_used == "Aggron":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Piplup" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Ninetails" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Garchomp":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Dragon Pulse":
                    atk_type = "Dragon"
                    damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Clefable":
                        damage *= 0
                if move == "Petal Blizzard":
                    atk_type = "Grass"
                    damage = int((random.randint(70, 90) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Piplup" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Swampert":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Ninetails" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Outrage":
                    atk_type = "Dragon"
                    damage = int((random.randint(80, 120) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Clefable":
                        damage *= 0
                if move == "Bite":
                    atk_type = "Dark"
                    damage = int((random.randint(60, 80) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Hydro Pump":
                    atk_type = "Water"
                    damage = int((random.randint(90, 110) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Lapras":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Surf":
                    atk_type = "Water"
                    damage = int((random.randint(80, 100) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Lapras":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Psychic":
                    atk_type = "Psychic"
                    damage = int((random.randint(80, 100) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Alakazam":
                        damage = int(damage / 2)
                        not_effective = True
                    if enem_pokemon_used == "Shirfty":
                        damage *= 0
                if move == "Thunder Punch":
                    atk_type = "Electric"
                    damage = int((random.randint(55, 75) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Camerupt":
                        damage *= 0
                    if enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Togekiss":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Pikachu":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Headbutt":
                    atk_type = "Normal"
                    damage = int((random.randint(80, 90) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Mamoswine":
                        damage = int(damage / 2)
                        not_effective = True
                    if enem_pokemon_used == "Gengar":
                        damage *= 0
                if move == "Earthquake":
                    atk_type = "Ground"
                    damage = int((random.randint(90, 110) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Gengar" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Pikachu" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Togekiss":
                        damage *= 0
                if move == "Ice Beam":
                    atk_type = "Ice"
                    damage = int((random.randint(80, 100) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Swellow" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Togekiss":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Lapras" or enem_pokemon_used == "Slowbro":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Sucker Punch":
                    atk_type = "Dark"
                    damage = int((random.randint(75, 80) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Razor Leaf":
                    atk_type = "Grass"
                    damage = int((random.randint(75, 85) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Piplup" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Swampert":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Ninetails" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Air Cutter":
                    atk_type = "Flying"
                    damage = int((random.randint(65, 80) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Torterra":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Pikachu" or enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Luxray":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Hurricane":
                    atk_type = "Flying"
                    damage = int((random.randint(95, 115) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Torterra":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Pikachu" or enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Luxray":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Steel Wing":
                    atk_type = "Steel"
                    damage = int((random.randint(75, 85) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                    if enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Lapras":
                        damage *= 2
                        supereffective = True
                if move == "Shadow Ball":
                    atk_type = "Dark"
                    damage = int((random.randint(70, 80) + platk + enemdef / 3))
                    if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Close Combat":
                    atk_type = "Fighting"
                    damage = int((random.randint(100, 120) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Buneary" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Lapras" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Snorlax":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Tropius" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Alakazam":
                        damage = int(damage / 2)
                        not_effective = True
                    if enem_pokemon_used == "Gengar":
                        damage *= 0
                if move == "Moonblast":
                    atk_type = "Fairy"
                    damage = int((random.randint(75, 95) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Shirfty":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Play Rough":
                    atk_type = "Fairy"
                    damage = int((random.randint(75, 90) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Shirfty":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Dazzling Gleam":
                    atk_type = "Fairy"
                    damage = int((random.randint(65, 80) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Shirfty":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Aggron" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Venusaur":
                        damage = int(damage / 2)
                        not_effective = True
                if move == "Iron Head":
                    atk_type = "Steel"
                    damage = int((random.randint(65, 80) + platk + enemdef) / 3)
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                    if enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff" or enem_pokemon_used == "Gengar" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Mamoswine" or enem_pokemon_used == "Togekiss" or enem_pokemon_used == "Lapras":
                        damage *= 2
                        supereffective = True
                if move == "Water Pulse":
                    atk_type = "Water"
                    damage = int((random.randint(80, 90) + enem_atk + pldef) / 3)
                    if enem_pokemon_used == "Charizard" or enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Typhlosion" or enem_pokemon_used == "Camerupt" or enem_pokemon_used == "Magcargo" or enem_pokemon_used == "Magmortar" or enem_pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Lapras":
                        damage = int(damage / 2)
                        not_effective = True
                enem_HP -= damage
                attack = False
                counter = True
            if plspeed < enem_speed:
                enemy_animation = True
                text4x = 450
                text5x = 700
                text4y = 823049
                atk_timer = 0
                if enem_attack == "Thunderbolt":
                    enem_atk_type = "Electric"
                    damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                    if enem_pokemon_used == "Garchomp" or enem_pokemon_used == "Swampert" or enem_pokemon_used == "Camerupt":
                        damage *= 0
                    if enem_pokemon_used == "Blastoise" or enem_pokemon_used == "Piplup" or enem_pokemon_used == "Slowbro" or enem_pokemon_used == "Swellow" or enem_pokemon_used == "Pelipper" or enem_pokemon_used == "Charizard" or enem_pokemon_used == "Togekiss":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Jolteon" or enem_pokemon_used == "Torterra" or enem_pokemon_used == "Tropius" or enem_pokemon_used == "Venusaur" or enem_pokemon_used == "Shirfty" or enem_pokemon_used == "Aggron" or enem_pokemon_used == "Raichu" or enem_pokemon_used == "Luxray" or enem_pokemon_used == "Pachirisu" or enem_pokemon_used == "Pikachu":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Iron Tail":
                    enem_atk_type = "Steel"
                    damage = int((random.randint(70, 100) + enem_atk + pldef) / 3)
                    if pokemon_used == "Charizard" or pokemon_used == "Magmortar" or pokemon_used == "Swampert" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Typhlosion" or pokemon_used == "Garchomp" or pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                    if pokemon_used == "Clefable" or pokemon_used == "Wigglytuff" or pokemon_used == "Gengar" or pokemon_used == "Slowbro" or pokemon_used == "Mamoswine" or pokemon_used == "Togekiss" or pokemon_used == "Lapras":
                        damage *= 2
                        supereffective = True
                if enem_attack == "Flamethrower":
                    enem_atk_type = "Fire"
                    damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                    if pokemon_used == "Venusaur" or pokemon_used == "Torterra" or pokemon_used == "Shirfty" or pokemon_used == "Tropius" or pokemon_used == "Aggron":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Piplup" or pokemon_used == "Blastoise" or pokemon_used == "Typhlosion" or pokemon_used == "Charizard" or pokemon_used == "Ninetails" or pokemon_used == "Camerupt" or pokemon_used == "Magmortar" or pokemon_used == "Blaziken" or pokemon_used == "Garchomp":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Dragon Pulse":
                    enem_atk_type = "Dragon"
                    damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                    if pokemon_used == "Garchomp":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Wigglytuff" or pokemon_used == "Clefable":
                        damage *= 0
                if enem_attack == "Petal Blizzard":
                    enem_atk_type = "Grass"
                    damage = int((random.randint(70, 90) + enem_atk + pldef) / 3)
                    if pokemon_used == "Piplup" or pokemon_used == "Blastoise" or pokemon_used == "Swampert":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Typhlosion" or pokemon_used == "Charizard" or pokemon_used == "Ninetails" or pokemon_used == "Camerupt" or pokemon_used == "Magmortar" or pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Outrage":
                    enem_atk_type = "Dragon"
                    damage = int((random.randint(80, 120) + enem_atk + pldef) / 3)
                    if pokemon_used == "Garchomp":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Wigglytuff" or pokemon_used == "Clefable":
                        damage *= 0
                if enem_attack == "Bite":
                    enem_atk_type = "Dark"
                    damage = int((random.randint(60, 80) + enem_atk + pldef) / 3)
                    if pokemon_used == "Grumpig" or pokemon_used == "Alakazam" or pokemon_used == "Gengar":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Blaziken" or pokemon_used == "Clefable" or pokemon_used == "Wigglytuff":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Hydro Pump":
                    enem_atk_type = "Water"
                    damage = int((random.randint(90, 110) + enem_atk + pldef) / 3)
                    if pokemon_used == "Charizard" or pokemon_used == "Blaziken" or pokemon_used == "Typhlosion" or pokemon_used == "Camerupt" or pokemon_used == "Magcargo" or pokemon_used == "Magmortar" or pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Venusaur" or pokemon_used == "Pelipper" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Lapras":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Surf":
                    enem_atk_type = "Water"
                    damage = int((random.randint(80, 100) + enem_atk + pldef) / 3)
                    if pokemon_used == "Charizard" or pokemon_used == "Blaziken" or pokemon_used == "Typhlosion" or pokemon_used == "Camerupt" or pokemon_used == "Magcargo" or pokemon_used == "Magmortar" or pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Venusaur" or pokemon_used == "Pelipper" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Lapras":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Psychic":
                    enem_atk_type = "Psychic"
                    damage = int((random.randint(80, 100) + enem_atk + pldef) / 3)
                    if pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Grumpig" or pokemon_used == "Aggron" or pokemon_used == "Alakazam":
                        damage = int(damage / 2)
                        not_effective = True
                    if pokemon_used == "Shirfty":
                        damage *= 0
                if enem_attack == "Thunder Punch":
                    enem_atk_type = "Electric"
                    damage = int((random.randint(55, 75) + enem_atk + pldef) / 3)
                    if pokemon_used == "Garchomp" or pokemon_used == "Swampert" or pokemon_used == "Camerupt":
                        damage *= 0
                    if pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Slowbro" or pokemon_used == "Swellow" or pokemon_used == "Pelipper" or pokemon_used == "Charizard" or pokemon_used == "Togekiss":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Jolteon" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Venusaur" or pokemon_used == "Shirfty" or pokemon_used == "Aggron" or pokemon_used == "Raichu" or pokemon_used == "Luxray" or pokemon_used == "Pachirisu" or pokemon_used == "Pikachu":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Headbutt":
                    enem_atk_type = "Normal"
                    damage = int((random.randint(80, 90) + enem_atk + pldef) / 3)
                    if pokemon_used == "Aggron" or pokemon_used == "Torterra" or pokemon_used == "Mamoswine":
                        damage = int(damage / 2)
                        not_effective = True
                    if pokemon_used == "Gengar":
                        damage *= 0
                if enem_attack == "Earthquake":
                    enem_atk_type = "Ground"
                    damage = int((random.randint(90, 110) + enem_atk + pldef) / 3)
                    if pokemon_used == "Gengar" or pokemon_used == "Aggron" or pokemon_used == "Pikachu" or pokemon_used == "Pachirisu" or pokemon_used == "Jolteon" or pokemon_used == "Luxray" or pokemon_used == "Raichu" or pokemon_used == "Garchomp" or pokemon_used == "Camerupt" or pokemon_used == "Blaziken" or pokemon_used == "Magcargo" or pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Charizard" or pokemon_used == "Swellow" or pokemon_used == "Tropius" or pokemon_used == "Togekiss":
                        damage *= 0
                if enem_attack == "Ice Beam":
                    enem_atk_type = "Ice"
                    damage = int((random.randint(80, 100) + enem_atk + pldef) / 3)
                    if pokemon_used == "Swellow" or pokemon_used == "Tropius" or pokemon_used == "Venusaur" or pokemon_used == "Togekiss":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Magmortar" or pokemon_used == "Camerupt" or pokemon_used == "Typhlosion" or pokemon_used == "Aggron" or pokemon_used == "Lapras" or pokemon_used == "Slowbro":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Sucker Punch":
                    enem_atk_type = "Dark"
                    damage = int((random.randint(75, 80) + enem_atk + pldef) / 3)
                    if pokemon_used == "Grumpig" or pokemon_used == "Alakazam" or pokemon_used == "Gengar":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Blaziken" or pokemon_used == "Clefable" or pokemon_used == "Wigglytuff":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Razor Leaf":
                    enem_atk_type = "Grass"
                    damage = int((random.randint(75, 85) + enem_atk + pldef) / 3)
                    if pokemon_used == "Piplup" or pokemon_used == "Blastoise" or pokemon_used == "Swampert":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Typhlosion" or pokemon_used == "Charizard" or pokemon_used == "Ninetails" or pokemon_used == "Camerupt" or pokemon_used == "Magmortar" or pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Air Cutter":
                    enem_atk_type = "Flying"
                    damage = int((random.randint(65, 80) + enem_atk + pldef) / 3)
                    if pokemon_used == "Venusaur" or pokemon_used == "Blaziken" or pokemon_used == "Tropius" or pokemon_used == "Torterra":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Pikachu" or pokemon_used == "Jolteon" or pokemon_used == "Pachirisu" or pokemon_used == "Luxray":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Hurricane":
                    enem_atk_type = "Flying"
                    damage = int((random.randint(95, 115) + enem_atk + pldef) / 3)
                    if pokemon_used == "Venusaur" or pokemon_used == "Blaziken" or pokemon_used == "Tropius" or pokemon_used == "Torterra":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Pikachu" or pokemon_used == "Jolteon" or pokemon_used == "Pachirisu" or pokemon_used == "Luxray":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Steel Wing":
                    enem_atk_type = "Steel"
                    damage = int((random.randint(75, 85) + enem_atk + pldef) / 3)
                    if pokemon_used == "Charizard" or pokemon_used == "Magmortar" or pokemon_used == "Swampert" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Typhlosion" or pokemon_used == "Garchomp" or pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                    if pokemon_used == "Clefable" or pokemon_used == "Wigglytuff" or pokemon_used == "Gengar" or pokemon_used == "Slowbro" or pokemon_used == "Mamoswine" or pokemon_used == "Togekiss" or pokemon_used == "Lapras":
                        damage *= 2
                        supereffective = True
                if enem_attack == "Shadow Ball":
                    enem_atk_type = "Dark"
                    damage = int((random.randint(70, 80) + enem_atk + pldef / 3))
                    if enem_pokemon_used == "Grumpig" or enem_pokemon_used == "Alakazam" or enem_pokemon_used == "Gengar":
                        damage *= 2
                        supereffective = True
                    if enem_pokemon_used == "Blaziken" or enem_pokemon_used == "Clefable" or enem_pokemon_used == "Wigglytuff":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Close Combat":
                    enem_atk_type = "Fighing"
                    damage = int((random.randint(100, 120) + enem_atk + pldef) / 3)
                    if pokemon_used == "Buneary" or pokemon_used == "Aggron" or pokemon_used == "Slowbro" or pokemon_used == "Lapras" or pokemon_used == "Mamoswine" or pokemon_used == "Snorlax":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Tropius" or pokemon_used == "Swellow" or pokemon_used == "Clefable" or pokemon_used == "Grumpig" or pokemon_used == "Togekiss" or pokemon_used == "Alakazam":
                        damage = int(damage / 2)
                        not_effective = True
                    if pokemon_used == "Gengar":
                        damage *= 0
                if enem_attack == "Moonblast":
                    enem_atk_type = "Fairy"
                    damage = int((random.randint(75, 95) + enem_atk + pldef) / 3)
                    if pokemon_used == "Garchomp" or pokemon_used == "Shirfty":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Aggron" or pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Play Rough":
                    enem_atk_type = "Fairy"
                    damage = int((random.randint(75, 90) + enem_atk + pldef) / 3)
                    if pokemon_used == "Garchomp" or pokemon_used == "Shirfty":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Aggron" or pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Dazzling Gleam":
                    enem_atk_type = "Fairy"
                    damage = int((random.randint(65, 80) + enem_atk + pldef) / 3)
                    if pokemon_used == "Garchomp" or pokemon_used == "Shirfty":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Aggron" or pokemon_used == "Gengar" or pokemon_used == "Venusaur":
                        damage = int(damage / 2)
                        not_effective = True
                if enem_attack == "Iron Head":
                    enem_atk_type = "Steel"
                    damage = int((random.randint(65, 80) + enem_atk + pldef) / 3)
                    if pokemon_used == "Charizard" or pokemon_used == "Magmortar" or pokemon_used == "Swampert" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Typhlosion" or pokemon_used == "Garchomp" or pokemon_used == "Blaziken":
                        damage = int(damage / 2)
                        not_effective = True
                    if pokemon_used == "Clefable" or pokemon_used == "Wigglytuff" or pokemon_used == "Gengar" or pokemon_used == "Slowbro" or pokemon_used == "Mamoswine" or pokemon_used == "Togekiss" or pokemon_used == "Lapras":
                        damage *= 2
                        supereffective = True
                if enem_attack == "Water Pulse":
                    enem_atk_type = "Water"
                    damage = int((random.randint(80, 90) + enem_atk + pldef) / 3)
                    if pokemon_used == "Charizard" or pokemon_used == "Blaziken" or pokemon_used == "Typhlosion" or pokemon_used == "Camerupt" or pokemon_used == "Magcargo" or pokemon_used == "Magmortar" or pokemon_used == "Ninetails":
                        damage *= 2
                        supereffective = True
                    if pokemon_used == "Venusaur" or pokemon_used == "Pelipper" or pokemon_used == "Blastoise" or pokemon_used == "Piplup" or pokemon_used == "Torterra" or pokemon_used == "Tropius" or pokemon_used == "Lapras":
                        damage = int(damage / 2)
                        not_effective = True
                score_show = font.render(enem_pokemon_used + " used " + enem_attack + "!", True, (black))
                plHP -= damage
                attack = False
                counter = True
        if atk_timer >= 719 and option <= 2 and plHP > 0 and enem_HP > 0:
            option = 1
        if supereffective:
            score_show6 = font2.render("Its Super Effective!", True, (black))
            text6x = 580
            text6y = 20
        if not_effective:
            score_show7 = font2.render("Its Not Very Effective...", True, (black))
            text7x = 500
            text7y = 20
        if not not_effective:
            text7x = 500
            text7y = 123781293
        if not supereffective:
            text6x = 580
            text6y = 200000
        if plHP <= 0:
            plHP = 0
        if enem_HP <= 0:
            enem_HP = 0
        if plHP <= 0 and atk_timer >= 359:
            plHP = 0
            if plspeed >= enem_speed:
                if atk_timer >= 719:
                    score_show = font.render(pokemon_used + " has fainted!", True, (black))
                    attack = False
                    counter = False
                if atk_timer >= 1000:
                    option = 1
                    attack = False
                    counter = False
                    plpkm_count -= 1
                    del team[0]
                    pokemon_used = str(team[0])
                    reset = True
            if plspeed < enem_speed:
                if atk_timer >= 359:
                    score_show = font.render(pokemon_used + " has fainted!", True, (black))
                    attack = False
                    counter = False
                if atk_timer >= 720:
                    option = 1
                    attack = False
                    counter = False
                    plpkm_count -= 1
                    del team[0]
                    pokemon_used = str(team[0])
                    reset = True
        if enem_HP <= 0 and atk_timer >= 359:
            enem_HP = 0
            if plspeed >= enem_speed:
                if atk_timer >= 359:
                    score_show = font.render(enem_pokemon_used + " has fainted!", True, (black))
                    attack = False
                    counter = False
                if atk_timer >= 720:
                    option = 1
                    attack = False
                    counter = False
                    enempkm_count -= 1
                    del enemteam[0]
                    enem_pokemon_used = enemteam[0]
                    enemreset = True
            if plspeed < enem_speed:
                if atk_timer >= 719:
                    score_show = font.render(enem_pokemon_used + " has fainted!", True, (black))
                    attack = False
                    counter = False
                if atk_timer >= 1000:
                    option = 1
                    attack = False
                    counter = False
                    enempkm_count -= 1
                    del enemteam[0]
                    enem_pokemon_used = enemteam[0]
                    enemreset = True
        if player_animation:
            plpkmx_change = 5
            if atk_timer == 5:
                plpkmx_change = 0
                plpkmx = 100
                player_animation = False
        if player_animation2:
            plpkmx_change = 5
            if atk_timer == 365:
                plpkmx_change = 0
                plpkmx = 100
                player_animation2 = False
        if enemy_animation:
            enempkmx_change = -5
            if atk_timer == 5:
                enempkmx_change = 0
                enempkmx = 600
                enemy_animation = False
        if enemy_animation2:
            enempkmx_change = -5
            if atk_timer == 365:
                enempkmx_change = 0
                enempkmx = 600
                enemy_animation2 = False
        if person == "red" and reset:
            if pokemon_used == "Pikachu":
                types = ["Electric"]
                attacks = pikachu_moves
                plpkmImg = pygame.image.load('pikachuback.png')
                plpkmx = 100
                plpkmy = 175
                plspeed = 100
                platk = 55
                pldef = 80  # lower def stat is better
                plHP = 110
            if pokemon_used == "Charizard":
                types = ["Fire", "Flying"]
                attacks = charizard_moves
                plspeed = 60
                platk = 90
                plHP = 150
                pldef = 50
                plpkmImg = pygame.image.load('charizardback.png')
                plpkmx = 100
                plpkmy = 170
            if pokemon_used == "Venusaur":
                types = ["Grass", "Poison"]
                attacks = venusaur_moves
                plspeed = 40
                platk = 70
                plHP = 150
                pldef = 55
                plpkmImg = pygame.image.load('venusaurback.png')
                plpkmx = 100
                plpkmy = 176
            if pokemon_used == "Blastoise":
                types = ["Water"]
                attacks = blastoise_moves
                plspeed = 60
                platk = 95
                plHP = 160
                pldef = 55
                plpkmImg = pygame.image.load('blastoiseback.png')
                plpkmx = 100
                plpkmy = 176
            if pokemon_used == "Snorlax":
                types = ["Normal"]
                attacks = snorlax_moves
                plspeed = 20
                platk = 110
                plHP = 180
                pldef = 20
                plpkmImg = pygame.image.load('snorlaxback.png')
                plpkmx = 100
                plpkmy = 193
            if pokemon_used == "Lapras":
                types = ["Ice", 'Water']
                attacks = lapras_moves
                plspeed = 50
                platk = 80
                plHP = 150
                pldef = 60
                plpkmImg = pygame.image.load('laprasback.png')
                plpkmx = 100
                plpkmy = 168
            reset = False
        if person == "leaf" and reset:
            if pokemon_used == "Venusaur":
                types = ["Grass", "Poison"]
                attacks = venusaur_moves
                plspeed = 40
                platk = 70
                plHP = 150
                pldef = 55
                plpkmImg = pygame.image.load('venusaurback.png')
                plpkmx = 100
                plpkmy = 176
            if pokemon_used == "Jolteon":
                types = ["Electric"]
                attacks = jolteon_moves
                plpkmImg = pygame.image.load('jolteonback.png')
                move = jolteon_moves
                plpkmx = 100
                plpkmy = 173
                pldef = 70
                plspeed = 100
                platk = 75
                plHP = 120
            if pokemon_used == "Wigglytuff":
                types = ["Fairy", "Normal"]
                attacks = wigglytuff_moves
                plspeed = 60
                platk = 70
                plHP = 140
                pldef = 70
                plpkmImg = pygame.image.load('wigglytuffback.png')
                plpkmx = 100
                plpkmy = 171
            if pokemon_used == "Ninetales":
                types = ["Fire"]
                attacks = ninetails_moves
                plspeed = 80
                platk = 80
                plHP = 170
                pldef = 60
                plpkmImg = pygame.image.load('Ninetalesback.png')
                plpkmx = 100
                plpkmy = 170
            if pokemon_used == "Gengar":
                types = ["Ghost", "Poison"]
                attacks = gengar_moves
                plspeed = 50
                platk = 110
                plHP = 180
                pldef = 60
                plpkmImg = pygame.image.load('gengarback.png')
                plpkmx = 100
                plpkmy = 178
            if pokemon_used == "Slowbro":
                types = ["Ice", "Water"]
                attacks = slowbro_moves
                plspeed = 30
                platk = 90
                plHP = 160
                pldef = 60
                plpkmImg = pygame.image.load('slowbroback.png')
                plpkmx = 100
                plpkmy = 184
            reset = False
        if person == "brendan" and reset:
            if pokemon_used == "Swampert":
                types = ["Water", "Ground"]
                plspeed = 40
                platk = 70
                plHP = 150
                pldef = 50
                plpkmImg = pygame.image.load('swampertback.png')
                plpkmx = 100
                plpkmy = 170
                attacks = swampert_moves
            if pokemon_used == "Shiftry":
                types = ["Grass", "Dark"]
                plpkmImg = pygame.image.load('shiftryback.png')
                plpkmx = 100
                pldef = 60
                plpkmy = 177
                plspeed = 100
                platk = 75
                plHP = 120
                attacks = shirfty_moves
            if pokemon_used == "Swellow":
                types = ["Flying", "Normal"]
                plspeed = 90
                pldef = 55
                platk = 80
                plHP = 140
                plpkmImg = pygame.image.load('swellowback.png')
                plpkmx = 100
                plpkmy = 179
                attacks = swellow_moves
            if pokemon_used == "Camerupt":
                types = ["Fire", "Ground"]
                plspeed = 50
                pldef = 55
                platk = 90
                plHP = 180
                plpkmImg = pygame.image.load('cameruptback.png')
                plpkmx = 100
                plpkmy = 192
                attacks = camerupt_moves
            if pokemon_used == "Aggron":
                types = ["Steel", "Rock"]
                plspeed = 70
                pldef = 30
                platk = 110
                plHP = 180
                attacks = aggron_moves
                plpkmImg = pygame.image.load('aggronback.png')
                plpkmx = 100
                plpkmy = 175
            if pokemon_used == "Grumpig":
                types = ["Psychic"]
                plspeed = 60
                pldef = 70
                platk = 80
                plHP = 130
                plpkmImg = pygame.image.load('grumpigback.png')
                plpkmx = 100
                plpkmy = 168
                attacks = grumpig_moves
            reset = False
        if person == "may" and reset:
            if pokemon_used == "Blaziken":
                types = ["Fire", "Fighting"]
                plspeed = 40
                pldef = 50
                platk = 70
                plHP = 150
                attacks = blaziken_moves
                plpkmImg = pygame.image.load('blazikenback.png')
                plpkmx = 100
                plpkmy = 155
            if pokemon_used == "Tropius":
                types = ["Grass", "Flying"]
                plpkmImg = pygame.image.load('tropiusback.png')
                plpkmx = 100
                pldef = 60
                plpkmy = 177
                plspeed = 100
                platk = 75
                plHP = 120
                attacks = tropius_moves
            if pokemon_used == "Swellow":
                types = ["Flying", "Normal"]
                plspeed = 90
                pldef = 55
                platk = 80
                plHP = 140
                plpkmImg = pygame.image.load('swellowback.png')
                plpkmx = 100
                plpkmy = 179
                attacks = swellow_moves
            if pokemon_used == "Raichu":
                types = ["Electric"]
                plspeed = 90
                pldef = 60
                platk = 90
                plHP = 150
                plpkmImg = pygame.image.load('raichuback.png')
                plpkmx = 100
                plpkmy = 180
                attacks = raichu_moves
            if pokemon_used == "Pelipper":
                types = ["Water", "Flying"]
                plspeed = 80
                pldef = 65
                platk = 80
                plHP = 140
                plpkmImg = pygame.image.load('pelipperback.png')
                plpkmx = 100
                plpkmy = 175
                attacks = pelipper_moves
            if pokemon_used == "Magcargo":
                types = ["Fire"]
                pldef = 60
                plspeed = 60
                platk = 80
                plHP = 160
                plpkmImg = pygame.image.load('magcargoback.png')
                plpkmx = 100
                plpkmy = 182
                attacks = magcargo_moves
            reset = False
        if person == "lucas" and reset:
            if pokemon_used == "Torterra":
                types = ["Grass", "Ground"]
                plspeed = 50
                pldef = 40
                platk = 90
                plHP = 175
                plpkmImg = pygame.image.load('torterraback.png')
                plpkmx = 100
                plpkmy = 167
                attacks = torterra_moves
            if pokemon_used == "Alakazam":
                types = ["Psychic"]
                pldef = 55
                plpkmImg = pygame.image.load('alakazamback.png')
                plpkmx = 100
                plpkmy = 171
                plspeed = 70
                platk = 85
                plHP = 160
                attacks = alakazam_moves
            if pokemon_used == "Clefable":
                types = ["Fairy", "Normal"]
                pldef = 55
                plspeed = 70
                platk = 80
                plHP = 160
                plpkmImg = pygame.image.load('clefableback.png')
                plpkmx = 100
                plpkmy = 183
                attacks = clefable_moves
            if pokemon_used == "Magmortar":
                types = ["Fire"]
                pldef = 50
                plspeed = 80
                platk = 90
                plHP = 180
                plpkmImg = pygame.image.load('magmortarback.png')
                plpkmx = 100
                plpkmy = 175
                attacks = magmortar_moves
            if pokemon_used == "Luxray":
                types = ["Electric"]
                pldef = 65
                plspeed = 95
                platk = 110
                plHP = 180
                plpkmImg = pygame.image.load('luxrayback.png')
                plpkmx = 100
                plpkmy = 157
                attacks = luxray_moves
            if pokemon_used == "Garchomp":
                types = ["Dragon", "Ground"]
                pldef = 45
                plspeed = 60
                platk = 95
                plHP = 170
                attacks = garchomp_moves
                plpkmImg = pygame.image.load('garchompback.png')
                plpkmx = 100
                plpkmy = 157
            reset = False
        if person == "dawn" and reset:
            if pokemon_used == "Piplup":
                types = ["Water"]
                pldef = 80
                plspeed = 50
                platk = 90
                plHP = 130
                plpkmImg = pygame.image.load('piplupback.png')
                plpkmx = 100
                plpkmy = 175
                attacks = piplup_moves
            if pokemon_used == "Buneary":
                types = ["Normal"]
                pldef = 75
                plpkmImg = pygame.image.load('bunearyback.png')
                plpkmx = 100
                plpkmy = 155
                plspeed = 70
                platk = 85
                plHP = 160
                attacks = buneary_moves
            if pokemon_used == "Pachirisu":
                types = ["Electric"]
                pldef = 65
                plspeed = 70
                platk = 80
                plHP = 155
                plpkmImg = pygame.image.load('pachirisuback.png')
                plpkmx = 100
                plpkmy = 161
                attacks = pachirisu_moves
            if pokemon_used == "Mamoswine":
                types = ["Ice", "Rock"]
                pldef = 50
                plspeed = 80
                platk = 90
                plHP = 180
                plpkmImg = pygame.image.load('mamoswineback.png')
                plpkmx = 100
                plpkmy = 175
                attacks = mamoswine_moves
            if pokemon_used == "Typhlosion":
                types = ["Fire"]
                pldef = 50
                plspeed = 95
                platk = 110
                plHP = 180
                plpkmImg = pygame.image.load('typhlosionback.png')
                plpkmx = 100
                plpkmy = 170
                attacks = typhlosion_moves
            if pokemon_used == "Togekiss":
                types = ["Fairy", "Flying"]
                pldef = 45
                plspeed = 60
                platk = 95
                plHP = 170
                attacks = togekiss_moves
                plpkmImg = pygame.image.load('togekissback.png')
                plpkmx = 100
                plpkmy = 182
            reset = False
        # pkm for enemy
        if enemy == "Red" and enemreset:
            if enem_pokemon_used == "Pikachu":
                enem_types = ["Electric"]
                enemdef = 80
                enempkmImg = pygame.image.load('pikachufront.png')
                enempkmy = 140
                enem_speed = 100
                enem_atk = 55
                enem_HP = 100
                enem_attacks = pikachu_moves
            if enem_pokemon_used == "Charizard":
                enem_types = ["Fire", "Flying"]
                enemdef = 50
                enem_speed = 60
                enem_atk = 90
                enem_HP = 150
                enem_attacks = charizard_moves
                enempkmImg = pygame.image.load('charizardfront.png')
            if enem_pokemon_used == "Venusaur":
                enem_types = ["Grass", "Poison"]
                enem_speed = 40
                enemdef = 55
                enem_atk = 70
                enem_HP = 150
                enem_attacks = venusaur_moves
                enempkmImg = pygame.image.load('venusaurfront.png')
            if enem_pokemon_used == "Blastoise":
                enem_types =["Water"]
                enemdef = 55
                enem_speed = 60
                enem_atk = 95
                enem_HP = 160
                enem_attacks = blastoise_moves
                enempkmImg = pygame.image.load('blastoisefront.png')
            if enem_pokemon_used == "Snorlax":
                enem_types = ["Normal"]
                enemdef = 20
                enem_speed = 20
                enem_atk = 110
                enem_HP = 180
                enem_attacks = snorlax_moves
                enempkmImg = pygame.image.load('snorlaxfront.png')
            if enem_pokemon_used == "Lapras":
                enem_types = ["Ice", "Water"]
                enemdef = 60
                enem_speed = 50
                enem_atk = 80
                enem_HP = 150
                enem_attacks = lapras_moves
                enempkmImg = pygame.image.load('laprasfront.png')
            enemreset = False
        if enemy == "Leaf" and enemreset:
            if enem_pokemon_used == "Venusaur":
                enem_types = ["Grass", "Poison"]
                enemdef = 55
                enem_speed = 40
                enem_atk = 70
                enem_HP = 150
                enem_attacks = venusaur_moves
                enempkmImg = pygame.image.load('venusaurfront.png')
            if enem_pokemon_used == "Jolteon":
                enem_types = ["Electric"]
                enemdef = 70
                enem_attacks = jolteon_moves
                enempkmImg = pygame.image.load('jolteonfront.png')
                enem_speed = 100
                enem_atk = 75
                enem_HP = 120
            if enem_pokemon_used == "Wigglytuff":
                enem_types = ["Normal", "Fairy"]
                enemdef = 70
                enem_speed = 60
                enem_atk = 70
                enem_HP = 140
                enem_attacks = wigglytuff_moves
                enempkmImg = pygame.image.load('wigglytufffront.png')
            if enem_pokemon_used == "Ninetales":
                enem_types = ["Fire"]
                enemdef = 60
                enem_speed = 80
                enem_atk = 80
                enem_HP = 170
                enem_attacks = ninetails_moves
                enempkmImg = pygame.image.load('Ninetalesfront.png')
            if enem_pokemon_used == "Gengar":
                enem_types = ["Ghost", "Poison"]
                enemdef = 55
                enem_speed = 50
                enem_atk = 110
                enem_HP = 180
                enem_attacks = gengar_moves
                enempkmImg = pygame.image.load('gengarfront.png')
            if enem_pokemon_used == "Slowbro":
                enem_types = ["Ice", "Water"]
                enem_speed = 30
                enemdef = 60
                enem_atk = 90
                enem_HP = 160
                enem_attacks = slowbro_moves
                enempkmImg = pygame.image.load('slowbrofront.png')
            enemreset = False
        if enemy == "Brendan" and enemreset:
            if enem_pokemon_used == "Swampert":
                enem_types = ["Water", "Ground"]
                enem_attacks = swampert_moves
                enemdef = 50
                enem_speed = 40
                enem_atk = 70
                enem_HP = 150
                enempkmImg = pygame.image.load('swampertfront.png')
            if enem_pokemon_used == "Shiftry":
                enem_types = ["Grass", "Dark"]
                enempkmImg = pygame.image.load('shiftryfront.png')
                enem_speed = 100
                enemdef = 60
                enem_attacks = shirfty_moves
                enem_atk = 75
                enem_HP = 120
            if enem_pokemon_used == "Swellow":
                enem_types = ["Normal", "Flying"]
                enem_speed = 90
                enemdef = 55
                enem_attacks = swellow_moves
                enem_atk = 80
                enem_HP = 140
                enempkmImg = pygame.image.load('swellowfront.png')
            if enem_pokemon_used == "Camerupt":
                enem_types = ["Fire", "Ground"]
                enem_speed = 50
                enemdef = 55
                enem_atk = 90
                enem_HP = 180
                enem_attacks = camerupt_moves
                enempkmImg = pygame.image.load('cameruptfront.png')
            if enem_pokemon_used == "Aggron":
                enem_types = ["Steel", "Rock"]
                enem_speed = 70
                enemdef = 30
                enem_atk = 110
                enem_HP = 180
                enem_attacks = aggron_moves
                enempkmImg = pygame.image.load('aggronfront.png')
            if enem_pokemon_used == "Grumpig":
                enem_types = ["Psychic"]
                enem_speed = 60
                enemdef = 70
                enem_atk = 80
                enem_HP = 130
                enem_attacks = grumpig_moves
                enempkmImg = pygame.image.load('grumpigfront.png')
            enemreset = False
        if enemy == "May" and enemreset:
            enemdef = 55
            if enem_pokemon_used == "Blaziken":
                enem_types = ["Fire", "Fighting"]
                enem_speed = 40
                enem_atk = 70
                enemdef = 50
                enem_HP = 150
                enem_attacks = blaziken_moves
                enempkmImg = pygame.image.load('blazikenfront.png')
            if enem_pokemon_used == "Tropius":
                enem_types = ["Grass", "Flying"]
                enemdef = 60
                enempkmImg = pygame.image.load('tropiusfront.png')
                enem_speed = 100
                enem_atk = 75
                enem_HP = 120
                enem_attacks = tropius_moves
            if enem_pokemon_used == "Swellow":
                enem_types = ["Normal", "Flying"]
                enemdef = 55
                enem_speed = 90
                enem_atk = 80
                enem_HP = 140
                enem_attacks = swellow_moves
                enempkmImg = pygame.image.load('swellowfront.png')
            if enem_pokemon_used == "Raichu":
                enem_types = ["Electric"]
                enemdef = 60
                enem_speed = 90
                enem_atk = 90
                enem_HP = 150
                enem_attacks = raichu_moves
                enempkmImg = pygame.image.load('raichufront.png')
            if enem_pokemon_used == "Pelipper":
                enem_types = ["Water", "Flying"]
                enemdef = 65
                enem_speed = 80
                enem_atk = 80
                enem_HP = 140
                enem_attacks = pelipper_moves
                enempkmImg = pygame.image.load('pelipperfront.png')
            if enem_pokemon_used == "Magcargo":
                enem_types = ["Fire"]
                enemdef = 60
                enem_speed = 60
                enem_atk = 80
                enem_HP = 160
                enem_attacks = magcargo_moves
                enempkmImg = pygame.image.load('magcargofront.png')
            enemreset = False
        if enemy == "Lucas" and enemreset:
            if enem_pokemon_used == "Torterra":
                enem_types = ["Grass", "Ground"]
                enemdef = 40
                enem_speed = 50
                enem_atk = 90
                enem_HP = 175
                enem_attacks = torterra_moves
                enempkmImg = pygame.image.load('torterrafront.png')
            if enem_pokemon_used == "Alakazam":
                enem_types = ["Psychic"]
                enempkmImg = pygame.image.load('alakazamfront.png')
                enem_speed = 70
                enem_attacks = alakazam_moves
                enemdef = 55
                enem_atk = 85
                enem_HP = 160
            if enem_pokemon_used == "Clefable":
                enem_types = ["Normal", "Fairy"]
                enem_speed = 70
                enemdef = 55
                enem_atk = 80
                enem_HP = 160
                enem_attacks = clefable_moves
                enempkmImg = pygame.image.load('clefablefront.png')
            if enem_pokemon_used == "Magmortar":
                enem_types = ["Fire"]
                enemdef = 50
                enem_speed = 80
                enem_atk = 90
                enem_HP = 180
                enem_attacks = magmortar_moves
                enempkmImg = pygame.image.load('magmortarfront.png')
            if enem_pokemon_used == "Luxray":
                enem_types = ["Electric"]
                enemdef = 65
                enem_speed = 95
                enem_atk = 110
                enem_attacks = luxray_moves
                enem_HP = 180
                enempkmImg = pygame.image.load('luxrayfront.png')
            if enem_pokemon_used == "Garchomp":
                enem_types = ["Dragon", 'Ground']
                enemdef = 45
                enem_speed = 60
                enem_atk = 95
                enem_HP = 170
                enem_attacks = garchomp_moves
                enempkmImg = pygame.image.load('garchompfront.png')
            enemreset = False
        if enemy == "Dawn" and enemreset:
            if enem_pokemon_used == "Piplup":
                enem_types = ["Water"]
                enem_speed = 50
                enemdef = 80
                enem_atk = 90
                enem_HP = 130
                enem_attacks = piplup_moves
                enempkmImg = pygame.image.load('piplupfront.png')
            if enem_pokemon_used == "Buneary":
                enem_types = ["Normal"]
                enempkmImg = pygame.image.load('bunearyfront.png')
                enem_speed = 70
                enemdef = 70
                enem_atk = 85
                enem_HP = 160
                enem_attacks = buneary_moves
            if enem_pokemon_used == "Pachirisu":
                enem_types = ["Electric"]
                enem_speed = 70
                enemdef = 65
                enem_atk = 80
                enem_HP = 155
                enem_attacks = pachirisu_moves
                enempkmImg = pygame.image.load('pachirisufront.png')
            if enem_pokemon_used == "Mamoswine":
                enem_types = ["Ice", "Rock"]
                enemdef = 50
                enem_speed = 80
                enem_atk = 90
                enem_HP = 180
                enem_attacks = mamoswine_moves
                enempkmImg = pygame.image.load('mamoswinefront.png')
            if enem_pokemon_used == "Typhlosion":
                enem_types = ["Fire"]
                enem_speed = 95
                enemdef = 50
                enem_atk = 110
                enem_HP = 180
                enem_attacks = typhlosion_moves
                enempkmImg = pygame.image.load('typhlosionfront.png')
            if enem_pokemon_used == "Togekiss":
                enem_types = ["Fairy", "Flying"]
                enemdef = 55
                enem_speed = 60
                enem_atk = 95
                enem_HP = 170
                enem_attacks = togekiss_moves
                enempkmImg = pygame.image.load('togekissfront.png')
            enemreset = False
        cx += c_change
        cy += cy_change
        ix += ix_change
        enemx1 += enemx1_change
        iy += iy_change
        pickedx = 2132
        pickedy = 1782
        bg(bgx, bgy)
        battleem(bex, bey)
        enemy1(enemx1, enem1y)
        intro(ix, iy)
        enempkm(enempkmx, enempkmy)
        plpkm(plpkmx, plpkmy)
        op1(op1x, op1y)
        op2(op2x, op1y)
        first_move = attacks[0]
        second_move = attacks[1]
        if plspeed >= enem_speed and plHP > 0 and enem_HP > 0 and attack:
            score_show = font.render(str(pokemon_used) + " used " + move + "!", True, (black))
        if enem_speed > plspeed and atk_timer >= 359 and plHP > 0 and enem_HP > 0 and counter:
            score_show = font.render(pokemon_used + " used " + move + "!", True, (black))
        if enem_speed > plspeed and atk_timer < 359 and plHP > 0 and enem_HP > 0:
            score_show = font.render(enem_pokemon_used + " used " + enem_attack + "!", True, (black))
        if plspeed >= enem_speed and atk_timer >= 359 and plHP > 0 and enem_HP > 0:
            score_show = font.render(enem_pokemon_used + " used " + enem_attack + "!", True, (black))
        score_show2 = font.render(pokemon_used + " HP: " + str(plHP), True, (black))
        score_show3 = font.render(enem_pokemon_used + " HP: " + str(enem_HP), True, (black))
        score_show4 = font2.render(first_move , True, (black))
        score_show5 = font2.render(second_move, True, (black))
        gameDisplay.blit(score_show, (textX, textY))
        gameDisplay.blit(score_show2, (text2X, text2Y))
        gameDisplay.blit(score_show3, (text2X, text3Y))
        gameDisplay.blit(score_show4, (text4x, text4y))
        gameDisplay.blit(score_show5, (text5x, text4y))
        gameDisplay.blit(score_show6, (text6x, text6y))
        gameDisplay.blit(score_show7, (text7x, text7y))
        plpkmx += plpkmx_change
        enempkmx += enempkmx_change
        cursor(cx, cy)
        pygame.display.update()
        clock.tick(60)
    except IndexError:
        if enempkm_count == 0:
            print("You win the battle!")
            quit()
        if plpkm_count == 0:
            print("You meet defeat. You lose the battle.")
            quit()