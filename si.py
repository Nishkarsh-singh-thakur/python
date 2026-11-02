from pathlib import Path
import os

def create_folder():
    name = input("tell your folder name :- ")
    p = Path(name)
    if p.exists():
        print("folder already exist try again ")
        create_folder()
    else:
        p.mkdir()
        print("new folder created successfully!")

def read_folder():
    p = Path("")
    items = list(p.rglob("*"))
    return items


def update_folder():
    items = read_folder()
    for i in items:
            i = str(i)
            for j in i:
                if j == ".":
                    break
            else:
                print(i)
    name = input("which folder you want to update :- ")
    old_p = Path(name)

    if old_p.exists():
        new_name = input("Enter your new name:- ")
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("updated successfully ")

    else:
        print("name does not exist try again ")
        update_folder()


def delete_folder():
    name = input("tell your folder name :- ")
    p = Path(name)
    if not p.exists():
        print("folder doesn't exist try again ")
        delete_folder()
    else:
        p.rmdir()
        print("folder deleted successfully!")


def create_file():
    name = input("Tell your file name with extension :- ")
    p = Path(name)
    if p.exists() and p.is_file():
        print("File name already exist please Try again ")
        create_file()
    else:
        with open(p,"w") as fs:
            data = input("what do you want to write :- ")
            fs.write(data)
            print("file created successfully")

def read_file():
    items = read_folder()
    for i in items:
        p = Path(i)
        if p.is_file():
            print(i)
    name = input("which file you want to read :- ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as fs:
            data = fs.read()
            print("\n\n\n\nyou file content is \n\n\n\n")
            print(data)             
    else:
        print("no such file exists please try again ")
        read_file()

def update_file():
    items = read_folder()
    for i in items:
        p = Path(i)
        if p.is_file():
            print(i)

    name = input("Tell your file name :- ")
    p = Path(name)
    if p.exists() and p.is_file():
        print("Choose one option ")
        print("press 1 to change the name")
        print("press 2 to overwrite the file content")
        print("press 3 to append new content ")

        res = int(input("tell your response :- "))

        if res == 1:
            new_name = input("tell new name with extension ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("file name changes successfully ")

        elif res == 2:
            with open(p,"w") as fs:
                data = input("What do you want to overwrite:- ")
                fs.write(data)
                print("overwritten successfully ")

        elif res == 3:
            with open(p,"a") as fs:
                data = input("What do you want to Append:- ")
                fs.write(data)
                print("Appended successfully ")




print("press 1 - for creating a folder")
print("press 2 - for reading a folder")
print("press 3 - for updating a folder")
print("press 4 - for deleting a folder")
print("press 5 - for creating a file")
print("press 6 - for reading a file")
print("press 7 - for updating a file")
print("press 8 - for deleting a file")

res = int(input("Tell your response :- "))

if res == 1:
    create_folder()

if res == 2:
    items = read_folder()
    for i in range(len(items)):
        print(f"{i+1} : {items[i]}")


if res == 3:
    update_folder()

if res == 4:
    delete_folder()

if res == 5:
    create_file()

if res == 6:
    read_file()

if res == 7:
    update_file()