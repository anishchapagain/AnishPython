#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%
'''
EarthQuake Data:
Columns: Date,Time,Latitude,Longitude,Magnitude,Epicentre
'''
#%%
data = pd.read_csv('earthquake.csv')
#%%
data  # get rows from DataFrame: data
#%%
data.describe()
#%%
#some filtering of Data
reader = data[data['Magnitude']>=4.5 ]
#%%
reader = data[data.Epicentre.isin(['Sindhupalchowk','Nuwakot','Gorkha']) & (data.Magnitude>5.0)]
#%%
reader = data[data.Epicentre.isin(['Sindhupalchowk','Nuwakot','Gorkha']) ]#Dolakha
#%%
reader = data[data.Epicentre.str.contains(r'Dol')]#Dolakha
#%%
reader = data[data.Date.str.contains(r'/04/')] #April
#%%
reader = data[data.Date.between('2015/04/25','2015/04/31') & data.Epicentre.str.contains(r'Sindhu')]
#%%
reader = data[data.Date.str.contains(r'/04/') & data.Epicentre.str.contains(r'Sindhu')]
#%%
print(reader)