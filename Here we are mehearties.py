

def main():
    dictionary = {}
    char_array = []
    num_array = []
    user_input = input("Write down values")
    with open('values.txt', 'w') as file:
        file.writelines(user_input)       
    with open('values.txt', 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                print("End of file")
                break
            if char.isalpha() == True:
                char_array.append(char)
                print(char_array)
            
            elif char.isdigit() == True:
                num_array.append(char)
                print(num_array)
    count = 0
    for item in char_array:
        dictionary[char_array[count]] = num_array[count]
        count = count + 1
    with open('results.txt', 'w') as file:
        file.writelines(dictionary)










        





if __name__ == "__main__":
    main()

