import pandas as pd
from matplolib import pyplot

data = [20,45,65,72,67,89,76,43,23,99,100]
s=pd.series(data,index=range(len(data)))
s.plot()