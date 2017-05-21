import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = [20,45,65,72,67,89,76,43,23,99,100]
s=pd.Series(data,index=range(len(data)))
s.plot(kind="line")
plt.show()