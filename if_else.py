#if statement = block of code that will execute when condition is true 

age = int(input("how old are you: "))

if age >= 18:
    print("You are an adult")
elif age<0:
    print("You are not born yet")
else:
    print("You are a child!")