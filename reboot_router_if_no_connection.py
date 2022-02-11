#!/usr/bin/env python
from internet import internet
from reboot_router import reboot
from config import *
import requests
import time
import sys

def reboot_router():
    client = requests.Session()
    reboot(client, ROUTER, USER, PASSWORD)

if __name__ == '__main__':
    try:
        while True: 
            print('Checking...',file=sys.stderr)
            if not internet(TEST_HOST, TEST_PORT, TEST_TIMEOUT):
                print('Internet connection is down. Rebooting router...',file=sys.stderr) 
                try:
                    reboot_router()
                except requests.HTTPError as exception:
                    print('Router down or unresponsive, trying again later...',file=sys.stderr)
            else:
                print('Internet connection is up. Will check again in ' + str(CHECK_TIMEOUT) + ' seconds...',file=sys.stderr)
            time.sleep(CHECK_TIMEOUT)               
    except KeyboardInterrupt:
        print('CTRL+C caught, exiting...',file=sys.stderr)


