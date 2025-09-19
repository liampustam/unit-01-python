print("Welcome to the Calculatinator-inator 9000!")

first = float(input("Enter your first number: "))

second = float(input("Enter your second number: "))
#Sked them which operations they want to choose
print()
print("1.addition ")
print()
print("2.subtraction ")
print()
print("3.multiplication")
print()
print("4.division ")
print()
print("5.exponents ")
print()
print("6.floor division ")
print()
print("7.remainder ")
print()
input1 = input("Select an operation: ")

 

#Does the math for addition
if input1 == "1" or input1 == "addition":
    addition = first + second
    print(addition)
#Does the math for subtraction
elif input1 == "2" or input1 == "subtraction":
    subtraction = first - second 
    print(subtraction)
#Does the math multiplication
elif input1 == "3" or input1 == "multiplication":
    multiplication = first * second
    print(multiplication)
#Does the math for division
elif input1 == "4" or input1 == "division":
    #If the number is greater than 0 it continues
    if second > 0 or second < 0:
        division = first / second 
        print(division)
    #if the number is 0  it will not work
    else:
        print("Can not calculate with that number")
# calculate exponents 
elif input1 == "5" or input1 == "exponents":
    exponents = first ** second 
    print(exponents)
# does the math for floor division
elif input1 == "6" or input1 == "floor division":
    #If the number is greater than 0 it continues
    if second > 0 or second < 0:
        floor_division = first // second
        print(floor_division)
     #if the number is 0  it will not work
    else:
        print("Can not calculate with that number")
#Does math with remainder
elif input1 == "7" or input1 == "remainder":
         #If the number is greater than 0 it continues

     if second > 0 or second < 0:
        remainder = first % second
        print(remainder)
     #if the number is 0  it will not work
     else:
        print("Can not calculate with that number")
# If the user chooes an operations thats not there it wont work        
else:
    print("INVALID OPERATION")





