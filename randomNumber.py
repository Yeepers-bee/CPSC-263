import random

user_input: int

random_number: int
def main():
    random_number = get_random()
    while True: 
        user_input = get_input()
        if compare(user_input, random_number) == False:
            continue
        else:
            break
            



def get_input():
    """doc stringgggg get inputttt"""
   user_input_check = int(input("Enter number guess: "))
   user_input = user_input_check
   return user_input_check


def get_random():
    """GET THAT RANDOM NUMBER"""
    random_number_check = random.randrange(0, 101)
    random_number = random_number_check
    return random_number_check
    
    

def compare(user_input, random_number):
    if user_input != int(random_number):
        if user_input > random_number:
            print("Higher then random")
            return False
        if user_input < random_number:
            print("Less than random")
            return False
    elif random_number == int(user_input):
        print("Correct!")
        return True
        
    

if __name__ == "__main__":
    main()
