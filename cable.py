import numpy as np
import math
from matplotlib import pyplot as plt

#resolution
r = 40

h = r/2

#derivative of time
m_1 = np.eye(r**2,k=1)
m_2 = np.eye(r**2,k=-1)

for i in range(r-1):
    m_1[(i+1)*r-1][(i+1)*r] = 0
    m_2[(i+1)*r][(i+1)*r-1] = 0

m = m_1 - m_2

#2nd order derivative of distance
n_1 = np.eye(r**2)
n_2 = np.eye(r**2,k=r)
n_3 = np.eye(r**2,k=-r)

n = 2*n_1 - n_2 - n_3

#cable equation
a = np.eye(r**2) + (float(r))*m - (float(r)**2)*n

#input
c = np.zeros(r**2)
c[:r] = [0,0,0,0,0,0,0,0,0,0.9,
          0,0,0,0,0,0,0,0,0,0.9,
          0,0,0,0,0,0,0,0,0,0.9,
          0,0,0,0,0,0,0,0,0,0]
#c[:r] = np.ones(r)
b = - (r**2)*c

#solution
x = np.linalg.solve(a,b)

#output
#print c[:r]

#for i in range(r):
#    print x[i*r:i*r+r]
plt.plot(c[:r])
for i in range(r):
    if i%8 == 0: 
        plt.plot(x[i*r:i*r+r])

plt.show()
