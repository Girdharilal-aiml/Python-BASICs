#TAKE TWO NUMBERS AND PRINT THEIR SUM

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

print("sum is: ", num1 + num2)

#TAKE SIDE OF SQUARE AND FIND AREA

side = int(input("Enter side lenght: "))
print("Area is:", side*side)                    # or side power 2 which = side**2


#TAKE TWO FLOATING NUMBERS AND PRINT THEIR AVERAGE

num3 = float(input("Enter 1st floating number: "))
num4 = float(input("Enter 2nd floating number: "))
print("Average is:", (num3+num4)/2) 

#TAKE TWO NUMBERS AND PRINT TRUE IF A == B OR A>=B ELSE FALSE

num5 = int(input("Enter a: "))
num6 = int(input("Enter b: "))
if(num5>=num6 or num5==num6):
    print(True)
else:
    print(False)