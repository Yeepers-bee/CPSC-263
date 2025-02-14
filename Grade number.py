
print("Letter Grade Converter\n") 

continue_input = "y"


while continue_input == "y" or continue_input == "Y": 
    grade = int(input("Enter numerical grade: ")) 
    if 90 <= grade: 
        letter: str = "A" 
    elif 80 <= grade < 90: 
        letter: str = "B"
    elif 70 <= grade < 80: 
        letter: str = "C"
    elif 60 <= grade < 70: 
        letter: str = "D"
    else:
        letter: str = "F"
    print("Letter grade: ", letter) 
    continue_input: str = input("\nContinue? (y/n)")
