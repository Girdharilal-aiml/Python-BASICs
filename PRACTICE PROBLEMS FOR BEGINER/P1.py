""" File Management System ---> CRUD Operations"""


from pathlib import Path
import os


print("1 for Creating a file")
print("2 for Reading a file")
print("3 for Appending a file")
print("4 for Deleting a file")
choice = int(input("Enter your choice: "))

def read_all_file_name():
    path = Path(__file__).parent
    items = list(path.iterdir())

    for i, item in enumerate(items):
        print(i+1, item.name)


def createfile():
    try:
        read_all_file_name()
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter the data you want to write in the file: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as e:
        print("Error: ", e)


def readfile():
    try:
        read_all_file_name()
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("Data in the file: ", data)
            print("File read successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print("Error: ", e)

def updatefile():
    try: 
        read_all_file_name()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("1 for changing name of the file")
            print("2 for overwriting data of the file")
            print("3 for appending data to the file")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_name = input("Enter the new name of the file: ")
                p2 = Path(new_name)
                p.rename(p2)
                print("File name changed successfully")

            if choice == 2:
                with open(p, 'w') as fs:
                    data = input("Enter the data you want to write in the file: ")
                    fs.write(data)
                print("File updated successfully")

            if choice == 3:
                with open(p, 'a') as fs:
                    data = input("Enter the data you want to append in the file: ")
                    fs.write(" "+data)
                print("File updated successfully")
    except Exception as e:
        print("Error: ", e)

def deletefile():
    try:
        read_all_file_name()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)

            
    except Exception as e:
        print("Error: ", e)
