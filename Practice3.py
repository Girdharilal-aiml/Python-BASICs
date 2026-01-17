# WAP to store the above values in a list & sort them from "A" to "D"

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)


# WAP to count the number of students with the "A" grade in the following tuple

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method )

list2 = [1,2,3,2,1]
print(list2)

list3 = list2.copy()
print(list3)

list3.reverse()
print(list3)

if(list2 == list3):
    print("PALINDROME")
else: 
    print("NOT PALINDROME")


# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

mov1 = input("Enter first movie name: ")
mov2 = input("Enter second movie name: ")
mov3 = input("Enter third movie name: ")

list1 = []

list1.append(mov1)
list1.append(mov2)
list1.append(mov3)

print(list1)