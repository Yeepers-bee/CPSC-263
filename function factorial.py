
##variable = int(input("Write number for factorial: "))

def factorial (param : int):
    loop:int = param
    result: int = 0
    while loop > 0:
        print("Went in loop")
        result += loop
        loop -= 1
    print("The factorial for",str(param), " is ", str(result))
    




    
