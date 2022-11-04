
def modulus_numbers(x,y):
    x = input("Enter first value")
    y = input("Enter Second Value")
    if (int(x) <= 0 or int(y) <= 0):
        print(" please enter a positive number")
        exit()
    else:
        z = int(x) % int(y)
        print(x, "modulus", y, "=", int(z))

modulus_numbers(32,6)

