"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
#Creates a list
list = [1,2,3,4,5]

print(list)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
#Add elemts to the list
list = [1,2,3,4,5]

list.append(6)

print(list)
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

#Remove elements from the list
list = [1,2,3,4,5]

list.remove(1)

print(list)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
#Changes a specific number in the list
list = [1,2,3,4,5]

list[1] = 100

print(list)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
#Adds on numbers to the list
list = [1,2,3,4,5]

list.extend([6,7,8,9])

print(list)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

#deletes a number from the list
list = [1,2,3,4,5]

del list[1]

print(list)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
#Prints out the second list
list = [1,2,3,4,5]

list_2 = [1,2]

print(list_2)
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
#Adds list 2 onto list 1
list = [1,2,3,4,5]

list_2 = [6,7,8,9]

list.extend(list_2)

print(list)