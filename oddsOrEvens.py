import math

def main():
    print("Even or Odd Checker\n")
    user_input = int(input("Enter an integer: "))
    formula= user_input%2
    if formula > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")






if __name__ == "__main__":
    main()
