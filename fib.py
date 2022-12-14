
# 0,1,1,2,3,5


#Step 1 : enter first number

startnum = int(input("Enter your number :"))

#Step 3: Ask the user how many fibonacci numbers they wish to print and accept that from command line
count = int(input("How many fibonacci numbers do you wish to print?"))

if count < 0:
    print("Please enter a valid count")
    exit()

a = 0
b = 1
#c = a+b

if startnum < 0:
    if count == 1:
        print(a)
        exit()
    elif count == 2:
        print(a,b)
        exit()
    elif count == 3:
        print(a,b,c)
        exit()
    elif count > 3:
        print(a, b, c)
        count = count-3
        a=1
        b=1
elif startnum == 0:
    if count == 1:
        print(a)
        exit()
    if count == 2:
        print(a,b)
        exit()
    if count > 2:
        print(a, b)
        count = count - 2
        a = 1
        b = 1
for i in range(0,count):
    if count>0:
        c=a+b
        if c > startnum:
            print(c)
            count = count-1
            a=b
            b=c
















