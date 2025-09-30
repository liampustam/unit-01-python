

a = "add"
r = "remove"
i = 1

todo_list = []

#Makes sure the list runs forever
while 1 > 0:
    print("-----------------------------")
    #prints your todo
    print("Your current todos are:")
    print()
    print('\n'.join(todo_list))
    print()
    #Asks if they want to add or remove things from the list
    check = input("Would you like to add, remove, clear all or edit?: ")
    #If you want to add it adds stuff to the list
    if check == "add":
        print()
        add = input("What do you want to add to the list: ")
        print()
        #Adds whatever wants to be added to the list
        todo_list.append(add)
        print()
    #This happend when the person wants to remove
    elif check == "remove":
        print()
        #Pick which one they want to remove
        remove = int(input("Which # would you like to remove: "))
        #Makes it so that the index does not matter
        del todo_list[remove -1]
    #Removes everything from the list
    elif check == "clear" or check == "clear all":
        todo_list = []
    elif check == "edit":
        print()
        edit = int(input("What # would you like to edit?: "))
        todo_list[edit -1]
        print()
        pick = input("What would you like it to say?: ")
        todo_list.replace(pick)


#If its not an option, theres an error
    else:
        print()
        print()
        print("*ERROR not a choice*")






