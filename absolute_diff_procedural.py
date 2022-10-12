# Get the first number
x = input("enter first input")
print("first value is" + x)
# Get the second number
y = input("enter second input")
print("second value is" + y)
# abs diff numbers and store result
print("results")
z = (int(x) - int(y))
# print result
if z < 0:
    print(abs(z))
else:
    print(z)