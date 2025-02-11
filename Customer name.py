name = str(input("Customer name? "))

gender = str(input("F or M? "))


if gender == "F" or gender == "f":
    print("Hello Ms." + name)  

elif gender == "M" or gender == "m": 
    print("Hello Mr." + name)

else:
    print("Incorrect input for gender. try again.")

