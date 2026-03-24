age = int(input("Enter your age: "))
try:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:    print("Your age is:", age)

except ValueError as e:
    print("Error:", e)


