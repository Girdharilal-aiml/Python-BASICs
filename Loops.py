# 2 Types of LOOP ----> FOR AND WHILE

# While works on Condition
# For works on Number

# FOR LOOP                  ---> range(Start, Stop, Steps)
a = range(1,20,1)
for i in a:
    print(i)

for i in range(1,10,2):
    print(i)

# Table of 5

for i in range(5,51,5):
    print(i)

# Which Table you want?
n = int(input("Enter number of table you want?: "))

for i in range(n,(n*10)+1,n):
    print(i)


# String in LOOP

b = "Learning is key to success"
print(len(b))

