

def main():


    list_time = [48.0, 30.5, 20.2, 100.0, 42.0, 50.5, 20.6, 606.5, 501.2]
    largest = 0
    smallest = 999999999999999
    for i in range(len(list_time)):
                   temp = list_time[i]
                   if temp > largest:
                       largest = temp
                   elif temp < smallest:
                       smallest = temp
    print("this is the smallest: ", str(smallest))
    print("this is the largest: ", str(largest))

               
               
               
if __name__ == "__main__":
    main()
