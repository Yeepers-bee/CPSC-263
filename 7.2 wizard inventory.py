import random

def main():
    command_menu()
    
    while True:
        print('')
        command_occured = False
        user_input = input("Command: ")

#walk
        if user_input == "walk":
            walk()
            command_occured = True
#show
        elif user_input == "show":
            show()
            command_occured = True
#drop 
        elif user_input == "drop":
            drop()
            command_occured = True
#exit
        elif user_input == "exit":
            print("Command: exit")
            print("Bye!")
            return
        elif not command_occured:
            print("ERROR! Invalid command.")
    
            
            
def title():
    print("The Wizard Inventroy Program/n")

def walk():
    line_count: int = 0
    with open('wizard_all_items.txt', 'r') as file:
        all_items = file.readlines()
    for line in all_items:
        line_count = line_count + 1
    ran_num = random.randint(1, line_count)
    print("While walking down a path, you see " + str(all_items[ran_num]),  end='')
    user_input = input("Do you want to grab it? (y/n): ")
    if user_input == 'y':

        if check() == True:
            print("You picked up " + str(all_items[ran_num]), end='')
            outfile = open('wizard_inventory.txt', 'a')
            outfile.write(str(all_items[ran_num]))
            outfile.close()
        else:
            print("You can't carry any more items. Drop something first.")
    if user_input == 'n':
        pass
        


def check():
    inventory_space = 4
    file = open('wizard_inventory.txt', 'r')
    all_items = file.readlines()
    line_count = 0
    for line in all_items:
        line_count = line_count + 1
    if line_count == inventory_space:

        return False
    else:
  
        return True
    

def show():
    file = open('wizard_inventory.txt', 'r')
    wizard_inventory = file.readlines()
    line_count = 1
    for line in wizard_inventory:
        print(str(line_count) + ".  " + str(wizard_inventory[line_count - 1]), end='')
        line_count = line_count + 1
    file.close()

def drop():
    with open('wizard_inventory.txt', 'r') as file:
        wizard_inventory = file.readlines()
    user_input = input("Number: ")
    line_count = 0
    dropped = False
    
    for line in wizard_inventory:
        line_count += 1
        if line_count == int(user_input):
            print("You dropped " + line.strip())
            new_inventory = wizard_inventory[:line_count-1] + wizard_inventory[line_count:]
            with open('wizard_inventory.txt', 'w') as file:
                file.writelines(new_inventory)
            dropped = True
            break
    
    if not dropped:
        print("Invalid number to drop.")

def command_menu():
    print("walk - Walk down the path")
    print("show - Show all items ")
    print("drop - Drop an item")
    print("exit - Exit program")




if __name__ == "__main__":
    main()
