import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#SERIES
>>> s=pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
'''
0                7
1       Heisenberg
2             3.14
3      -1789710578
4    Happy Eating!
dtype: object
'''

>>> s.dtypes  #dtype('O')
>>> type(s)   #<class 'pandas.core.series.Series'>
>>> s.columns #AttributeError: 'Series' object has no attribute 'columns'
>>> s.values  #array([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'], dtype=object)

>>> s.index=['A','B','C','D','E']
>>> s
'''
A                7
B       Heisenberg
C             3.14
D      -1789710578
E    Happy Eating!
dtype: object
'''

>>> s['A'] # 7

>>> d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,'Austin': 450, 'Boston': 508}
>>> d    #{'Austin': 450, 'Portland': 900, 'San Francisco': 1100, 'Chicago': 1000, 'New York': 1300, 'Boston': 508}

>>> cities=pd.Series(d)
>>> cities
'''
Austin            450
Boston            508
Chicago          1000
New York         1300
Portland          900
San Francisco    1100
dtype: int64
'''

>>> cities['Austin']  #450

>>> cities[cities<1000]
'''
Austin      450
Boston      508
Portland    900
dtype: int64
'''
>>> less1000 = cities < 1000
>>> less1000
'''
Austin            True
Boston            True
Chicago          False
New York         False
Portland          True
San Francisco    False
dtype: bool
'''
>>> cities[less1000]
'''
Austin      450
Boston      508
Portland    900
dtype: int64
'''
>>> cities[cities<500]
'''
Austin    450
dtype: int64
'''
>>> cities[cities<500] = 599
>>> cities
'''
Austin            599
Boston            508
Chicago          1000
New York         1300
Portland          900
San Francisco    1100
dtype: int64
'''

>>> 'Austin' in cities    #True
>>> 508 in cities          #False

>>> cities/2
'''
Austin           299.5
Boston           254.0
Chicago          500.0
New York         650.0
Portland         450.0
San Francisco    550.0
dtype: float64
'''

>>> np.square(cities)
'''
Austin            358801
Boston            258064
Chicago          1000000
New York         1690000
Portland          810000
San Francisco    1210000
dtype: int64
'''

>>> cities.isnull()
'''
Austin           False
Boston           False
Chicago          False
New York         False
Portland         False
San Francisco    False
dtype: bool
'''

>>> cities>500
'''
Austin           True
Boston           True
Chicago          True
New York         True
Portland         True
San Francisco    True
dtype: bool
'''

#DATAFRAME
>>> data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
>>> data
'''
{'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'], 'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012], 'wins': [11, 8, 10, 15, 11, 6, 10, 4], 'losses': [5, 8, 6, 1, 5, 10, 6, 12]}'''

>>> football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
>>> football
'''
   year     team  wins  losses
0  2010    Bears    11       5
1  2011    Bears     8       8
2  2012    Bears    10       6
3  2011  Packers    15       1
4  2012  Packers    11       5
5  2010    Lions     6      10
6  2011    Lions    10       6
7  2012    Lions     4      12
'''

>>> football['year']
'''
0    2010
1    2011
2    2012
3    2011
4    2012
5    2010
6    2011
7    2012
Name: year, dtype: int64
'''

>>> football[football['year']>2011]
'''
   year     team  wins  losses
2  2012    Bears    10       6
4  2012  Packers    11       5
7  2012    Lions     4      12
'''


>>> football[football['wins']>=10]
'''
   year     team  wins  losses
0  2010    Bears    11       5
2  2012    Bears    10       6
3  2011  Packers    15       1
4  2012  Packers    11       5
6  2011    Lions    10       6
'''

>>> football
'''
   year     team  wins  losses
0  2010    Bears    11       5
1  2011    Bears     8       8
2  2012    Bears    10       6
3  2011  Packers    15       1
4  2012  Packers    11       5
5  2010    Lions     6      10
6  2011    Lions    10       6
7  2012    Lions     4      12
'''

>>> football[football['year']<2012]
'''
   year     team  wins  losses
0  2010    Bears    11       5
1  2011    Bears     8       8
3  2011  Packers    15       1
5  2010    Lions     6      10
6  2011    Lions    10       6
'''

>>> football[(football['year']<2012) & (football['wins']>10)]
'''
   year     team  wins  losses
0  2010    Bears    11       5
3  2011  Packers    15       1
'''

