from matplotlib import pyplot as plt
from matplotlib import cm,patches
import numpy as np
import matplotlib.animation as animation

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


t = np.arange(0.02,5,0.02)
a = 3
y = beta(t,a,0.5,3)

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(6, 6)

ax = plt.axes(xlim=(0, 7), ylim=(0, 2))

dendrite = [patches.Rectangle((0.5, 0),1,0, fc='y'),
            patches.Rectangle((1.5, 0),1,0, fc='y'),
            patches.Rectangle((2.5, 0),1,0, fc='y'),
            patches.Rectangle((3.5, 0),1,0, fc='y'),
            patches.Rectangle((4.5, 0),1,0, fc='y'),
            patches.Rectangle((5.5, 0),1,0, fc='y'),
    ]


def init():
    for p in dendrite:
        ax.add_patch(p)
    return dendrite[0],dendrite[1],dendrite[2],dendrite[3],dendrite[4],dendrite[5],



def animate(i):
    dendrite[0].set_height(beta(t,a,0  ,3)[i])
    dendrite[1].set_height(beta(t,a,0.2,3)[i])
    dendrite[2].set_height(beta(t,a,0.4,3)[i])
    dendrite[3].set_height(beta(t,a,0.6,3)[i])
    dendrite[4].set_height(beta(t,a,0.8,3)[i])
    dendrite[5].set_height(beta(t,a,1.0,3)[i])
    return dendrite[0],dendrite[1],dendrite[2],dendrite[3],dendrite[4],dendrite[5],

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=249, 
                               interval=20,
                               blit=True)

plt.show()
