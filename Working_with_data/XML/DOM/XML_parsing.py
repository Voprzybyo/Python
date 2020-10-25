#! /usr/bin/env python

import xml.dom.minidom


domtree = xml.dom.minidom.parse('D:/PythonProjects/Start/XML_file.xml')
team = domtree.documentElement
persons = team.getElementsByTagName('person')  # Collection of all element with tag 'person' in 'team' block

for person in persons:
    print("\n****** PERSON *******")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))

    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Salary: {}".format(person.getElementsByTagName('salary')[0].childNodes[0].data))

# Change values of XML blocks
persons[1].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Claude Shannon"   # Change name of second person
persons[0].setAttribute('id', '20')                                                     # Change ID of first person
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "68"                # Change age of fourth person


newperson = domtree.createElement('person')
newperson.setAttribute('id', '5')

# Create independent elements (not associated with newperson yet)
# NAME
name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Freddie Mercury'))

# AGE
age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('32'))

# SALARY
salary = domtree.createElement('salary')
salary.appendChild(domtree.createTextNode('1900'))

# Assign name, age and salary to newperson
newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(salary)

# Add newperson to 'team' block
team.appendChild(newperson)

domtree.writexml(open('New_XML_added_data.xml', 'w'))
