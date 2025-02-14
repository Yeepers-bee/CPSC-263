print("Tip Calculator\n")

cost = float(input("Cost of meal: "))

tip_array = [.15, .20, .25]


for i in tip_array:
    if i == .15:
        print("\n15%")
    elif i == .20:
        print("\n20%")
    else:
        print("\n25%")
        
    temp = cost * i
    tip = "%.2f"%temp 

    print("Tip amount:   ", str(tip))
    temp = float(tip) + cost
    total = "%.2f"%temp 


    print("Total amount: ", str(total))
