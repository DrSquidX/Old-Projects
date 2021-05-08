import datetime

ask = True

while ask:
    try:
        today = datetime.date.today()
        print("Today is:", today)

        event = input("What is the event?: ")
        yearofevent = int(input("What is the year of the event?: "))
        monthofevent = int(input("What is the month of the event?: "))
        dayofevent = int(input("What is the day of the event?: "))
        eventdate = datetime.date(yearofevent, monthofevent, dayofevent)
        nexteventYear = today.year + (eventdate.year - today.year)
        nexteventday = datetime.date(nexteventYear, eventdate.month, eventdate.day)
        print("Date of " + event + ":", nexteventday)
        diff = nexteventday - today
        if diff.days == 0:
            print("That is actually today!")
        print("Days till " + event + ":", diff.days)
        doitagain = ""
        while doitagain != "yes" and doitagain != "y" and doitagain != "n" and doitagain != "no":
            doitagain = input("Would you like to use the calculator again(y/n)?: ")
            if doitagain == "y" or doitagain == "yes":
                ask = True
            elif doitagain == "n" or doitagain == "no":
                print("Thank you for using the calculator!")
                ask = False
                quit()
            else:
                print("Invalid Input.")
    except ValueError:
        print("Error Calculating. Please try again.")