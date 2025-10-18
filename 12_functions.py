"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
#Prints hello, and the persons name
def greeting(name):
    print(f"Hello, {name}!")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#Squares any number that is gice
def square(num):
    return num ** 2

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
#Prints true or false if the number is even
def is_even(number):
    return number % 2 == 0

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

#Calculates area of a triangle
def area_of_rectangle(length, width):
    return length * width

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

#Converts Celisuis to farenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""

#Calulates the mean of numbers
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.



Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""

#Calulates the price and quantitiy of something
def total_calculator(price, quantity, discount=0.0):
    total = price * quantity
    if discount > 0:
        total -= total * discount
    return total