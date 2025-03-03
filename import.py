import randomNumber

user_input: int

random_number: int
def main():
    random_number = randomNumber.get_random()
    while True: 
        user_input = randomNumber.get_input()
        if compare(user_input, random_number) == False:
            continue
        else:
            break


if __name__ == "__main__":
    main()
