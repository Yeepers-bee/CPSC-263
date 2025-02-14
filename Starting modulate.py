
continue_input = "y"

while continue_input == "y" or continue_input == "Y": 
    
    cents = int(input("Enter number of cents (0-99): "))

    quarters: int = int(cents/25)

    

    modulate:int = int(cents%25)

    dimes: int = modulate/10

    d_modulate: int = modulate%10

    nickles: int = int(d_modulate/5)

    penny: int = int(d_modulate%5)

    




    print("Quarters: ", str(quarters))
    print("Dimes: ", str(dimes))
    print("Nickels: ", str(nickles))
    print("Pennies: ", str(penny))
    continue_input: str = input("\nContinue? (y/n)")
