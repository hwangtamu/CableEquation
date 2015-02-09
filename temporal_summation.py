from matplotlib import pyplot as plt
import numpy as np

#current, alpha function, single spike
def alpha(t,a):
    return a*a*t*np.exp(-a*t)

#complex spikes
def rep_alpha(t,a,n):
    c = np.zeros(len(t))
    if n>0:
        for i in range(n):
            c += np.piecewise(t,[t<=i,t>i],[0,lambda t:alpha(t-i,a)])
        return c





#differentiate potential, c:current
def delta(m,t,x,n):
    return np.piecewise(t,[t<=m,t>m],[0,lambda t:0.01*rep_alpha(t,a,n)*np.exp(-(t-m)-0.25*x*x/(t-m))/np.sqrt(t-m)])


#potential
def beta(t,a,x,n):
    v = np.zeros(len(t))
    for m in t:
        v += delta(m,t,x,n)
    return v
'''
#old version model
def theta(t,a):
    return a*a*t*np.exp(-a*t)/(1-a)-a*a*np.exp(-a*t)/((1-a)*(1-a))+a*a*np.exp(-t)/((1-a)*(1-a))
'''    

t = np.arange(0.02,5,0.02)

a = 3
y = rep_alpha(t,a,3)

plt.plot(t,y,label="alpha")

y_1 = beta(t,a,0,3)
plt.plot(t,y_1,label="x=0")

y_2 = beta(t,a,0.5,3)
plt.plot(t,y_2,label="x=0.5")


plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.show()
