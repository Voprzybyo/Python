#! /usr/bin/env python

import os

def list_subdir(path):

    for root, dirs, files in os.walk(path):

        path = root.split(os.sep)    # os.sep -> the character used by the operating system to separate pathname components. This is '/'
        print( (len(path) - 1) * '->', os.path.basename(root))

        for file in files:
          print(len(path) * '->', file)


list_subdir("D:/PythonProjects/TestowyKatalog")
list_subdir("D:/PythonProjects")