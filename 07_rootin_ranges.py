"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#counts from 1 and stops at 9
for x in range(1,10):
    print(x)

print()
print()
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#counts in incraments of 5 from 900 to 1000
for x in range(900, 1001, 5):
    print(x)

print()
print()
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#counts in incraments of 9 from 1 to 100
for x in range(1, 108, 9):
    print(x)

print()
print()
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#counts from 1 to 10 and adds up the numbers in between
sum = 0
for x in range(1, 10):
    sum += x
print(sum)

print()
print()
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5
# the output of the code is:

# *
# **
# ***
# ****
# ***** 

#The code adds a * each time it runs and prints it in it's own secction
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()