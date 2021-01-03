#! /usr/bin/env python3

import sys

input_file = "Baby_Shark.txt"
print("Output: Baby_Shark.txt")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))
