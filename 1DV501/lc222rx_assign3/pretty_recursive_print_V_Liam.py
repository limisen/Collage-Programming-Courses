# Boop
import os


dir_list = []
curr_index = -1


def print_containt(dir_path):
    global curr_index
    if curr_index >= 0 and not curr_index > len(dir_list):
        curr_index += 1
    else:
        curr_index = 0
    for entry in dir_path:
        if entry.is_file() and not entry.name.startswith("."):
            print("  File:", entry.name)
        elif entry.is_dir() and not entry.name.startswith("."):
            print("Dir:", entry.path)
            dir_list.append(entry.path)
            dir_path = entry.path
            dir_path = os.scandir(dir_path)
            print_containt(dir_path)
            print()


dir_path = "C:/Users/liamc/Documents/VS Code - Folders/"
dir_path += "Programing courses/"
entries = os.scandir(dir_path)          # List of entries of type DirEntry
print_containt(entries)
