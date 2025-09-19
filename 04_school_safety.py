# Asking how many computers
computers = int(input("How many computers are available?"))
# Asking how many students
students = int(input("How many students are waiting? "))
# Asking how what type of class it is
classes = input("What type of class is it: programming, research, or typing? ")
# Asking if there are any students with special accommodations
accommodations = int(input("How many students need special accommodations?: "))
# Asking how long the class is
period = int(input("How long is the class period?"))

# Showing how much computers the class still needs


if classes == "programming" or "typing" or "research":
    if classes == "programming": 
        if period >= 90:
            if computers >= 5:
                if accommodations >= 1:
                    if computers >= students or computers <= students:
                        print("You need to ")
                else:
                    print("There is not enough computers for each student")
            else:
                print("You need atleast 5 computers")
        else:
            print("class is not long enough")
    # Checking to see if the class is either typing or research
    if classes == "typing" or classes ==  "research":
     # Making sure the class is atleast 45 minutes
        if period >= 45:
            # Checking to see if someone in the class has accommodations
            if accommodations >= 1:
                #Checking to see if theres enough computers
                if computers <= students or computers >= students:
                    print("Adequate for class") 
                else:
                    print("Not adequate for the class")
            else:
                print("There is not enough computers for each student")
        else:
            print("This class is not long enough")
else:
    print("This is not a class")

        




        


