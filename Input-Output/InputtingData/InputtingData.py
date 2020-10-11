#! /usr/bin/env python

#print ("Please type your firstname, last name and year of birth (in single line)")

def splitdata(data):
    
    data = data.split()
    print("First Name: " + data[0])
    print("Last Name: " + data[1])
    print("Year of birth: " + data[2])



data = input("Please type your firstname, last name and year of birth (in single line)")
print(data)

splitdata(data)