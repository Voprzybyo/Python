#! /usr/bin/env python

import json


# function to add to JSON
def write_json(filename='D:/PythonProjects/Start3/SensorsData2.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Show content function
def showContent():

    for SensorsReadings in data['SensorsReadings']:
        print(SensorsReadings)  # Print all content
        # print(SensorsReadings['Temperature'], SensorsReadings['Time'])  # Print temperature value with timestamp
    print("")


# Write record to JSON file
def writeRecord():
    temperature = input("Temperature: ")
    humidity = input("Humidity: ")
    time = input("Time: ")

    # Data to be written
    data_to_write = {
        "Temperature": temperature,
        "Humidity": humidity,
        "Time": time,
    }

    temp = data['SensorsReadings']
    temp.append(data_to_write)  # Add new record to .json file
    write_json(data)
    print("\nAdding record:\n", data_to_write, "\nto file\n")


def deleteRecord():

    record_to_delete_time = input("Enter time. Sensors data with given timestamp will be deleted.")
    print(record_to_delete_time)
    for SensorsReadings in data['SensorsReadings']:
        print(SensorsReadings['Time'])
        if SensorsReadings['Time'] == str(record_to_delete_time):
            del SensorsReadings['Time']
            del SensorsReadings['Temperature']
            del SensorsReadings['Humidity']
            write_json(data)


# MAIN
while 1:
    with open('D:/PythonProjects/Start3/SensorsData2.json') as f:
        data = json.load(f)

    print("What do you want to do?")
    print("1. Show content of JSON file")
    print("2. Add record")
    print("3. Delete record")
    print("4. Exit")

    # Removing Nested None Dictionaries
    # Using filter() + dict()
    # Removing Nested None Dictionaries
    # Using dictionary comprehension
    data = {key: val for key, val in data.items() if val}
    write_json()

    choice = int(input())
    if choice == 1:
        showContent()
    elif choice == 2:
        writeRecord()
    elif choice == 3:
        deleteRecord()
    elif choice == 4:
        break
    else:
        print("Wrong choice! Choose 1,2 or 3\n")

f.close()
