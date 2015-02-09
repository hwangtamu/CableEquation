from matplotlib import pyplot as plt
import numpy as np

#current, alpha function
def alpha(t,a):
    return a*a*t*np.exp(-a*t)

#differentiate potential, c:current
def delta(m,t,x):
    return np.piecewise(t,[t<=m,t>m],[0,lambda t:0.01*alpha(m,a)*np.exp(-(t-m)-0.25*x*x/(t-m))/np.sqrt(t-m)])


#potential
def beta(t,a,x):
    v = np.zeros(len(t))
    for m in t:
        v += delta(m,t,x)
    return v

def theta(t,a):
    return a*a*t*np.exp(-a*t)/(1-a)-a*a*np.exp(-a*t)/((1-a)*(1-a))+a*a*np.exp(-t)/((1-a)*(1-a))
    

t = np.arange(0.02,5,0.02)

a = 3
y = alpha(t,a)

plt.plot(t,y,label="alpha")

y = beta(t,a,0)
plt.plot(t,y,label="x=0")

y = beta(t,a,0.5)
plt.plot(t,y,label="x=0.5")

plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.show()
