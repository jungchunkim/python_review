#!/usr/bin/env python3

import sys
import glob
import os 

# Write to a text file
my_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output : Output written to file")
