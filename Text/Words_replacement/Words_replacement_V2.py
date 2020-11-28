def replace_words(old_words, new_words, path_r):

    f1 = open(path_r, "r")  # Open file to read
    text = f1.read()        # Read file and save content in "text" variable
    f1.close()              # Close file we read from

    print(text)             # Print text got from file

    dictionary = {old_words[0]: new_words[0], old_words[1]: new_words[1], old_words[2]: new_words[2], old_words[3]: new_words[3]}
    # for loop to check if there are words form list in "text"-string
    for word in dictionary:
        text = text.replace(word, dictionary[word])

    print(text)             # Print text with replaced words

    path_w = "D:/PythonProjects/TestowyKatalog/test6.txt"
    f2 = open(path_w, "w")  # Open file to write
    f2.write(text)          # Write text to file
    f2.close()              # Close file we wrote to


path_r = "D:/PythonProjects/TestowyKatalog/test5.txt"

# word_list_to_replace_test = ["i", "oraz", "nigdy", "dlaczego"]

# Get and parse 4 words to replace in text
old_words = input("Please enter 4 words you want to replace in .txt file: ")
old_words = old_words.split()

# Get and parse 4 new words the old ones will be replaced by
new_words = input("Please enter 4 new words: ")
new_words = new_words.split()

replace_words(old_words, new_words, path_r)
