import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def exponent(x, y):
    return math.pow(x, y)
def squareroot(x):
    return math.sqrt(x)
calculate = True
while calculate:
    try:
        x = float(input("What is your first number?: "))
        y = float(input("What is your second number(this will not matter if you are calculating square roots)?: "))
        answer = add(x, y)
        operation = input("What type of equation?(add, subtract, divide, multiply, exponent, squareroot): ")
        if operation == "add":
            answer = add(x, y)
            correct = True
        elif operation == "subtract":
            answer = subtract(x, y)
            correct = True
        elif operation == "divide":
            answer = divide(x, y)
            correct = True
        elif operation == "multiply":
            answer = multiply(x, y)
            correct = True
        elif operation == "exponent":
            answer = exponent(x, y)
            if OverflowError:
                print("The answer is way too big! Try another smaller exponent!")
            correct = True
        elif operation == "squareroot":
            answer = squareroot(x)
            correct = True
        elif operation != "add" and operation != "subtract" and operation != "multiply" and operation != "divide" and operation != "exponent" and operation != "squareroot" and not OverflowError:
            print("Invalid Input")
            correct = False
        if correct:
            print("The answer to the equation was:")
            print(answer)
            doitagain = input("Do you wish to use the calculator again?(y/n): ")
            if doitagain == "y" or doitagain == "yes":
                calculate = True
            elif doitagain == "n" or doitagain == "no":
                print("Thank you for using the calculator!")
                calculate = False
                quit()
        else:
            print("invalid operation.")
    except ZeroDivisionError:
        print("Zero Division is impossible!")
    except OverflowError:
        print("The answer is too big!")
    except ValueError:
        print("Invalid Input.")
    except NameError:
        print("Invalid Input.")


