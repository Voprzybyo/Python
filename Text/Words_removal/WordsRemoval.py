#! /usr/bin/env python

# Function removing given in list words from given file path
def remove_words(word_list, path_r):

    f1 = open(path_r, "r")  # Open file to read
    text = f1.read()        # Read file and save content in "text" variable
    f1.close()              # Close file we read from

    print(text)             # Print text got from file

    # for loop to check if there are words form list in "text"-string
    for i in range(len(word_list)):
        text = text.replace(word_list[i], "")   # Replace word from list with empty string

    print(text)             # Print text without words we wanted to remove

    path_w = "D:/PythonProjects/TestowyKatalog/test2.txt"
    f2 = open(path_w, "w")  # Open file to write
    f2.write(text)          # Write text to file
    f2.close()              # Close file we wrote to


path = "D:/PythonProjects/TestowyKatalog/test.txt"

word_list_to_remove_test = ["się", "i", "oraz", "nigdy", "dlaczego"]

word_list_to_remove = input("Please enter words you want to remove from .txt file...")
word_list_to_remove = word_list_to_remove.split()

remove_words(word_list_to_remove, path)
