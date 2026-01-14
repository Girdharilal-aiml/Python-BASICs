# Python is INDENTATION language which mean 4 spaces befor statement

""" if(Condition):
    statment 1              ---> Give 4 spaces before statments
elif(Condition):
    statment 2
else:
    statment 3 """                 

# For Example

light = input("Light is : ")

if(light=="red"):
    print("STOP")
elif(light=="yellow"):
    print("WAIT")
elif(light=="green"):
    print("GO")
else:
    print("Invalid Signal")


# Example 2

marks = int(input("Enter your marks:"))

if(marks>=90):
    print("A+")
elif(marks>=80):
    print("A")
elif(marks>=70):
    print("B")
elif(marks>=60):
    print("C")
elif(marks>=50):
    print("D")
elif(marks<=50):
    print("F")
else:
    print("Invalid Signal")


""" Single Line if / Ternary Operation
<var> = <value1> if <condition> else <value2>  
    FIRST  """

food = input("Food is: ")
eat = "Yes" if food=="cake" else "No"
print(eat)



""" SECOND   
    <statment1> if <condition> else <statment2>     """

fruit = input("Enter fruit: ")
print("sweet") if fruit == "apple" or fruit == "pineapple" else print("Not sure")