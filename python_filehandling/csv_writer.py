import csv
import sys
import os

filename="newCSV.csv"
with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(('Header 1', 'Header 2', 'Header 3', 'Header 4')) #Header
    for i in range(3):
        row = (
            i + 1,
            "Data "+str(i),
            "DataRow "+str(i),
            "DataRow Again "+str(i)
        )
        writer.writerow(row)

print(open(os.path.dirname(os.path.abspath(__file__))+'/'+filename, 'r').read())