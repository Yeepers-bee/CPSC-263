import random


print_question = lambda num_1, num_2: print("What is ", str(num_1), "-", str(num_2), "?")

def main():
    count: int = 0
    while count < 10:
        num_1 = number_generate()
        num_2 = number_generate()
        if num_1 >= num_2:    
            print_question(num_1, num_2)
            answer = num_1 - num_2
            print(str(answer))
        else:
            print_question(num_2, num_1)
            answer = num_2 - num_1
            print(str(answer))
        
        student_answer = student_input()
        if student_answer == answer:
            print("Correct!")
        else:
            print("Incorrect!") 
        count += 1
        
        

def student_input():
    student_answer = input("Answer: ")
    return int(student_answer)


def number_generate():
    num_1 = random.randrange(0, 10)
    return num_1


if __name__ == "__main__":
    main()
