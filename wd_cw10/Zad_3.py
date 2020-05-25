import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 30, 100)
plt.ylim([-1,1])
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='cos(x)')

plt.xlabel('x')
plt.ylabel('sin(x) cos(x)')

plt.title("Wykres sin(x) cos(x)")

plt.legend()
plt.show()