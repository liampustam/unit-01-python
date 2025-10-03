text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1
    
print(count)


n = int(input("give me a number: "))

for num in range(1, n):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")


num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + str(num) + " is " + str(result))


attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == "incorrect_password":
        print("Correct password!")

    elif attempts > 2 :
        print("Too many attempts")
        break
    else:
        print("Incorrect password")

