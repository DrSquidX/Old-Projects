import random

number = random.randint(1, 5)
guess_count = 3
loop = True
number_guessed = False

while loop:
    try:
        if not number_guessed:
            number_guess = int(input("What is your guess for the number(1-5)?: "))
        if number_guess == number:
            print("You have guessed the number!")
            number_guessed = True
        if number_guess != number:
            guess_count -= 1
            print("You were incorrect.")
            print("You have")
            print(guess_count)
            print("guesses left.")
        if guess_count == 0:
            print("You lost.")
        if guess_count == 0 or number_guessed:
            playagain = input("Would you like to play again?: ")
            if playagain == "y":
                number = random.randint(1, 3)
                loop = True
                number_guessed = False
                guess_count = 3
            if playagain == "n":
                loop = False
                print("Thank you for playing!")
                quit()
    except:
        print("Invalid input.")