""" A Built-in data types that stores set of values
    It can store elements of DIFFERENT TYPES (integer, float, string, etc) """

# List is Mutable, slicing possible

# variable = [value1,value2,...]            ---> LIST

marks = [21.2, 2143.4, 45.5, 65.7]
print(marks)
print(type(marks))
print(len(marks))
print(marks[2:3])           # Slicing 


Student1 = ["Girdhari lal", 19 , 98.5]
print(Student1)


# LIST METHODS

# All changes are made in original list

list1 = [2,6,8,-4,-10]
print(list1)

list1.append(4)                                 # adds one element at the end    [2,6,8,-4,-10,4]
print(list1)

list1.sort()                                    # sorts in ascending order [-10,-4,2,4,6,8]
print(list1)

list1.sort( reverse = True )                    # sorts in descending order [8,6,4,2,-4,-10]
print(list1)

list1.reverse()                                 # reverse list [4,-10,-4,8,6,2]
print(list1)

list1.insert( 3 , 5 )                    # insert element at index
print(list1)



