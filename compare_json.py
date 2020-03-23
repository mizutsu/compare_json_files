#!/usr/bin/env python
# coding: utf-8

import sys
import json


def main(filepath):
    fp = open(filepath, 'r')
    json_data = json.load(fp)

    return json_data["data"]


args = sys.argv
data_details_1 = main(args[1])
data_details_2 = main(args[2])

if len(data_details_1) != len(data_details_2):
    exit(1)


for i, value in enumerate(data_details_1):
    if value == data_details_2[i]:
        continue

    print(value)
    print(data_details_2[i])
    print('')

