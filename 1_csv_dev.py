import sys
import csv


input_file = sys.argv[1] 
output_file = sys.argv[2] 


with open(input_file, 'r', newline='') as csv_in_file: #파일을 close를 안해줘도 자동으로 닫아준다
    with open(output_file, 'w', newline = '') as csv_out_file:
            filereader = csv.reader(csv_in_file, delimiter = ',')
            filewriter = csv.writer(csv_out_file, delimiter = ',')
            for row_list in filereader:
                filewriter.writerow(row_list)
        
