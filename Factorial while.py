factorial: int = int(input("Enter number for factorial: "))

count: int = 1

answer: int = 1
while(factorial < 0):

    factorial: int = int(input("Enter number for factorial: "))
    
while (count <= factorial):
    answer*= count
    count += 1 

print("The answer is: ",int(answer))

    

