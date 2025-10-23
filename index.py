print("Welcome to my calculator")
def calculator():
    menu = input("1. Addition 2. Subtraction 3. Multiplication 4. Division")
    if(menu == "1"):
        addition()
    elif(menu == "2"):
        subtraction()
    elif(menu == "3"):
        multiplication()
    elif(menu == "4"):
        division()
    else:
        print("incorrect entry")
    
    print("Do tou want to do anything else?")
    reload = input("1. Yes 2. No")
    if(reload == "1"):
        calculator()
    else:
        print("BYE!")
        print("See you again")

def addition():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first + second
    print(result)

def subtraction():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first - second
    print(result)

def multiplication():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first * second
    print(result)

def division():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first / second
    print(result)
calculator()