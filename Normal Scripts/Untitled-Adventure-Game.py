#this is my first game in python.
import time
import random
HP = 100
bow_ammo = 10
max_damage_taken = 50
min_damage_taken = 10
question_answered = False
attack_damage = random.randint(10, 75)
damage_taken = random.randint(min_damage_taken, max_damage_taken)
play_game = input("Would You Like To Play This Game?(y/n): ")
# HP = HP - 10(just a note for me so that that i remember how to take away value from a variable)
#this game is about 90-95% complete. Please do not type in any incorrect inputs.
#I have not added everything there.
if play_game == "can i just skip the game":
    time.sleep(1)
    print("Lol u win!")
    time.sleep(5)
    print("No seriously you beat the game cause of this easter egg.")

if play_game != "yes" and play_game != "y" and play_game != "n" and play_game != "no":
    print("Invalid Input. You are such an idiot.")
    time.sleep(1)
    play_game = input("Would You Like To Play This Game?(y/n): ")

if play_game == "n" or play_game == "no":
    print("What are you doing here? You ran the code, so why aren't you playing?")
    time.sleep(3)
    print("Get out.")
    time.sleep(2)
    print("GET OUT WHY ARE YOU STILL HERE")
#why did u say no

#pls dont cheat and look at the code. maybe if ur finished then you can
#btw the loading thing just makes the game feel cool in my opinion.
if play_game == "y" or play_game == "yes":
    name = input("What is your name?: ")
    print("Good.")
    time.sleep(2)
    print("Loading Story.....")
    time.sleep(5)
    print("1% finished")
    time.sleep(0.5)
    print("2% finished")
    time.sleep(0.5)
    print("3% finished")
    time.sleep(0.5)
    print("4% finished")
    time.sleep(0.5)
    print("6% finished")
    time.sleep(0.5)
    print("10% finished")
    time.sleep(3)
    print("30% finished")
    time.sleep(1)
    print("37% finished")
    time.sleep(2)
    print("51% finished")
    time.sleep(1)
    print("69% finished(nice)")
    time.sleep(5)
    print("80% finished")
    time.sleep(1)
    print("85% finished")
    time.sleep(1)
    print("90% finished")
    time.sleep(2)
    print("100% finished")
    time.sleep(0.2)
    print("Story Loaded!")
    time.sleep(1)
    print("You are in your cabin in a dark stormy night(very cliche but ok)")
    time.sleep(1)
    print("Your HP:")
    print(HP)
    print("Bow Ammo:")
    print(bow_ammo)
    print("Attack Damage:")
    print("10-75 HP")
    leavehouse = input("Do you wish to leave you cabin?(y/n): ")
    if leavehouse.lower() == "no" or leavehouse.lower() == "n":
        print("You went to sleep and waited till Dawn.")
        time.sleep(1)
        leavehouseatdawn = input("Do you wish to leave your cabin now?(y/n): ")

        if leavehouseatdawn.lower() == "no" or leavehouseatdawn.lower == "n":
            print("You are so lazy. THIS IS NOT AN OPTION!")
            time.sleep(1)
            leavehouseatdawn = input("Do you wish to leave your cabin now?(y/n): ")

        if leavehouseatdawn.lower() == "yes" or "y":
            print("You leave your cabin.")
            time.sleep(1)
            print("A person walks up to you.")
            time.sleep(2)
            print("Person: Hello "+name+". We are aware of your abilities.")
            time.sleep(2)
            print(name+": Why did you come to me?")
            time.sleep(2)
            print("Person: Please. Our king has been captured by an evil monster.")
            time.sleep(2)
            print(name+": An evil monster? Who?")
            time.sleep(2)
            print("Person: We do not speak of this name.")
            time.sleep(1)
            print("Person: But since it's you that I'm talking too you, I will tell you.")
            time.sleep(2)
            print("Person: His name is Zork.")
            time.sleep(1)
            print("Person: Enter his castle and enter the holding cells and rescue our leader!")
            time.sleep(1)
            rescueleader = input("Rescue Their King?: ")
            if rescueleader.lower() == "y" or rescueleader.lower() == "yes":
                time.sleep(1)
                print(name+": Ok. I will help.")
                time.sleep(1)
                print(name+": I just need some items.")
                time.sleep(2)
                print("The Person Gave You better weapons!")
                print("Your HP:")
                print(HP)
                print("Bow Ammo:")
                bow_ammo = bow_ammo + 10
                attack_damage = random.randint(20, 75)
                print(bow_ammo)
                print("Attack Damage:")
                print("20-75 HP")
                time.sleep(2)
                print("You began your quest.")
                time.sleep(1)
                print("You are walking on a rocky path.")
                time.sleep(1)
                print("You find a fork in the path.")
                leftorright1 = input("Do you go left or right?: ")
                if leftorright1.lower() == "left":
                    print("You go the left path.")
                    time.sleep(1)
                    print("You obliviously trespass into a monsters property and it attacks you.")
                    time.sleep(1)
                    print("You get killed since you suck at making good decisions.")
                if leftorright1 == "mid":
                    #this is an easter egg!
                    print("You went towards the middle.")
                    time.sleep(1)
                    print("U sneaked towards the castle, where you end up in the same room as Zork")
                    time.sleep(1)
                    killhim = input("Attempt to kill him?")
                    if killhim.lower() == "y" or killhim == "yes":
                        print("You sneaked towards him and stabbed him.")
                        time.sleep(1)
                        print("Zork died.")
                        time.sleep(1)
                        print("You put his body in the nearby closet where it will never be found again.")
                        time.sleep(1)
                        print("You make your way to the holding cells, where you rescue the leader.")
                        time.sleep(1)
                        print("You also make it back home safetly, and you are now a happy person.")
                        time.sleep(1)
                        print("Thank you for finding this easter egg, and thanks for playing!")
                        time.sleep(1)
                        print("You win!")
                        #ending3
                    if killhim.lower() == "n" or "no":
                        print("You stalled, and you were revealed.")
                        time.sleep(1)
                        print("With quick reflexes, Zork killed you.")
                        time.sleep(1)
                        print("Game over.")
                if leftorright1.lower() == "right":
                    print("You take the right path. Literally!")
                    time.sleep(1)
                    print("You can start seeing the large castle that Zork owns.")
                    time.sleep(1)
                    print("*Pokemon Battle Music Starts Playing*")
                    time.sleep(1)
                    print("You have encountered a wild Pig!")
                    time.sleep(1)
                    print("Your HP:")
                    print(HP)
                    print("Bow Ammo:")
                    print(bow_ammo)
                    print("Attack Damage:")
                    print("20-75 HP")
                    enemyhp1 = 80
                    enemyalive = True
                    print("Enemy HP:")
                    print(enemyhp1)
                    #first fight. You can run if you want!
                    while enemyalive == True and HP > 1:
                        whatdoyoudo = input("What Do You Do?(run/attack): ")
                        if whatdoyoudo.lower() == "run":
                            time.sleep(1)
                            print("You ran away safetly!")
                            enemyalive = False
                        if whatdoyoudo.lower() == "attack":
                            time.sleep(1)
                            weaponuse1 = input("Which weapon do you use?(bow/sword): ")
                            if weaponuse1.lower() == "bow":
                                if bow_ammo == 0:
                                    print("You are out of ammo!")
                                attack_damage = random.randint(20, 75)
                                print("You did:")
                                print(attack_damage)
                                print("Damage!")
                                enemyhp1 = enemyhp1 - attack_damage
                                bow_ammo = bow_ammo - 1
                                print("Bow Ammo:")
                                print(bow_ammo)
                                if enemyhp1 < 0:
                                    enemyhp1 = 0
                                time.sleep(1)
                                print("Enemy HP:")
                                print(enemyhp1)
                                time.sleep(1)
                                print("The Pig Is Too Slow To do anything!")
                                if enemyhp1 <= 0:
                                    print("You won the battle!")
                                    enemyalive = False
                            if weaponuse1 == "sword":
                                attack_damage = random.randint(20, 75)
                                print("You did:")
                                print(attack_damage)
                                print("Damage!")
                                enemyhp1 = enemyhp1 - attack_damage
                                if enemyhp1 < 0:
                                    enemyhp1 = 0
                                time.sleep(1)
                                print("Enemy HP:")
                                print(enemyhp1)
                                print("The Pig Is Too Slow To do anything!")
                                if enemyhp1 <= 0:
                                    print("You won the battle!")
                                    enemyalive = False
                    print("You start to head you way towards the castle.")
                    time.sleep(1)
                    print("You seem tired.")
                    time.sleep(1)
                    rest1 = input("Rest?(y/n): ")
                    if rest1 == "yes" or rest1 == "y":
                        time.sleep(1)
                        print("You took a small rest.")
                        HP = HP + 75
                        print("You Gained some HP!")
                        time.sleep(1)
                        print("Your HP:")
                        print(HP)
                        rest1 = "no"
                    if rest1 == "n" or rest1 == "no":
                        time.sleep(1)
                        print("You continue your way to the castle.")
                        time.sleep(1)
                        print("You eventually reach the castle.")
                        time.sleep(1)
                        print("Suddenly, a castle guard notices you.")
                        time.sleep(2)
                        print("!")
                        print("Castle Guard: You are an intruder! Prepare to be DESTROYED!")
                        time.sleep(1)
                        print("*More pokemon battle music starts playing*")
                        time.sleep(1)
                        enemyalive2 = True
                        enemyhp2 = 120
                        print("Your HP:")
                        print(HP)
                        print("Bow Ammo:")
                        print(bow_ammo)
                        print("Attack Damage:")
                        print("20-75 HP")
                        print("Enemy HP:")
                        print(enemyhp2)
