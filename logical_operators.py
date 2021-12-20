#the basic logical operators are AND, OR , NOT 

temp = int(input("what is the temperature outside: "))

if temp >= 0 and temp <=30:
    print("Temp is good today and you should go outside")

elif temp<0 or temp>30:
    print("Temp is not good today and should be inside")
