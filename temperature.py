temp: int = int(input("temp? "))

if 80 <= temp and temp <= 100:
                print("Temperature is ",temp,": swim")
elif 60 <= temp and temp < 80:
                print("Temperature is " ,temp, ": play golf")
elif temp < 60 :
    print("Temperature is ",temp, ": eat")
elif temp > 100:
    print ("Temperature is ",temp, ": nap")
