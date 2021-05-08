import random
import time
ask = True
ask2 = True
def win(whatthing, computer_input):
    if whatthing == "r" and computer_input == 3:
        return True
    if whatthing == "p" and computer_input == 1:
        return True
    if whatthing == "s" and computer_input == 2:
        return True
    else:
        return False
def lose(whatthing, computer_input):
    if whatthing == "r" and computer_input == 2:
        return True
    if whatthing == "p" and computer_input == 3:
        return True
    if whatthing == "s" and computer_input == 1:
        return True
    else:
        return False
def draw(whatthing, computer_input):
    if whatthing == "r" and computer_input == 1:
        return True
    if whatthing == "p" and computer_input == 2:
        return True
    if whatthing == "s" and computer_input == 3:
        return True
    else:
        return False
question = True
print("Rock Paper Scissors 1.1")
print("A remake by DrSquid.")
print("Please only type the first letter of the item(r for rock, p for paper and s for scissors).")
print("")
while ask:
    whatthing = input("What type of thing will you choose(r/p/s)?: ")
    if whatthing == "r" or whatthing == "p" or whatthing == "s":
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.5)
        print("Shoot!")
        time.sleep(0.5)
        computer_input = random.randint(1, 3)
        if win(whatthing, computer_input):
            print("You win!")
        if draw(whatthing, computer_input):
            print("It's a draw!")
        if lose(whatthing, computer_input):
            print("You lose.")
        ask2 = True
        while ask2:
            try_again = input("Would you like to play again?: ")
            if try_again == "y" or try_again == "yes":
                ask = True
                ask2 = False
            elif try_again == "n" or try_again == "no":
                ask = False
                ask2 = False
                print("Thank you for playing!")
            else:
                print("Invalid Input.")
    else:
        print("Invalid Input.")
#nice