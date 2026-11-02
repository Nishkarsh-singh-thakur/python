from pathlib import Path
import os

def create_folder():
    name = input("tell name of folder")
    p = Path(name)
    if p.exists():
        print("folder already exist try again")
        create_folder()
    else:
        p.mkdir()
        print("new folder created succesfully !")

def read_folder():
    p = Path("")
    items = list(p.rglob("*"))
    for i in range(len(items)):
        print(f"{i+1} :  {items[i]}")

def update_folder():
    read_folder()
    name = input("Enter a folder name that you want to update")
    old_p = Path(name)
    if old_p.exists():
        new_name = input("enter your new name:-")
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("update folder")
    else:
        print("Name alredy exist")
        update_folder()
    
print("press 1 - creating a folder")
print("press 2 - reading a folder")
print("press 3 - updating a folder")
print("press 4 - deleting a folder")
print("press 5 - creating a file")
print("press 6 - reading a file")
print("press 7 - updating  file")
print("press 8 - deleting a file")

res= int(input("Tell your response:- "))
if res == 1:
    create_folder()
    
if res == 2:
    read_folder()
if res == 3:
    update_folder()
        
    





