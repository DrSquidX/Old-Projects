#importing libraries
import random
import time
#while loop variables
ask = True
ask2 = True
ask3 = True
#list
friends = []
#intro
print("Random Group Assigner for Groups Of 2 (1.3)")
print("By DrSquid")
print("")
#the thing itself
while ask:
    new_person = str(input("Who is being added to the list?: ")) #adding people to group
    friends.insert(3,new_person)
    friends.pop
    friends.sort() #sorts the group by alphabetical order
    personcount = len(friends)
    print("The current number of people is:", personcount)
    ask2 = True
    while ask2:
        continue_count = input("Do you wish to continue adding people(y/n)?: ")
        if continue_count == "y" or continue_count == "yes":
            ask2 = False
        elif continue_count == "n" or continue_count == "no":
            ask2 = True
            random.shuffle(friends) #shuffles the group
            group_number = 1 #sets the group number to 1
            assign = True
            while assign: #group assiging
                try:
                    random.shuffle(friends)  # shuffles group
                    person1 = friends[0]  # 1st person in group 1
                    person2 = friends[1]  # 2nd person in group 1
                    print("Assigning Team", group_number) #announces the group number being made
                    time.sleep(2)
                    print("This group consists of:", person1, "and", person2) #announces the team
                    del friends[0] #deletes person 1 off the list
                    time.sleep(0.01)
                    del friends[0] #deletes person 2 off the list
                    group_number += 1 #makes the group number go up by 1
                    personcount -= 2 #decreases the person count by 2
                    time.sleep(3)
                    if personcount < 1: #if the person count is smaller than 1
                        while ask3: #if you want to try again.
                            doagain = input("Do you wish to use the group assigner again?: ")
                            if doagain == "y" or doagain == "yes":
                                friends = []
                                ask2 = False
                                ask3 = False
                                assign = False
                            elif doagain == "n" or doagain == "no":
                                print("Thank you for using the group assigner!")
                                quit()
                            else:
                                print("Invalid Input.")
                except IndexError: #if there is a group of 3
                    lastperson = friends.pop(0) #last person assiging
                    remaining_person = random.randint(1, group_number) #decides which group number
                    print("There is a remaining person.")
                    time.sleep(2)
                    print("The remaining person is", lastperson) #announces the last person
                    time.sleep(2)
                    print("S/he is in group", remaining_person) #announces their group
                    time.sleep(2)
                    assign = False #ends the assign loop
                    while ask3: #if you want to use the thing again
                        doagain = input("Do you wish to use the group assigner again?: ")
                        if doagain == "y" or doagain == "yes":
                            friends = []
                            ask2 = False
                            ask3 = False
                            assign = False
                        elif doagain == "n" or doagain == "no":
                            print("Thank you for using the group assigner!")
                            quit()
                        else:
                            print("Invalid Input.")
        else:
            print("Invalid input.")