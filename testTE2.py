__author__ = "Glenn Rowe"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022"
__license__ = "Cisco Sample Code License, Version 1.1"

import requests
import json
from configparser import ConfigParser


def main():
    global token, base_url
    te_api_config = ConfigParser()
    te_api_config.read("TE_Config.ini")
    token = te_api_config['TE']['token']
    base_url = te_api_config['TE']['base_url']
    test_1234()

def testlistresp():
    return base_url+'/tests.json'

def test_1234():
    hdr = {"Authorization": token, "Content-Type": "application/json", "Accept": "application/json"}
    print(hdr)
    resp = requests.get(url=base_url+'/tests.json', headers=hdr)
    print(json.dumps(testlistresp))

'''    for testlist in resp['resp']:
        print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
            format(device['hostname'],
                    device['managementIpAddress'],
                    serialNumber,
                    platformId,
                    device['softwareVersion'],
                    device['role'],uptime))
'''

if __name__ == '__main__':
    main()