#!/usr/bin/env python3

import sys

input_file = sys.argv[1]
print("Output: {}".format(sys.argv[1]))
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()
