
"""
Simple Script to call teh Test List from Thousand Eyes   
"""

__author__ = "Glenn Rowe"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022"
__license__ = "Cisco Sample Code License, Version 1.1"

# Import necessary modules
import requests
import json
from configparser import ConfigParser

# Disable warnings
requests.packages.urllib3.disable_warnings()

def get1_token():
    global tokenKey, base_url
    te_api_config = ConfigParser()
    te_api_config.read("TE_Token_Access.ini")
    tokenKey = te_api_config['TE']['token']
    base_url = te_api_config['TE']['base_url']
    
def TE_test_list(token, url):
    # Define API Call
    api_call = "/tests.json"

    # Header information
    headers = {"Authorization": tokenKey, "Content-Type": "application/json", "Accept": "application/json"}

    # Combine URL, API call and parameters variables
    url += api_call

    resp = requests.get(url, headers=headers, verify=False).json()

    # Get teh TE Test list from the reponse and return
    TEtestlist = resp["test"]
    return TEtestlist

def call_TE_test():
# Assign obtained authentication token to a variable
# URL address
    auth_token = get1_token()

# Get list of hosts
    get_testlist = TE_test_list(auth_token, base_url)

# Display in table
print("\n Test List from ThousandEyes Instance")
print("\n {testId:9} {testName:30} {type:10}".format(testId="   ID", testName="Name", type="Type"))
print("\n")

for TElist in get_testlist:
    #print("{testId}")
    print ("{testId:10} {testName:30} {type:10}".format(testId=TElist["testId"], 
                                              testName=TElist["testName"], 
                                              type=TElist["type"]))

print("\n")

call_TE_test()