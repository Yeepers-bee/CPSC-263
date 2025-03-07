

def main():
    l = []
    while True: 
        temp = user_array()
        l.append(temp)
        temp_answer = input("Continue? (y/n)")
        l.append(temp)
        if temp_answer == 'n':
            break
    user_num = user_input()
    for i in range(len(l)):
        if l[i] == user_num:
            l[i] = 0
        else:
            continue
    print("The max is: ", str(max(l)))
    print("The min is: ", str(min(l)))

        










def user_array():
    temp = int(input("Input number for list: "))
    return temp
 
    
        
    
def user_input():
    temp = int(input("Input number for replacement: "))
    return temp


#only works if directly executed

if __name__ == "__main__":
    main()

    
