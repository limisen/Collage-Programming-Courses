# A program with two functions;
# function one counts the number of directories
# function two counts the number of files

import os


def count_directories(path):  # Returns the number of directories
    count_dir = 1
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir():
            count_dir += count_directories(entry.path)
    return(count_dir)


def count_files(path):  # Returns the number of files
    count_file = 0
    for entry in os.scandir(path):
        if entry.is_file() and not entry.name.startswith("."):
            count_file += 1
    return(count_file)


path = "C:/Users/liamc/Documents/VS Code - Folders/Programing courses/1DV501"


print(f"I am right now at: {path}")
print(f"Below me, I have {count_directories(path)} directories/folders")
print(f"This directory contains {count_files(path)} files")
