# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:30:01 2021

@author: frank
Test batch running for LSFB input file generation and then WRAP batch processing run using SIM/TAB
Then pulling all WAM results into single excel file to summarize. 
Running through Spyder (py 3.8)
"""

import glob
import pandas as pd
from pandas import ExcelWriter #just for ExcelWriter!
import shutil


#pulling all LIN files in current folder, putting into list, removing .lin extensions
LINlist=[]
LINfinal=[]
for file in glob.glob("*.lin"):
    LINlist.append(file)
    
#LINlist

for item in LINlist:
    item=item.replace('.LIN','')
    LINfinal.append(item)

#LINfinal
    
#writing list of LIN files to txt file which will be read by LSFB batch file
LINfilelist=open('LSFBFileList.txt','w')
for item in LINfinal:
    LINfilelist.write(item)
    LINfilelist.write('\n')
LINfilelist.close()

##Run batch file for LSFB exe to prepare all input data files for WRAP run
from subprocess import Popen
p = Popen("LSFB.bat")
stdout, stderr = p.communicate()

print('Finish processing input files using LSFB executable')

##copy and rename original .dat and .dis files for each drought sequence scenario
for item in LINfinal:
    shutil.copy("C3.dat",item+".dat")
    shutil.copy("C3.dis",item+".dis")

#writing list of dat files to txt file which will be read by WRAP batch file
SimTabfilelist=open('SimTabFileList.txt','w')
for item in LINfinal:
    SimTabfilelist.write(item)
    SimTabfilelist.write('\n')
SimTabfilelist.close()

##Run batch Sim and Tab executables
from subprocess import Popen
p = Popen("SimTab.bat")
stdout, stderr = p.communicate()

print('Finish WRAP Sim and Tab executables')

##pull all FY output files names and put into list
YROint=[]
YRO=[]
for file in glob.glob("*.yro"):
    YROint.append(file)
for item in YROint:
    item=item.replace('.YRO','')
    YRO.append(item)

#format and write YRO output files to combined xlsx spreadsheet, each on separate tabs
FYfinal=pd.DataFrame(columns=['Iteration','Level','Annual Target','Mean Shortage','Mean Actual',\
                            'Volume Reliability (%)','Periods Without Shortage','Period Reliability (%)'])
#print(FYfinal)
writer=
('YRO_Output_Combined.xlsx')
with ExcelWriter('YRO_Output_Combined.xlsx', engine='xlsxwriter') as writer:
    for item in YRO:
        FY=pd.read_csv(item+'.YRO',sep='\s+', engine='python', header=None,skiprows=(17))
        FY.columns = ['Iteration','Level','Annual Target (AFY)','Mean Shortage (AFY)','Mean Actual Diversion (AFY)',\
                            'Volume Reliability (%)','Periods Without Shortage (# months)','Period Reliability (%)']
        FY=FY[FY.Iteration != '---'] # removing rows with '---'
        FY=FY[FY.Iteration != 'Routine'] # removing rows with '---'
        FY=FY[:-1] # removing last row which is '------...'
        FY=FY.astype('float64') ##formatting column types
        FY.to_excel(writer,item,index=False)
        FYfinal=FY.loc[:]

## Want to create another tab which is the last row of each of the YRO tables. This would be a summary tab showing final FYs for each scenario.
    
    
    
    
    
    
    
    
    