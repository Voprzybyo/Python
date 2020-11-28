def replace_words(path_r):

    f1 = open(path_r, "r")  # Open file to read
    text = f1.read()        # Read file and save content in "text" variable
    f1.close()              # Close file we read from

    print(text)             # Print text got from file

    dictionary = {"nigdy": "prawie nigdy", "dlaczego": "czemu", " i ": " oraz ", " oraz ": " i "}

    # for loop to check if there are words form list in "text"-string
    for word in dictionary:
        text = text.replace(word, dictionary[word])

    print(text)             # Print text with replaced words

    path_w = "D:/PythonProjects/TestowyKatalog/test6.txt"
    f2 = open(path_w, "w")  # Open file to write
    f2.write(text)          # Write text to file
    f2.close()              # Close file we wrote to

path_r = "D:/PythonProjects/TestowyKatalog/test5.txt"

replace_words(path_r)