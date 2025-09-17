"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
# Created a float variable
first_float = 23.5

# Convert the float into an intger 
the_integer = int(first_float)


# printed  the integer and the float
print(first_float)
print(the_integer)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

sum = float(input("Enter a number: "))

    # Check if the number is positive, negative, or zero
if sum > 0:
    print("It is a positive number")
elif sum < 0:
    print("It is a negative number.")
else:
    print("It is zero.")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

input1 = input("Whats Your first number?: ")

num1 = float(input1)

print(type(num1))



input2 = input("What is your second number?: ")

num2 = float(input2)


print(type(num2))

print

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
# Made dictionary of fruits
fruit = float(input("What fruit would you like to search for: "))

x = {
    "peaches": 7,
    "apples": 6,
    "pineapple": 5,

}

# Printed out the number of pineapples

print(f"{fruit}")

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
str
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.

"""