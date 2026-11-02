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
    
    for i in items:
        i = str(i)
        for j in i:
            if j == ".":
                break
        else:
            print(i)
    # for i in range(len(items)):
    #     print(f"{i+1} :  {items[i]}")

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
        
def del_folder():
    name = input("Enter a folder name your want to delete")
    p = Path(name)
    if p.exists():
        p.rmdir()
        print("folder is deleted")
        
    else:
        print("folder is not exist.")
    
def create_file(): 
    name = input("Enter a file name that you made")
    p = Path(name) 
    if not p.exists() and not p.is_file():
        with open(name,"w") as fs:
            fs.write("file is created")
        print("File created succesfully")
    else:
        print("name alredy exist try again")
        create_file()
        
def read_file():
    
    items = read_folder()
    for i in items:
        p = Path(i)
        if p.is_file():
            print(i)
    name = input("which file you want to read")
    p = Path(name)
    if p.exists and p.is_file():
        with open(name,"r") as fs:
            data = fs.read()
            print("\n\n\n you file content is \n\n\n")
            print(data)
    
    
def update_file():
    items = read_folder()
    for i in items:
        p = Path(i)
        if p.is_file():
            print(i)
    name = input("Tell your file name :-")
    p = Path(name)
    if p.exists() and p.is_file():
        print("Choose one option")
        print("Press 1 to change the name")
        print("Press 2 to overwrite the file content ")
        print("Press 3 to append new content ")
        
    res = int(input("tell you response :-"))
    if res == 1:
        new_name = input("tell your new name with extention")
        p = Path(new_name)# douth
        new_p = Path(new_name)
        p.rename(new_p)
        print("file name changes succesfully")
    elif res == 2:
        with open(p,"w")as fs:
            data = input("What do you want to overwrite:- ")
            fs.write(data)
            print("overwritten successfully")
 
    elif res == 3:
        with open(p,"a")as fs:
            data = input("What do you want to overwrite:- ")
            fs.write(data)
            print("Append successfully")  

def delete_file():
    items = read_folder()
    for i in items:
        p = Path(i)
        if p.is_file():
            print(i)
    name = input("tell your file exists pleasetry again")
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)

    else:
        print("no such file exists please try again")
        delete_file()     
        
    
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
        
if res == 4:
    del_folder()

if res == 5:
    create_file()
    
if res == 6:
    read_file()
if res == 7:
    update_file()
if res == 8:
    delete_file()