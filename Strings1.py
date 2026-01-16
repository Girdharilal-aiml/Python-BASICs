# WAYS OF WRITING STRINGS
str1 = "This is a string."
str2 = 'This is also a string.'
str3 = """And this is also a string."""

# BASIC OPERATOR
str4 = "String with line break. Here comes next line"               
str5 = "String with line break. \nHere comes \tnext line"         # \n for new line and \t for tab space

print(str4)
print(str5)

str6 = "HELLO"
str7 = "WORLD"
print(str6+str7)        # + for concatenating

len1 = len(str1)               # len will will character length of a string
print(len1)                    # len + 1

# INDEXING

str8 = "WINTIP LABS"
print(str8[0])       # W
print(str8[6])       # " "
print(str8[7])       # L
# str8[0] = "G"           Not possible , Only access but cannot modify


# SLICING

#str[starting index : Ending Index]             ending idx will not be included

print(str8[6:10])           # " LAB"      S is on 10 index which is not included
print(str8[6:11])           # " LABS"

#negative indexing

"""A   P   P   L   E
  -5  -4  -3  -2  -1                like this
"""
str9 = "APPLE"
print(str9[-3:-1])                  # "PL"