
def main():
    menu()
    dictionary = {}
    FILENAME = "monthly_sales.txt"
    with open(FILENAME, 'r') as file:
        #for each line get month as key and money as value.
        for line in file:
            clean_line = line.strip()
            split_list = clean_line.split('\t')
   
            month = split_list[0]
            value = split_list[1]
            dictionary[month] = int(value)
        temp = file.readline()
    file.close()
    while True:
        command_occured = False
        print('')
        user_input = input("Command: ")
        if user_input == 'view':
            view(dictionary)
            command_occured = True
        elif user_input == 'edit':
            edit(dictionary, FILENAME)
            command_occured = True
        elif user_input == 'totals':
            totals(dictionary)
            command_occured = True
        elif user_input == 'exit':
            print("Bye!")
            return
        elif not command_occured:
            print("ERROR! Invalid command.")



def view(dictionary):
    user_input = input("Three-letter Month: ")
    valid = valid_month(user_input, dictionary)
    if valid is not None:
        display_sales_amount(valid, dictionary)
    else:
        print("Invalid three-letter month.")
        return
               

def totals(dictionary):
    year: int = 0
    for key in dictionary:
        year = year + dictionary[key]
    #divide by the amount of months for monthly average
    month = year / 12
    print("Yearly total: " + str(year))
    print("Monthly average: " + str(month))
    return
        

def edit(dictionary, FILENAME):
    user_input = input("Three-letter Month: ")
    valid = valid_month(user_input, dictionary)
    if valid is not None:
        user_sales_amount = input("Sales Amount: ")
        dictionary[valid] = user_sales_amount
        
        with open(FILENAME, 'w') as file:
            for key in dictionary:
                #lets file keep the same present format
                file.write(f"{key}\t{dictionary[key]}\n")
        file.close()
        display_sales_amount(valid, dictionary)
        return
    else:
        print("Invalid three-letter month.")
        return
    
   

    #with open(FILENAME, 'r') as file:
        
    

def valid_month(user_input, dictionary):
    key_list = dictionary.keys()
    #this stores the keys in lower case text to see if that matched input
    lower_key_list = []
    #handles if user_input is capitalized
    if user_input in dictionary:
        return user_input
    else:
        #handles lowercase user_input
        for key in key_list:
            # Return the original key
            if key.lower() == user_input.lower():
                return key 
        else:
            return None




def display_sales_amount(user_input, dictionary):
    print("Sales amount for " + user_input + " is " + str(dictionary[user_input]))
    return


            
def menu():
    print("COMMAND MENU")
    print("view	- View sales for specified month")
    print("edit	- Edit sales for specified month ")
    print("totals - View sales summary for year")
    print("exit	- Exit program")


if __name__ == "__main__":
    main()



