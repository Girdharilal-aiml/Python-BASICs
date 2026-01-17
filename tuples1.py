"""   A built-in data type that lets us create immutable sequence of values   """

tuple1 = (4,2,3,6,1)
print(type(tuple1))
print(tuple1[2])
# tuple1[0] = 44            ---> Not Allowed 

# single value tuple

tuple2 = (2, )                  # , is compulsory else it would be consider as another type
print(type(tuple2))
print(tuple2)

# METHODS

print(tuple1.index(1))          # Returns Index

print(tuple1.count(2))          # Returns number of occurence

