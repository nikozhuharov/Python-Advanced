import os
import getpass
from os import listdir
from os.path import isfile, join, isdir

files_dict = {}
current_path = os.getcwd()


def files_collector(dir_path, files_dict):
    for file in listdir(dir_path):
        current_path = join(dir_path, file)
        if isfile(current_path):
            file_name, file_extension = file.split(".")
            if file_extension not in files_dict:
                files_dict[file_extension] = [file]
            else:
                files_dict[file_extension].append(file)
        elif isdir(current_path):
            files_collector(current_path, files_dict)


files_collector(current_path, files_dict)

# The final result will be recorded in a desktop generated text file called report.txt
path = f"C:\\Users\\{getpass.getuser()}\\Desktop"
with open(join(path, "report.txt"), "w") as f:
    for key, value in sorted(files_dict.items()):
        f.write("." + key)
        f.write("\n")
        for v in sorted(value):
            f.write("---" + v)
            f.write("\n")
