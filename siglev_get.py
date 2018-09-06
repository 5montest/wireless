#!/usr/bin/env python
# -*-coding: utf-8 -*-

import subprocess
import re
import time

pattern = r"(?<=level=)(.*)(?= dBm)"
cmd = "iwconfig <your wireless interface name>"

def main():
    while True:
        result = subprocess.check_output(cmd.split())
        match = re.search(pattern,result)
        if match:
            dbm = match.group()
            dbm = int(dbm)
            print dbm
            time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\nEND"
