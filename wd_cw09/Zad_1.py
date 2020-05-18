import pandas as pd
import matplotlib.pyplot as plt

ts = pd.read_excel('datasets/imiona.xlsx')

ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()