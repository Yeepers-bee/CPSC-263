s = 10000 #global varaible

#try not to use global variables as they are a pain to change
#might as well make it constant then




def sum (*arg):
    s=0
    for k,v in arg.items: ##This is how it works for passing key and value to arg
        s+=i
    return s

def main():
    ##if it does not have a global variable here then it would look for them if you ask for
    #suches presence.
    global s = 100 # changes global variable
    print("sum=", sum(n1=1,n2=2,n3=3,n4=4))
    print("sum=", sum(n1=1,n2=4))
    print("sum=", sum(n1=1,n2=2,n3=3,n4=4,n100=100,n200=200))
    print("sum=", sum())      

    
    while true:
        i=int(input("Input numbers to sum, 0 to exit"))
        if i == 0:
            break

#**kwags something you use as argument. short for keyword arguments. **kwags when you use this you are able
        #to pass both the key and the value. 


