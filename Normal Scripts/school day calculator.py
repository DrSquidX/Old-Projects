schoolday_nobreaks = int(input("How many weeks of school are there?: "))
holiday_weeks = int(input("How many weeks of holiday?: "))
holidays = int(input("How many days of holiday you have(excluding weekends)?: "))

schoolday_nobreaks = schoolday_nobreaks + holiday_weeks
days_of_school_noholidays = schoolday_nobreaks * 5
days_of_school = days_of_school_noholidays - holidays
print("The days of school are:")
print(days_of_school)