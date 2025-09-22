"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
#The correct password variable
correct_password = "hithere"

#Asks to enter a password
input1 = input("Enter your password: ")

#Prints if password is guessed correctly
if input1.lower() == correct_password:
    print("Successfullty Logged In")
    #Prints if password is not guessed correctly
else :
    print("Wrong Password")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
user_input = input("Enter Something: ")


user_input = input("Enter something: ")

if user_input:  # Checks if the string is empty
    print("invalid")
else:
    print("valid")



"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
#Ask them to enter a setence
text = input("Enter a sentence: ").lower()

#Replaces all dogs with cat
text = text.replace("cat", "dog")

print(text)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
#Ask what name is
name = input("What is your name?:  ")
#Ask what age they are
age = input("What is your age")

#Prints name and age
print(name, "is", age)
"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""