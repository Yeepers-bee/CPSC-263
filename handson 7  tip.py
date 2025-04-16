
def main():
    title()
    meal = cost_of_meal()
    tip = get_tip()
    output(meal, tip)
    

def title():
    print("Tip Calculator\n")
    print("INPUT")
    return

def cost_of_meal():
    while True:
        try:
            meal = float(input("Cost of meal: "))
            if meal <= 0:
                print("Must be greater than 0. Please try again.")
            else:
                return meal 
        except ValueError:
            print("Must be valid decimal number. Please try again.")






def get_tip():
    while True:
        try:
            tip = int(input("Tip percent: "))
            if tip  <= 0:
                print("Must be greater than 0. Please try again.")
            else:
                return tip
        except ValueError:
            print("Must be valid integer. Please try again.")



def output(meal, tip):
    print("\nOUTPUT")
    print(f"{'Cost of meal:':<15}{meal:>.2f}")
    print(f"{'Tip percent:':<15}{tip}%")
    tip_amount = calculate_tip(meal, tip)
    total_amount = tip_amount + meal
    print(f"{'Tip amount:':<15}{tip_amount:>.2f}")
    print(f"{'Total amount:':<15}{total_amount:>.2f}")
        



def calculate_tip(meal, tip):
    percent_tip = tip * .01
    tip_amount = percent_tip * meal
    total_amount = tip_amount + meal
    return tip_amount
    
    



if __name__ == "__main__":
    main()


