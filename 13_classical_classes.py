"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
#Set class named person
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
#Allows it to print name and age
liam = Person("Liam", 17)
print(liam.name)
print(liam.age)

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
#main class animal
class Animals:
    def speak(self):
        pass
#sub class Dog
class Dog(Animals):

    def speak(self):
        print("woof!")
#Prints woof for dog
dog = Dog()
dog.speak()

class Cat(Animals):
    
    def speak(self):
        print("meow")
#Print meow for cat
cat = Cat()
cat.speak()









"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

#Main class BankAccount
class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    #TAkes how much is in your account and adds a number
    def deposit(self, amount):  
        if amount > 0:
            self.balance += amount
            print(f"Successfullt depostitied ${amount}. Your new balance is ${self.balance}")
    #Subtracts how much you would like to withdraw from your balance
    def withdraw(self, amount_2):
        if amount_2 < 0:
            self.balance -= amount_2
            print(f"Successfully withdrew ${amount_2}. Your new balance is ${self.balance}")