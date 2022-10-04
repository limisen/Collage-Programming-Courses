# Boop
import os


def pretty_print(dir_path, depth):
    depth = 0
    dir_list = []
    if depth >= 0 and not depth > len(dir_list):
        depth += 1
    for entry in dir_path:
        if entry.is_file() and not entry.name.startswith("."):
            print("  " * depth, entry.name)

        elif entry.is_dir() and not entry.name.startswith("."):
            print("  " * (depth-1), entry.path)
            dir_list.append(entry.path)
            dir_path = entry.path
            dir_path = dir_path
            pretty_print(dir_path)


dir_path = "C:/Users/liamc/Documents/VS Code - Folders/"
dir_path += "Programing courses/"
depth = 1
entries = os.scandir(dir_path)
pretty_print(dir_path, depth)
