
def fibonacci_numbers():
    x = int(input("Enter a number:"))
    print(f"You entered {x}")
    y = int(input("How many fibonacci numbers you wish to print?"))


    a = 0
    b = 1
    c = a+b
    print(c)
    a = b
    b = c
    c = a+b
    print(c)



fibonacci_numbers()