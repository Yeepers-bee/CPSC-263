
#determines country that has won the most campionships 
def main():
    dictionary = {}
    with open ("world_cup_champions.txt", 'r') as file:
        file.readline()
        file.readline()
        #getting rid of first line
        temp = file.readline()
        while temp != '':  
            split_list = temp.split(',')
            year = split_list[0]
            split_key = split_list.pop(1)
            if split_key in dictionary:
                    dictionary[split_key].append(year)
            else:      
                dictionary[split_key] = [year]
            
            temp = file.readline()
            print(f"Dictionary now: {dictionary}")
        sorted_dictionary = dict(sorted(dictionary.items()))
        headline(sorted_dictionary)



        


def headline(dictionary):
    print('Country	        Wins	Years	')
    print('=======	        ====	=====	')
    #seperator = ', '
    for key in dictionary:

        wins = 0
        for item in dictionary[key]:
            wins = wins + 1
        items_string = ', '.join(dictionary[key])
        #using formating so it is all alligned with after each of the values
        #it all has that many spaces so it all aligns nicely.
        print(f'{key:<15} {wins:<7} {items_string}')

    




if __name__ == "__main__":
    main()
