import csv
import sys
import os

#writerow:
#writerows: list of rows
#writeheader: write header

filename="newCSV.csv"
with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'w+',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Header 1', 'Header 2', 'Header 3', 'Header 4']) #Header
    for i in range(3):
        print(i)
        row = [
            i + 1,
            "Data "+str(i),
            "DataRow "+str(i),
            "DataRow Again "+str(i)
        ]
        writer.writerow(row)

print(open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'r').read())

#CSV Quoting
#QUOTE_ALL: regardless of type
#QUOTE_MINIMAL: with special characters #Default
#QUOTE_NONNUMERIC: all fields that are not Integers or Floats
#QUOTE_NONE: all fields that are not Integers or Floats
#writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC) 