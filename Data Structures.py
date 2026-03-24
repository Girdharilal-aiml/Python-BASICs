# Data structures are used to store, organize, and manipulate 
# data efficiently. Python provides several built-in data 
# structures
# And for storing multiple values we will again use variables

# Now in python we have 4 types of in-build data structure 
# List, Tuple, Dictionary, Set 



# SHALLOW COPY
x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print(x)   # [1, 2, 3, 4, 5]
print(y)   # [100, 2, 3, 4, 5]



# DEEP COPY
f = [1, 2, 3, 4, 5]
g = f
g[0] = 100
print(f)   # [100, 2, 3, 4, 5]
print(g)   # [100, 2, 3, 4, 5]



# DICTIONARY
# A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed
d = {"name": "Alice", "age": 30, "city": "New York"}
print(d)   
print(type(d))
print(d["name"])   # Accessing value using key
print(d.get("age"))  # Accessing value using get method

for i in d:
    print(d[i])   # Accessing values using keys

for i in d.values():
    print(i)

