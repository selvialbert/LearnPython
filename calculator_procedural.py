# Program make a simple calculator

# show the choice to user
print("Select operation :")
print("(1) Add (+)")
print("(2) Subtract (-)")
print("(3) Multiply (*)")
print("(4) Divide (/)")
print("(5) Find Remainder (%)")
print("(6) Find Quotient (//)")
print("(7) Find Square of a number (**)")


# take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7): ")

num1 = int(input("Enter first number: "))
if int(num1) < 0:
            print(" please enter a positive number")
            exit()
num2 = int(input("Enter second number: "))
if int(num2) < 0:
            print(" please enter a positive number")
            exit()
if choice == '1':
            print(num1, "+", num2, "=", num1+num2)

elif choice == '2':
            print(num1, "-", num2, "=", num1-num2)

elif choice == '3':
            print(num1, "*", num2, "=", num1*num2)

elif choice == '4':
            print(num1, "/", num2, "=", num1/num2)

elif choice == '5':
            print(num1, "/", num2, "=", num1%num2)

elif choice == '6':
            print(num1, "/", num2, "=", num1//num2)

elif choice == '7':
            print(num1, "/", num2, "=", num1**num2)

else:
    exit()

