#!/usr/bin/env python3
import sys
import glob
import os 

# Read multiple text files
inputPath = sys.argv[1]
output_file = sys.argv[2]

for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
    print(os.path.basename(input_file))
    print("-------------------------------")
    with open(input_file, 'r', newline='') as filereader:
        with open(output_file, 'a', newline='') as filewriter:
            for row in filereader:
                filewriter.write(row)
               
