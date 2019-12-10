#!/usr/bin/env python3
#
#
#
#

import json
import sys

if (len(sys.argv) < 2):
    print('Usage: ', sys.argv[0], "file.json [skip|pass|fail]\n")
    print('List the output and result of all skipped/passed/failed tests')
    exit(1)

if (len(sys.argv) >= 3):
    match = sys.argv[2]
else:
    match = "skip"

#print(sys.argv[1])

with open(sys.argv[1]) as json_data:
    data = json.load(json_data)

for test_name in data['tests']:
    if (match == data['tests'][test_name]['result']):
        print("Test: ", test_name)
        print(data['tests'][test_name]['result'])
        print(data['tests'][test_name]['out'])

