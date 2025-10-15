
contacts = {

}
#Make sure the program does no stop running 
while 1 > 0:
    print("-------------------------------------------------------")
    #Prints your contact book
    print("Contact Book Menu:")
    print()
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")
    choice = input("Enter your choice: ")
    #Adds a contact
    if choice == "1" or choice == "add":
        name = input("Enter the contact's name: ")
        contact = input("Enter the contact's phone number ")
        while len(contact) == 10:
            contacts[name] = contact
            print("Contact successfully saved!")
            break
        else:
            print("Contact not saved")
    #Deletes contact of choice
    if choice == "2" or choice == "delete":
        remove = input("Which contact would you like to remove")
        #Makes sure that the contact is in the dictionary
        if remove in contacts:
            del contacts[remove]
            print("Contact successfully removed")
        else:
            print("Invalid contact")
        #Lists all the contacts
    if choice == "3" or choice == "list":
        print("Contacts: ")
        for x in contacts:
            print(x,  contacts[x])
        #When the choice is 4 the program stops running
    if choice == "4" or choice == "exit":
        break