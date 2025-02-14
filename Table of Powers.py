
print("Table of Powers\n") 

booll: bool = True
while booll:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))
    if start < stop:
        print("\nNumber   Squared Cubed")
        print("======   ======= =====")
        break
    else:
        print("Error: start is larger then stop. try again!")



    
for i in range(start, stop + 1):
    square = i ** 2
    cube = i ** 3
    print(str(i),"\t",str(square),"\t", str(cube))
