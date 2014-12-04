#analytical solution to cable equation
from matplotlib import pyplot as plt
import numpy as np



x = np.arange(0,2,0.02)
for a in range(5):
    y = (1/np.sqrt(x))*np.exp(-0.04*(a*a)/x)*np.exp(-x)
    plt.plot(x,y)
plt.show()
