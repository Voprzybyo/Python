#! /usr/bin/env python
import os

# List files in given directory
def list_files(path):
    files_list = os.listdir(path_to_dir)
    print(files_list)

# Count files in given directory
def count_files(path):
    files_list = os.listdir(path_to_dir)
    print("Number of files in directory: ", len(files_list))


path_to_dir = 'D:/PythonProjects'  # path to directory we are working with

list_files(path_to_dir)     #List files function call
count_files(path_to_dir)    #Count files function call
