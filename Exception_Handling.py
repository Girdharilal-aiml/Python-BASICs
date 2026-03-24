age = int(input("Enter your age: "))
try:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:    print("Your age is:", age)

except ValueError as e:
    print("Error:", e)



a = int(input("Enter a number: "))
try:
    result = 10 / a
    print("Result:", result)    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division successful.")

finally:    print("Execution completed.")