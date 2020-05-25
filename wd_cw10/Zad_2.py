import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.ylim([0,1])
y = 1/x
plt.plot(x,y,label='f(x)=1/x',color='green', linestyle='dotted',marker='>')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.title("Wykres funkcji f(x)=1/x dla x [1,20]")

plt.legend()
plt.show()