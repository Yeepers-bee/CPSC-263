n1 = int(input("First number: "))
n2 = int(input("Second number: "))


result = n1 if n1 < n2 else n2


while result > 0:
    if ((n1 % result) == 0) and ((n2 % result) == 0):
        break
    result -= 1

#if (n1 >= n2): 
 #   for i in range(1, result, 1):
     #   test1: str = i % n1 
     #   test2: str = i % n2

        





      #  if (isdigit(test1)) or test2 is float):
      #      continue
      #  else:
       #     k = i
       #     if largest < k:
       #         largest = k
        #   else:
         #       continue


print("The largest divisor is ", str(result))

                
                
        
        
