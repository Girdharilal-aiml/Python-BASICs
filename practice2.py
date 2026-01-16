# WAP to check if a number entered by the user is odd or even.

number1 = int(input("Enter Number1: "))
if(number1%2==0):
    print("EVEN")
else:
    print("ODD")


# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))

if(num1>num2 and num1>num3):
    print("number 1 is greatest.")
elif(num2>num1 and num2>num3):
    print("number 2 is greatest.")
elif(num3>num1 and num3>num2):
    print("Number 3 is greatest.")
else:
    print("Numbers are equal!")


# WAP to check if a number is a multiple of 7 or not.

number2 = int(input("Enter Number: "))
if(number2%7==0):
    print("Multiple of 7!")
else:
    print("Not multiple of 7!")


#WAP TO FIND OCCURENCE OF "$" IN A STRING

str1 = "Hi, I$am name$ , how we $ find $."
print(str1.count("$"))


#WAP TO TAKE USER NAME AND FIND LENGTH

name = input("Your name: ")
print(name)
print(len(name))