#get first number
x = input("enter first input")
if int(x) < 0:
    print (" please enter a positive number")
    exit()
else:
    print("first value is" + x)

# Get the second number
y = input("enter second input")
if int(y) < 0:
    print (" please enter a positive number")
    exit()
else:
    print("second value is" + y)

#print result
print("results")
# abssolute diff
z = (int(x) - int(y))
print (abs(z))