#2nd battle!
                        while enemyalive2 == True and HP > 1:
                            whatdoyoudo2 = input("What Do You Do?(run/attack): ")
                            if whatdoyoudo2 == "run":
                                time.sleep(1)
                                print("You attempted to run away but you were stabbed.")
                                time.sleep(1)
                                print("YOU DIED!")
                            if whatdoyoudo2 == "attack":
                                time.sleep(1)
                                weaponuse2 = input("Which weapon do you use?(bow/sword): ")
                                if weaponuse2 == "bow":
                                    if bow_ammo == 0:
                                        print("You are out of ammo!")
                                    attack_damage = random.randint(20, 75)
                                    print("You did:")
                                    print(attack_damage)
                                    print("Damage!")
                                    enemyhp2 = enemyhp2 - attack_damage
                                    bow_ammo = bow_ammo - 1
                                    print("Bow Ammo:")
                                    print(bow_ammo)
                                    if enemyhp2 < 0:
                                        enemyhp2 = 0
                                    time.sleep(1)
                                    print("Enemy HP:")
                                    print(enemyhp2)
                                    time.sleep(1)
                                    if enemyhp2 <= 0:
                                        print("You won the battle!")
                                        enemyalive2 = False
                                    if enemyalive2 == True:
                                        print("The enemy attacked you back!")
                                        time.sleep(1)
                                        damage_taken = random.randint(min_damage_taken, max_damage_taken)
                                        HP = HP - damage_taken
                                    if HP <= 0:
                                        print("You lost the battle and died.")
                                        print("Game Over.")
                                        enemyalive2 = False
                                    if HP < 0:
                                        HP = 0
                                        enemyalive2 = False
                                    time.sleep(1)
                                    print("Your HP:")
                                    print(HP)
                                if weaponuse2 == "sword":
                                    attack_damage = random.randint(20, 75)
                                    print("You did:")
                                    print(attack_damage)
                                    print("Damage!")
                                    enemyhp2 = enemyhp2 - attack_damage
                                    if enemyhp2 < 0:
                                        enemyhp2 = 0
                                    time.sleep(1)
                                    print("Enemy HP:")
                                    print(enemyhp2)
                                    time.sleep(1)
                                    if enemyhp2 <= 0:
                                        print("You won the battle!")
                                        enemyalive2 = False
                                    if enemyalive2 == True:
                                        print("The enemy attacked you back!")
                                        time.sleep(1)
                                        damage_taken = random.randint(min_damage_taken, max_damage_taken)
                                        HP = HP - damage_taken
                                    if HP <= 0:
                                        print("You lost the battle and died.")
                                    if HP < 0:
                                        HP = 0
                                    time.sleep(1)
                                    print("Your HP:")
                                    print(HP)
                                    '''
                                    |    |    |------  |       |      |-------|  |-|
                                    |    |    |        |       |      |       |  | |
                                    |----|    |-----   |       |      |       |  |_|
                                    |    |    |        |       |      |       |   _
                                    |    |    |______  |_____  |_____ |_______|  |_|
                                    '''
                                    #idk what this is
                                    #i was bored.
                if enemyalive2 == False:
                    print("You went further into the castle, stealthily.")
                    time.sleep(1)
                    leftorright2 = input("There's a path fork along the way in the castle(left/right): ")
                    time.sleep(1)
                    if leftorright2 == "left":
                        print("You took the left path.")
                        time.sleep(1)
                        print("You see the holding cells.")
                        enterholdcells = input("Enter The Holding Cells?(y/n): ")
                        if enterholdcells == "no" or enterholdcells == "n":
                            print("WHY! WHY DID YOU NOT PICK YES!?!?!?!?!?!?!")
                            time.sleep(1)
                            print("Game Over. You can't play this game.")
                        if enterholdcells == "yes" or enterholdcells == "y":
                            time.sleep(1)
                            print("You entered the holding cells.")
                            time.sleep(1)
                            print("You hear a noise of distress.")
                            time.sleep(1)
                            print("????: Help! Please! I've been kidnapped!")
                            time.sleep(2)
                            print("You analyze the noise and walk towards it.")
                            time.sleep(2)
                            print("It turns out it was the leader that was kidnapped.")
                            time.sleep(2)
                            rescuehim = input("Escape with him?(y/n): ")
                            if rescuehim == "Murder Zork":
                                print("You killed Zork, and went back home.")
                                time.sleep(1)
                                print("You won!")
                            if rescuehim == "yes" or rescuehim == "y":
                                print("Good choice!")
                                time.sleep(1)
                                print("That was you objective after all.")
                                time.sleep(1)
                                print("King: Thank You very much! I feel so lucky to leave this putrid castle!")
                                time.sleep(1)
                                print(name+": Be quiet. The guards could hear us.")
                                time.sleep(1)
                                print("You start your journey back to your cabin.")
                                time.sleep(1)
                                print("Your journey back is cut short.")
                                time.sleep(4)
                                print("Guard: There they are! Kill THEM!")
                                time.sleep(1)
                                escapefromcastle = input("Attempt To Escape Castle?(y/n): ")
                                if escapefromcastle == "n" or escapefromcastle == "no":
                                    print("Since we stupidly decided to stay, you and the King Died!")
                                    time.sleep(1)
                                    print("Game Over.")
                                if escapefromcastle == "y" or escapefromcastle == "yes":
                                    print("You and the king successfully escape the castle.")
                                    time.sleep(1)
                                    print("The problem is, is that it is not over yet.")
                                    time.sleep(1)
                                    print("Zork: You THINK THAT YOU CAN JUST TAKE MY PRISONER?!?!?!??!?!")
                                    time.sleep(1)
                                    print("*intense pokemon music starts playing*")
                                    bosshealth = 220
                                    max_damage_taken = 55
                                    min_damage_taken = 30
                                    time.sleep(1)
                                    print("The King Gave You A healing potion!")
                                    time.sleep(1)
                                    healthrestored = random.randint(30,80)
                                    HP = HP + healthrestored
                                    time.sleep(1)
                                    print("You got some of your health restored!")
                                    time.sleep(1)
                                    print("Your HP:")
                                    print(HP)
                                    print("Bow Ammo:")
                                    print(bow_ammo)
                                    print("Attack Damage:")
                                    print("20-75 HP")
                                    print("Enemy HP:")
                                    print(bosshealth)
                                    bossalive = True
                                    #boss battle!
                                    while bossalive == True:
                                        whatdoyoudo3 = input("What Do You Do?(run/attack): ")
                                        if whatdoyoudo3 == "run":
                                            time.sleep(1)
                                            print("You attempted to run away but you and the king were killed.")
                                            time.sleep(1)
                                            print("YOU DIED!")
                                        if whatdoyoudo3 == "attack":
                                            time.sleep(1)
                                            weaponuse3 = input("Which weapon do you use?(bow/sword): ")
                                            if weaponuse3 == "bow":
                                                if bow_ammo == 0:
                                                    print("You are out of ammo!")
                                                attack_damage = random.randint(30, 75)
                                                print("You did:")
                                                print(attack_damage)
                                                print("Damage!")
                                                bosshealth = bosshealth - attack_damage
                                                bow_ammo = bow_ammo - 1
                                                print("Bow Ammo:")
                                                print(bow_ammo)
                                                if bosshealth < 0:
                                                    bosshealth = 0
                                                time.sleep(1)
                                                print("Enemy HP:")
                                                print(bosshealth)
                                                time.sleep(1)
                                                if bosshealth <= 0:
                                                    print("You won the battle!")
                                                    bossalive = False
                                                if bossalive == True:
                                                    print("The enemy attacked you back!")
                                                    time.sleep(1)
                                                    damage_taken = random.randint(min_damage_taken, max_damage_taken)
                                                    HP = HP - damage_taken
                                                if HP <= 0:
                                                    print("You lost the battle and died.")
                                                if HP < 0:
                                                    HP = 0
                                                    bossalive = False
                                                time.sleep(1)
                                                print("Your HP:")
                                                print(HP)
                                            if weaponuse3 == "sword":
                                                attack_damage = random.randint(30, 75)
                                                print("You did:")
                                                print(attack_damage)
                                                print("Damage!")
                                                bosshealth = bosshealth - attack_damage
                                                time.sleep(1)
                                                if bosshealth == 0:
                                                    bossalive = False
                                                if bosshealth <= 0:
                                                    print("You won the battle!")
                                                    bossalive = False
                                                    bosshealth = 0
                                                if bossalive == True:
                                                    print("The enemy attacked you back!")
                                                    time.sleep(1)
                                                    damage_taken = random.randint(min_damage_taken, max_damage_taken)
                                                    HP = HP - damage_taken
                                                    if HP <= 0:
                                                        bossalive = False
                                                        print("Game Over.")
                                                    if HP < 0:
                                                        HP = 0
                                                        print("Game Over.")
                                                        bossalive = False
                                                print("Enemy HP:")
                                                print(bosshealth)
                                                time.sleep(1)
                                                print("Your HP:")
                                                print(HP)
                                        if bossalive == False and HP > 0:
                                            print("You have killed Zork. It is now time to go home!")
                                            gobackhome = input("Go Back Home?(y/n): ")
                                            if gobackhome == "y" or gobackhome == "yes":
                                                print("You run back the same route as the way you came in with the king.")
                                                time.sleep(1)
                                                print("As you get closer and closer to your hometown, people appear.")
                                                time.sleep(1)
                                                print("You also find a random healing potion.")
                                                time.sleep(1)
                                                HP = HP + 15
                                                print("Your HP:")
                                                print(HP)
                                                trustthem = input("Do You Trust Them To Guide You Back?(y/n): ")
                                                if trustthem == "y" or trustthem == "yes":
                                                    print("They proceeded to impale you with their swords, and also killed you and the king.")
                                                    time.sleep(1)
                                                    print("Game Over!")
                                                if trustthem == "n" or trustthem == "no":
                                                    bosshealth = 100
                                                    bossalive = True
                                                    print("You didn't trust them, and ran past them as fast as you possibly could.")
                                                    time.sleep(1)
                                                    print("They weren't done with you yet though.")
                                                    time.sleep(1)
                                                    print("*Random Pokemon Battle Music Starts Playing*")
                                                    min_damage_taken = 10
                                                    max_damage_taken = 30
                                                    #4th and final battle.
                                                    while bossalive == True:
                                                        time.sleep(1)
                                                        print("Your HP:")
                                                        print(HP)
                                                        print("Bow Ammo:")
                                                        print(bow_ammo)
                                                        print("Sword Attack Damage:")
                                                        print("20-75")
                                                        print("Enemy HP:")
                                                        print(bosshealth)
                                                        whatdoyoudo4 = input("What Do You Do?(attack/run): ")
                                                        if whatdoyoudo4 == "attack":
                                                            weaponuse4 = input("What Weapon Do You Use?(bow/sword): ")
                                                            if weaponuse4 == "bow":
                                                                bow_ammo = bow_ammo - 1
                                                                attack_damage = random.randint(20, 75)
                                                                bosshealth = bosshealth - attack_damage
                                                                print("You did:")
                                                                print(attack_damage)
                                                                print("Damage!")
                                                                damage_taken = random.randint(min_damage_taken, max_damage_taken)
                                                                time.sleep(1)
                                                                if bosshealth <= 0:
                                                                    bossalive = False
                                                                    bosshealth = 0
                                                                    print("You won the battle!")
                                                                if bossalive == True:
                                                                    print("The enemy attacked you back!")
                                                                    HP = HP - damage_taken
                                                                    if HP <= "0":
                                                                        bossalive = False
                                                                        print("Game Over!")
                                                                        HP = 0
                                                            if weaponuse4 == "sword":
                                                                attack_damage = random.randint(20, 75)
                                                                bosshealth = bosshealth - attack_damage
                                                                print("You did:")
                                                                print(attack_damage)
                                                                print("Damage!")
                                                                damage_taken = random.randint(min_damage_taken, max_damage_taken)
                                                                time.sleep(1)
                                                                if bosshealth <= 0:
                                                                    bossalive = False
                                                                    bosshealth = 0
                                                                    print("You won the battle!")
                                                                if bossalive == True:
                                                                    print("The enemy attacked you back!")
                                                                    HP = HP - damage_taken
                                                                    if HP <= 0:
                                                                        bossalive = False
                                                                        print("You died!")
                                                                        HP = 0
                                                if HP > 0 and bossalive == False:
                                                    #no more battles here!
                                                    print("You have killed the people that attacked you.")
                                                    time.sleep(1)
                                                    print("You continued to make your journey to your town.")
                                                    time.sleep(3)
                                                    print("At last, you arrive.")
                                                    time.sleep(1)
                                                    print("Town Guard: " + name + ", it appears that you have rescued our king! Please, let us assist you!")
                                                    time.sleep(1)
                                                    print(name + ": Oh yes! Here is the king!")
                                                    time.sleep(1)
                                                    print("You allowed them to escort the king back.")
                                                    time.sleep(1)
                                                    print("You have nothing left to do.")
                                                    time.sleep(1)
                                                    gobackhome2 = input("Go back to your cabin?(y/n): ")
                                                    if gobackhome2 == "y" or gobackhome2 == "yes":
                                                        print("You went into your cabin.")
                                                        time.sleep(1)
                                                        print("The King came to your cabin.")
                                                        time.sleep(1)
                                                        print("King: Thank You "+name+"! I must reward you!")
                                                        time.sleep(1)
                                                        print("How about 999999$?")
                                                        accept = input("Accept?(y/n): ")
                                                        #please accept.
                                                        if accept == "y" or accept == "yes":
                                                            print("You Just Got 999999$")
                                                            time.sleep(1)
                                                            print("Thanks to you, the king was saved and the evil Zork is dead.")
                                                            time.sleep(1)
                                                            print("Thank You For Playing "+name+"!")
                                                            time.sleep(1)
                                                            print("The End.")
                                                        if accept == "n" or accept == "no":
                                                            print("You kindly turned down the offer.")
                                                            time.sleep(1)
                                                            print("King: Well, I was not expecting that.")
                                                            time.sleep(1)
                                                            print("King: How humble of you.")
                                                            time.sleep(1)
                                                            print("Beacuse of you, the king is safe, and the evil Zork is dead.")
                                                            time.sleep(1)
                                                            print("Thank You For Playing.")
                                                            time.sleep(1)
                                                            #ending 2!
                                                            print("The End.")
                                                    if gobackhome2 == "n" or gobackhome2 == "no":
                                                        print("You decided that going back to your cabin was unnecessary.")
                                                        time.sleep(1)
                                                        print("You sat down onto a chair.")
                                                        time.sleep(1)
                                                        print("Beacuse of you, the king is safe, and the evil Zork is dead.")
                                                        time.sleep(1)
                                                        print("Thank You For Playing.")
                                                        time.sleep(1)
                                                        #ending 1!
                                                        print("The End.")

                                            if gobackhome == "n" or gobackhome == "no":
                                                print("ARE YOU SERIOUS!?!?!?!")
                                                time.sleep(1)
                                                print("WHY DONT YOU WANT TO GO HOME?!?!?!?!")
                                                time.sleep(1)
                                                print("GAME OVER YOU IDOT.")
                                                #how do you get here?
                                if HP == 0:
                                    print("Game Over.")



                            if rescuehim == "n" or rescueleader == "no":
                                print("Then why the heck are you playing this game?")
                                time.sleep(1)
                                print("the literal OBJECTIVE of the game was to rescue the KING!!!")
                                time.sleep(1)
                                print("Game over.")

                    if leftorright2 == "right":
                        print("You went on the right path.")
                        time.sleep(1)
                        print("You walked into an endless hole.")
                        time.sleep(1)
                        print("YOU DIED!")

            if rescueleader == "n" or rescueleader == "no":
                time.sleep(1)
                print("You said no and decided to jump down a hole.")
                time.sleep(1)
                HP = HP - HP
                print("Your HP:")
                print(HP)
                print("You died!")
                time.sleep(1)
                print("YOU LOSE")
    if leavehouse == "y" or leavehouse == "yes":
        time.sleep(1)
        print("You got struck by lightning and died.")
        HP = HP - HP
        print("Your HP:")
        print(HP)

#this should be the end of the code.