import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

ts = pd.read_excel('datasets/imiona.xlsx')
print(ts)
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()