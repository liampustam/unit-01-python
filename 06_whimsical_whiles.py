"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
# The starting number
i = 1

#Adds 1 till 10
while i <= 10:
    print(i)
    i += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
#Starts at 10
i = 10

# Subtracts till it gets to 1
while i <= 10 and i > 0:
    print(i)
    i -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

#Asks what the number is
number = int(input("Give me a number: "))
result = 1

#If the nnumber is greater than 0 it will subtract from the number and multiply it together
while number > 0:
    result = number * result
    number -= 1
print(result)





"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
#If the passwprd is wrong then you keep on trying till its right
guess = input("What do you think the password is: ")

correct_password = "hello"

while guess != correct_password:
    print("Try Again")
    guess = input("What do you think the password is: ")
else:
    print("Successfully logged in")
print()


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

#Prints the fibonacci
i = 0

a = i - 1

while i >= 0:
    i += 1
    print(i)
    if a > 34:
        break

print(i)


