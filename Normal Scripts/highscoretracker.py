import time
ask = True
ask_counter = 0

while ask:
    try:
        if ask_counter == 0:
            score = int(input("What is your score?: "))
            ask_counter += 1
        if ask_counter >= 1:
            print("The current highscore is", score)
            new_score = int(input("What is your next score?: "))
            if new_score > score:
                print("You have beaten your old highscore!")
                difference = new_score - score
                print("You beat it by", difference)
                print("points!")
                score = new_score
            elif new_score == score:
                print("Looks like your score was the exact same as your other score.")
                print("Try to beat it! You can do it!")
            elif new_score < score:
                print("Looks like your score is lower than your current highscore.")
                difference = score - new_score
                print("You were behind it by", difference)
                print("points.")
                print("Rather unfortunate. Try to beat it!")
    except ValueError:
        print("You have to input a valid integer.")
    except TypeError:
        print("Invalid Input.")