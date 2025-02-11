num1: int = int(input("first number: "))

num2: int = int(input("second number: "))

num3: int = int(input("third number: "))


if num1 >= num2 and num1 >= num3: 
    print("First number biggest: "  + str(num1))

elif num2 >= num1 and num2 >= num3:
    print("Second number biggest: "  + str(num2))                  

elif num3 >= num1 and num3 >= num2:
    print("Third number biggest: "  + str(num3))
else:
    print("Two numbers are the same")
  
