
def multiply_numbers(x,y):
    z = int(x) * int(y)
    print(int(z))

    x = input("Enter first value")
    y = input("Enter Second Value")
    if (int(x) <= 0 or int(y) <= 0):
        print(" please enter a positive number")
        exit()
    else:
        z = int(x) * int(y)
        print(x,"x",y,"=",int(z))


multiply_numbers(18,20)
