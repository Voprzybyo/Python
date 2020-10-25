#! /usr/bin/env python

import xml.sax


# Inherit from xml.sax.ContentHandler
class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attributes):
        self.current = name
        if self.current == "person":
            print("\n****** PERSON ******")
            print("ID: {}".format(attributes['id']))

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "salary":
            self.salary = content

    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "age":
            print("Age: {}".format(self.age))
        elif self.current == "salary":
            print("Salary: {}".format(self.salary))
        self.current = ""


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('D:/PythonProjects/Start/XML_file.xml')

