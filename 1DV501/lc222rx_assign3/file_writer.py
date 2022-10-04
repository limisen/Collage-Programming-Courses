# Quack

import os


def writing(path, name, content):
    os.chdir(path)
    name = open(name, mode="w")
    name.write(content)
    name.close()


path = input("Please provide a path for where to save your file: ")
name = input("Please provide a suitable name for the file: ")
content = ""
print("Please provide the content for the file, \"stop\" to stop writing: ")
x = ""
while x.lower() != "stop":
    content += x + "\n"
    x = input()

writing(path, name, content)
