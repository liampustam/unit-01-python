import os 
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
var = os.getcwd()
print(var)
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
new_name = "test_folder"
os.getcwd()
# os.mkdir(new_name)
var_list = os.listdir()
print(var_list)

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""

#if data in os.
"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""


"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""


"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""