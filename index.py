print("Welcoe to my calculator")
def calculator():
    menu = input("1. Addition 2. Subtraction")
    if(menu == "1"):
        addition()
    elif(menu == "2"):
        subtraction()
    else:
        print("incorrect entry")
    
    print("Do tou want to do anything else?")
    reload = input("1. Yes 2. No")
    if(reload == "1"):
        calculator()
    else:
        print("BYE!")

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

calculator()