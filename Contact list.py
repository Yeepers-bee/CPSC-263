
def main():
    contact = default_list()
    user_input = command_menu()
    while True:

#LIST
        if user_input == "1":
            listing = list_display(contact)
            user_input = input("")

#VIEW
        elif user_input == "2":
            view(contact)
            user_input = input("")

#ADD
        elif user_input == "3":
            adding = add()
            contact.append(adding)
            user_input = input("")

#DELETES
        elif user_input == "4":
            deleted = delete(contact)
            if deleted < len(contact):
                contact.pop(deleted)
            user_input = input("")
#QUIT
        elif user_input == "5":
            print("Command: exit")
            print("Bye!")
            contact = default_list()
            return
        else:
            user_input = input("")
            
            
def title():
    print("Contact Manager/n")

def list_display(contact):
    print("Command: list")
    length = len(contact)
    for i in range(length):
        number = i + 1
        print(number, ". ", contact[i][0], sep='')

def view(contact):
    print("Command: view")
    real_number = int(input("Number: "))
    number = real_number - 1
    if number < len(contact):
        
        name = contact[number][0]
        email = contact[number][1]
        phone = contact[number][2]
        print("Name: ", name)
        print("Email: ", email)
        print("Phone: ", phone)
    else:
        print(len(contact))
        print("ERROR:", real_number, "is not in the list!")

def add():
    print("Command: add")
    add_list = []
    name  = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    print(name, "was added.")
    add_list.append(name)
    add_list.append(email)
    add_list.append(phone)
    return add_list
    
def delete(contact):
    print("Command: del")
    real_delete_num = int(input("Number: "))
    delete_num = real_delete_num - 1
    if delete_num < len(contact):
        print(contact[delete_num][0], "was deleted.")
        return delete_num
    else:
        print("ERROR:", real_delete_num, "is not in the list!")
        return 999999999999999

def command_menu():
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    user_input = input("")
    return user_input
    
def default_list():
     contact = [
    ["Guido van Rossum", "guide@email.com", "+305 999 999"],
    ["Eric Idle", "eric@ericidle.com", "+ 44 20 7946 0958"]
    ]
     return contact
    




if __name__ == "__main__":
    main()
