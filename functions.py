# def function_name(parameters):        -----> function definition/syntax

def hello():
    print("Hello World")

hello()      # function call 


def palindrome(str1):
    rev = ""
    for i in range(len(str1)-1,-1,-1):
        rev = rev + str1[i]
    
    if rev == str1:
        print(f"Palindrome {str1}")
    else:
        print("Not a Palindrome")


palindrome("madam")
palindrome("hello")


