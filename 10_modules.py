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

data_dir = "data"

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
    print(f"Directory '{data_dir}' created.")
else:
    print("Directory already exists.")


"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
#Checks to see if the file is ine there
file_name = "05_calculator.py"
if os.path.isfile(file_name):
    print("File found:", os.path.abspath(file_name))
else:
    print("File not found.")


"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""

#Prints the python version that I am currectly using
print("Python version:", sys.version)


"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""

#Tells me what platform in running on
platform = sys.platform

if platform.startswith("linux"):
    print("Platform: Linux")
elif platform.startswith("win"):
    print("Platform: Windows")
elif platform.startswith("darwin"):
    print("Platform: MacOS")
else:
    print("Platform: Unknown")