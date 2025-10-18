"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#Tells the time it is right now down to the thousandth of a milisecond 
from datetime import datetime

time_not = datetime.today()

print(time_not)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#it tells you the current date and time in the standard U.S date format
from datetime import datetime
time_not = datetime.today()
my_specific = time_not.strftime("%m/%d/%Y")
print(my_specific)
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

#Takes two dates and tells you the differnce in the days
from datetime import datetime

first_day = "02/15/2008"
second_day = "02/28/2008"

first_day_time = datetime.strptime(first_day, "%m/%d/%Y")
second_day_time = datetime.strptime(second_day, "%m/%d/%Y")

rah = first_day_time - second_day_time
print(rah)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

#Calucatues how old someone is and tells you in days
from datetime import datetime

ask = input("When is your birthday in (MM/DD/YYYY): ")

birthday = datetime.strptime(ask, "%m/%d/%Y")

time_not = datetime.today()

ahh = time_not - birthday

print(ahh)