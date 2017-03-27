import csv
import os

# filename = 'earthquakePast.csv'
filename = 'earthquakePast_check.csv'

lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

l=[]
#with statement automatically closes the file again when the block end
#next(reader) # Move to next Row, Ignore the header in this case.
with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename) as f:  
    reader = csv.reader(f)                  #reader = csv.reader(f, delimiter=' ') #earthquakePast_check
    
    #1.
    count=0
    for row in reader:
        print(reader.line_num," >> ",row)
        l.append(reader.line_num)
         # print(row[1])
 #        lats.append(float(row[1]))
 #        lons.append(float(row[0]))
        count+=1
        if(count==10):
            break

    #2.        
    # for x in range(0,9):
        # print(next(reader))
    
    print("There are Total : ",len(l)," Rows")