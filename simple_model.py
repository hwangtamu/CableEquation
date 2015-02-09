from matplotlib import pyplot as plt
import numpy as np

#current
def alpha(t,a):
    return a*a*t*np.exp(-a*t)

#potential
def beta(t,a):
    return a*a*t*np.exp(-a*t)/(1-a)-a*a*np.exp(-a*t)/((1-a)*(1-a))+a*a*np.exp(-t)/((1-a)*(1-a))


    

t = np.arange(0,5,0.02)
a = 3
y = alpha(t,a)

plt.plot(t,y)

y = beta(t,a)

plt.plot(t,y)


plt.show()
