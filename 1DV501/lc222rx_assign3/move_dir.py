# A program with two functions;
import os


def list_dir(path):  # Returns the directories in a list
    lst_dir = []
    for entry in path:
        if entry.is_dir():
            lst_dir.append("Dir: " + str(entry.name))
    return(lst_dir)


def list_files(path):  # Returns the files in a list
    lst_file = []
    for entry in path:
        if entry.is_file():
            lst_file.append("File: " + str(entry.name))
    return(lst_file)


path = "C:/Users/liamc/Documents/VS Code - Folders/Programing courses"
path += "/1DV501/lc222rx_assign3"

a = None
while a != 4:
    print("1. List directories\n2. Change directory\n3. List files\n4. Quit")
    a = int(input("\n\n==> "))
    if a == 1:
        if len(list_dir(os.scandir(path))) == 0:
            print("No directories in current directory")
        if len(list_dir(os.scandir(path))) > 0:
            for i in range(len(list_dir(os.scandir(path)))):
                print(list_dir(os.scandir(path))[i])
        print()
    elif a == 2:
        print(os.getcwd())
        path = os.chdir(input("Name of directory to enter: "))
        print("\n", os.getcwd())
    elif a == 3:
        if len(list_dir(os.scandir(path))) == 0:
            print("No directories in current directory")
        if len(list_dir(os.scandir(path))) > 0:
            for i in range(len(list_files(os.scandir(path)))):
                print(list_files(os.scandir(path))[i])
        print()
