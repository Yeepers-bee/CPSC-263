import salesTaxFunctions

def main():
    title()
    while True:
        num_items = amount_items()
        total = 0
        if num_items == 0:
            print("\nThanks, bye!")
            break
        else:
            total = for_loop(num_items)
            float(total)
            round(total, 2)
            print("Total: ", str(total))
            tax = salesTaxFunctions.sales_tax(total)
            round(tax, 2)
            total_tax = salesTaxFunctions.total_after_tax(total, tax)
            print("Sales tax:     ", str(round(tax, 2)))
            print("Total after tax: ", str(round(total_tax, 2)))
            answer = input("\nAgain? (y/n): ")
            if answer == 'n':
                print("\nThanks, bye!")
                break
            
            
def for_loop(num_items):
    total = 0
    for i in range(num_items):
                cost = int(input("Cost of item: "))
                total += cost
    return total
    

def title():
    print("Sales Tax Calculator")

def amount_items():
    item = int(input("\nENTER ITEMS (ENTER 0 TO END)"))
    return item
        






if __name__ == "__main__":
    main()
