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

