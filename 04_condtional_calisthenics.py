'''
Exercise 1:
Check if an integer even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

# asking what ther number is
input1 = int(input("Enter a numebr: "))

# Checking if the number is greater than both 0 and 10
if input1 > 0 and input1 > 10:
    print("True")
else:
    print("False")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
# Setting conditions
age1 = int(input("What is your age?: "))
student = input("Are you a students, yes or no?: ")

# Checking to see if the conditions are met
if age1 < 18 or student == "yes":
    print("Price is $10")
else:
    print("Price is $20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
# Ask what fruit they pick
ask_fruit = input("Pick a fruit: apple, banana, or cherry?: ")

# List of fruit
x =  {
    "apple",
    "banana",
    "cherry"

}

# Checking if the fruit is there
if ask_fruit in x:
    print("Yes that fruit is in the list")
else:
    print("No that fruitn is not in the list")

'''
Exercise 4:
Check if a year is a century year and a leap year.

'''


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
destination = input("What zone is it going to?: ")

weight = float(input("How much does the package weight?: "))



'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''