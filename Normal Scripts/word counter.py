#while loop variables
ask = True
ask2 = True
print("Word Counter 1.2")
print("By DrSquid")
print("")
while ask:
    s = input("Type in the text that you want me to count the words of: ") #<----- type the text here
    word_count = len(s.split())#does the word count. It splits the set of words, which the len function counts the words.
    print("The word count is: ", str(word_count)) #shows the wordcount
    ask2 = True
    while ask2: #if you want to play again.
        countagain = input("Do you wish to have another thing counted?: ")
        if countagain == "y" or countagain == "yes":
            ask = True
            ask2 = False
        elif countagain == "n" or countagain == "no":
            ask = False
            ask2 = False
            print("Thank you for using the word counter!")
        else:
            print("Invalid Input.")