>>> football[football['year']<2012]
'''
   year     team  wins  losses
0  2010    Bears    11       5
1  2011    Bears     8       8
3  2011  Packers    15       1
5  2010    Lions     6      10
6  2011    Lions    10       6
'''

>>> football[football['year']<2012].plot()
>>> plt.show()

>>> football[football['year']<2012].plot(kind='line')
>>> plt.show()

>>> x=football[football['year']<2012]['team']
>>> x
'''
0      Bears
1      Bears
3    Packers
5      Lions
6      Lions
Name: team, dtype: object
'''
>>> list(x)
'''
['Bears', 'Bears', 'Packers', 'Lions', 'Lions']
'''

>>> x=football[football['year']<2012]['wins']
>>> x
'''
0    11
1     8
3    15
5     6
6    10
Name: wins, dtype: int64
'''

>>> x=football[football['year']<2012]
>>> x
'''
   year     team  wins  losses
0  2010    Bears    11       5
1  2011    Bears     8       8
3  2011  Packers    15       1
5  2010    Lions     6      10
6  2011    Lions    10       6
'''

>>> x=football[football['year']<2012]['losses']
>>> x
'''
0     5
1     8
3     1
5    10
6     6
Name: losses, dtype: int64
'''

>>> x=football[['losses','wins']]
>>> x
'''
   losses  wins
0       5    11
1       8     8
2       6    10
3       1    15
4       5    11
5      10     6
6       6    10
7      12     4
'''

>>> x=football[football['year']<2012][['losses','wins']]
>>> x
'''
   losses  wins
0       5    11
1       8     8
3       1    15
5      10     6
6       6    10
'''

>>> x=football[football['year']<2012][['losses','wins']].plot()
>>> plt.show()

>>> x=football[football['year']<2012][['losses','wins','team']].plot(kind='bar')
>>> plt.show()

>>> x=football[football['year']<2012][['losses','wins','team']].plot(kind='bar')
>>> plt.title("Team Win vs Losses before 2012")
>>> plt.xlabel("No of Teams")
>>> plt.ylabel("No of Games")
>>> plt.show()

>>> x=football[football['year']<2012][['losses','wins']]
>>> x
'''
   losses  wins
0       5    11
1       8     8
3       1    15
5      10     6
6       6    10
'''

>>> football[football['year']<2012][['losses','wins']]
'''
   losses  wins
0       5    11
1       8     8
3       1    15
5      10     6
6       6    10
'''

>>> football[football['year']<2012][['losses','wins','team']]
'''   
   losses  wins     team
0       5    11    Bears
1       8     8    Bears
3       1    15  Packers
5      10     6    Lions
6       6    10    Lions
'''

>>> football[football['year']<2012][['losses','wins','team']].set_index('team')
'''
         losses  wins
team                 
Bears         5    11
Bears         8     8
Packers       1    15
Lions        10     6
Lions         6    10
'''

>>> game = football[football['year']<2012][['losses','wins','team']].set_index('team')
>>> game
'''
         losses  wins
team                 
Bears         5    11
Bears         8     8
Packers       1    15
Lions        10     6
Lions         6    10
'''

>>> game.plot(kind='bar')
>>> game
'''     
	 losses  wins
team                 
Bears         5    11
Bears         8     8
Packers       1    15
Lions        10     6
Lions         6    10
'''
>>> game = football[football['year']<2012][['losses','wins','team']].set_index('team').plot(kind='bar')
>>> plt.show()

'''
EarthQuake Data:
Columns: Date,Time,Latitude,Longitude,Magnitude,Epicentre
'''

>>> data = pd.read_csv('earthquake.csv')
>>> data  # get rows from DataFrame: data
>>> data.describe()
#some filtering of Data
>>> reader = data[data['Magnitude']>=4.5 ]

>>> reader = data[data.Epicentre.isin(['Sindhupalchowk','Nuwakot','Gorkha']) & (data.Magnitude>5.0)]

>>> reader = data[data.Epicentre.isin(['Sindhupalchowk','Nuwakot','Gorkha']) ]#Dolakha

>>> reader = data[data.Epicentre.str.contains(r'Dol')]#Dolakha

>>> reader = data[data.Date.str.contains(r'/04/')] #April

>>> reader = data[data.Date.between('2015/04/25','2015/04/31') & data.Epicentre.str.contains(r'Sindhu')]

>>> reader = data[data.Date.str.contains(r'/04/') & data.Epicentre.str.contains(r'Sindhu')]
print(reader)