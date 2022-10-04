# Quack

import os


def reading(path, name):
    os.chdir(path=path)
    name = open(name, mode="r")
    content = ""
    lines = 0
    for i in name:
        content += i
        lines += 1
    print("Lines in file: ", lines)
    print("Content of file: \n", content)
    name.close()


path = input("Please provide a path to the directory the file is in: ")
name = input("Please provide the name for the file to be read: ")

reading(path, name)
