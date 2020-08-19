#!/usr/bin/env python3

"""
checks-runner runs funds-checker.py and log-checker.py on a regular interval.
"""

import os, sys, time
# from datetime import timedelta

# The interval at which the scripts are run, in hours.
DEFAULT_RUN_INTERVAL = 8

hours = DEFAULT_RUN_INTERVAL
if len(sys.argv) > 2:
    hours = sys.argv[2]

while True:
    os.popen('/home/gollum/funds-checker.py /home/gollum/.env')
    os.popen("/home/gollum/log-checker.py /home/gollum/.env sia {}".format(hours))
    time.sleep(hours * 3600)

