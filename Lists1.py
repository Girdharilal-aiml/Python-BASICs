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

list1 = [2,54,6,1,6]

list1.append(4)                                 # adds one element at the end    [2,54,6,1,6,4]
list1.sort()                                    # sorts in ascending order [1,2,6,6,54]
list1.sort( reverse = True )                    # sorts in descending order [54,6,6,2,1]
list1.reverse()                                 # reverse list [6,1,6,54,2]
list1.insert( idx, el )                         # insert element at index