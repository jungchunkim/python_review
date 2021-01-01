#!/usr/bin/env/python

import sys

print("Output: Baby_Shark.txt")
input_file=sys.argv[1]   #0번은 파일 자체를 표현
filereader=open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()
