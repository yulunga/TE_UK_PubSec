"""
Simple Script to call teh Test List from Thousand Eyes   
"""

__author__ = "Glenn Rowe"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022"
__license__ = "Cisco Sample Code License, Version 1.1"

# Import necessary modules
import csv
import sys

def main():
   menu()


def menu():
    print("************ Welcome to ThousandEyes Demo **************")
    print()

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        register()
    elif choice == "B" or choice =="b":
        login()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def register():
   pass
    
def login():
   pass
    
#the program is initiated, so to speak, here
main()