#!/usr/bin/env python3
#여러개의 파일을 통합작업하기 : sales_달_2019.csv 세개
#전체 파일 개수 및 각 파일의 행, 열의 숫자를 출력한다.

import csv
import glob
import os
import sys

#csv 파일들이 있는 폴더의 경로를 지정한다. 
input_path = sys.argv[1]
#경로 입력할 때 양쪽에 쌍따옴표 넣기!

file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 1
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)
		for row in filereader:
			row_counter += 1
	print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
	os.path.basename(input_file), row_counter, len(header)))
	file_counter += 1
print("---------------------------------------------")
print('Number of files: {0:d}'.format(file_counter))
