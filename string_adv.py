# STRING FUNCTIONS

str1 = "i am coder."

str1.endswith("ER")                         #returns true is string ends with substr
print(str1.endswith("er.")) 


str1.capitalize()                           #capitablizes 1st char
print(str1.capitalize())


# str.replace(old,new)                      replaces all occurrences of old with new
str1.replace("coder","designer")
str1 = str1.replace("coder","designer")
print(str1)


# str.find(word)                            returns 1st index of 1st occurrence
print(str1.find("a"))

str1.count("AM")                            #counts the occurrence of substr in string