

def main():
    while True:
        user_input = int_enter()
        factors = divisble(user_input)
        int(factors)
        if factors == 2:
            print(str(user_input), "is a prime number.")
        else:
            print(str(user_input), "is NOT a prime number.")
            print("It has ", str(factors), " factors.")
        answer = input("\nTry again? (y/n): \n")
        if answer == 'n':
                  print("\nBye!")
                  break

def title():
    print("Prime Number Checker\n")
    


def int_enter():
    user_input = int(input("Please enter an integer between 1 and 5000: "))
    if user_input == 1:
        print("Invalid integer. Please try again.")
        int_enter()
    else:   
        return user_input
    
def divisble(user_input):
    factors:int = 0
    for i in range(user_input):
        
        temp = user_input % (i + 1)
        if temp == 0:
            factors = factors + 1
    return factors



    
        
        
        


















if __name__ == "__main__":
    main()
