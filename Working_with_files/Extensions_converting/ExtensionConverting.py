#! /usr/bin/env python

import os

#Function changing extension of files in given directory
def change_extension(path, current_extension, dest_extension):

    os.chdir(path)                                          # Change directory to given path
    for filename in os.listdir(path):

        if filename.endswith(current_extension):            # Checking if file has .jpg extension
            prefix = filename.split(".")[0]                 # This method separate name of file from given extension
            os.rename(filename, prefix + dest_extension)    # Rename files (extension change)


path = "D:/PythonProjects/TestowyKatalog"

change_extension(path, ".jpg", ".png")
