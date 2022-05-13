"""
Simple Script to call teh Test List from Thousand Eyes   
"""

__author__ = "Glenn Rowe"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022"
__license__ = "Cisco Sample Code License, Version 1.1"

# Import necessary modules
import os
import csv
import sys




def main():
    os.system('clear')
    menu()


def menu():
    print()
    print("************ Welcome to ThousandEyes Demo **************")
    print()

    choice = input("""
                      1: List all services
                      2: Add new services
                      3: My TE configuration

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