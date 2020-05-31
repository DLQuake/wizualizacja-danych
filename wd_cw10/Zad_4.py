import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 30, 100)
plt.ylim([-1,3])
y1 = np.sin(x)+2
y2 = np.sin(x)*-1
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='sin(x)')

plt.xlabel('x')
plt.ylabel('sin(x)')

plt.title("Wykres sin(x), sin(x)")

plt.legend(loc='center left')
plt.show()