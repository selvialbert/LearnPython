
def modulus_numbers(x,y):
        x = input("enter first input")
        if int(x) < 0:
            print(" please enter a positive number")
            exit()
        else:
            print("first value is" + x)
        # Get the second number
        y = input("enter second input")
        if int(y) < 0:
            print(" please enter a positive number")
            exit()
        else:
            print("second value is" + y)
        # Modulus numbers and store result
        print("results")
        z = (int(x) % int(y))
        print(z)

        return z

modulus_numbers(32,6)

