import csv
import os

filename = 'earthquakePast.csv'
lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

#with statement automatically closes the file again when the block end
with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename) as f:  
    reader = csv.reader(f)
    #next(reader) # Ignore the header row.    
    
    count=0
    for row in reader:
        print(row)
        # print(row[1])
#        lats.append(float(row[1]))
#        lons.append(float(row[0]))
#        magnitudes.append(float(row[4]))
#        timestrings.append(row[5])
        count+=1
        if(count==10):
            break