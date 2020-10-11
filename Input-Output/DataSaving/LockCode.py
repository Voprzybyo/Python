#! /usr/bin/env python

# Function checking if given lock code is correct
def open_lock(given_code, password):
    if password == given_code:
        print("Lock code is correct!")
    else:
        print("Lock code is incorrect!")


# Set lock code
lock_code = input("Please enter lock code (it will be set as a key needed to unlock the lock (f.e. in chest) in the future)")

password = input("Please enter lock code...") # Enter lock code

open_lock(lock_code, password)  # And check if is correct (match with setted before)