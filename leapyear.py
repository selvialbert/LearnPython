# Program to find out if a year is a leap year

# step 1: Get the input from user
year = int(input("Enter an Year : "))

# step 2 : Check if the year is a leap year using below logic
# Step 3: Check if year is divisible by 4. If divisible perform step 4.  If not divisible print "year is not leap year as it's not divisible by 4".

if (year%4) == 0:
    if (year%100) == 0:
        if (year%400) == 0:
            print(year, " is a leap year as it's divisible by 400")
        else: print(year, "is not a leap year as it's divisible by 100 and not 400")
    else: print(year, "is a leap year as it's divisible by 4 and not divisible by 100 or 400")
else: print(year, "is not a leap year as it's not divisible by 4")








