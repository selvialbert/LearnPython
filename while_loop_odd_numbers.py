def odd_numbers():

    print("Printing Odd Numbers")
    x = (int(input("Enter a number :")))
    print("You entered :", x)

    y = (int(input("How many odd numbers you wish to print?")))
    print("Printing {0} numbers after {1}:".format(y,x))

# loop condition
    i=0
    while i in range(0,y):
        i=i+1
        if x%2 != 0:
            x = x+2
        else:
           x = x + 1
        print(x)


odd_numbers()
