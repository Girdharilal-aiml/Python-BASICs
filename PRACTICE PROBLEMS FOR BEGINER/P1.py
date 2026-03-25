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
     

