"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#Value
name = "LIAM"

#print each character in name
for name in name:
    print(name)

print()
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#List
num = [3, 4, 6 ]
sum = 0

#Adds the number up togehter
for x in num:
    sum += x

print(sum)


print()
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#string
sentence = "hello there my name is liam"

#Splits the words in the string
idk = sentence.split(" ")

#Syays the length of each wordin the string
for x in idk:
    
    print(len(x))

print()

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result



In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

a = {
    "peaches": 7,
    "apples": 6,
    "pineapple": 5,
    "banana": 3,

}

for x in a:
    print(x)