import math
#formula being used is 2 to the power of n
def power(x, y): #function
  return math.pow(x, y) #raises x to the power of y(basically utilizing this to raise things to powers)
ask = True #loop
print("Braille Calculator 1.0 By Adrian Fang")
while ask: #main loop
  try:
      x = 2 #the 2 in the formula
      y = 1 #the n in the formula
      loopnumber = int(input("What is the dot count in the braille formation?: ")) #for the max loop count
      loopnumber += 1
      loops = 1 #loop count
      thingy = 0 #just the value of the answer
      ask2 = False
      while loops < loopnumber:
          try: #tries to do this
              thingy = power(x, y)
              print("The amount of braille combinations for", loops,"dots is:", thingy)
              y += 1 #makes the exponent 1 greater
              loops += 1 #adds 1 to the loopcount
              if loops == loopnumber: #if number of loops = max amount of loops
                  loops += 1 #adds one to the loopcount to trigger the loops > loopnumber statement
          except OverflowError: #if the number is too big(an error)!
              print("The Number is too big now.")
              loops = loopnumber + 10
      if loops > loopnumber: #if the loopcount is bigger than the maxcount
          ask2 = True #makes subloop true
          while ask2: #subloop for question
              do_again = input("Would you like to use this again?: ")
              if do_again == "y" or do_again == "yes":
                  ask = True #makes this loop true
                  ask2 = False #makes this loop false
              elif do_again == "n" or do_again == "no":
                  ask = False #makes this loop false
                  print("Thank you for using the braille calculator!")
                  quit() #ends code
              else: #if you enter an invalid input
                  print("invalid input.")
  except ValueError: #if someone enters an str instead of an int
      print("Invalid Input.")