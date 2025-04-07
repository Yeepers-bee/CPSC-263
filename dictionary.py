


#keys and values. soore as key 5 scores. put in dictionary
#sort based on score.


def main():
    count: int = 0
    dic= {}
    while True:
        user_input = input("Give assignment key:")
        user_score = input("Score: ")
        dic[user_input] = user_score
        count = count + 1

        if count == 5:
            break

    list_key = list(dic.keys())
    list_key.sort()
    for key in list_key:
        print(key + "      " + dic[key])
    
        




if __name__ == "__main__":
    main()
