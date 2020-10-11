#! /usr/bin/env python

import random


def generate_numbers(how_many):
    random_numbers = list()

    for i in range(how_many):
        random_numbers.append(random.randint(1, 100))

    return random_numbers


def sort_array(tab):

    while 1:
        is_sorted = 1
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                tmp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = tmp
                is_sorted = 0
        if is_sorted == 1:
            break
    return tab


def check_sorting_correctness(tab1, tab2):
    counter = 0
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            counter += 1

    if counter == len(tab1):
        return 1
    else:
        return 0


how_many = 50
# Generate array of 50 random integers
array_of_numbers = generate_numbers(how_many)
array_of_numbers_copy = array_of_numbers        # Create copy of array to check correctness of sorting algorithm
print("\nNon-sorted array of integers: \n", array_of_numbers)   # Print non-sorted array

# Sort array using own-written algorithm
sort_array(array_of_numbers)
print("\nSorted array of integers: \n", array_of_numbers)

# Sort copy of array using build-in list method
array_of_numbers_copy.sort()

# Check correctness of sorting algorithm
res = check_sorting_correctness(array_of_numbers, array_of_numbers_copy)

if res == 1:
    print("Correctly sorted!")
else:
    print("Something went wrong. Check sorting algorithm")
