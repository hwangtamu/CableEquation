__author__ = 'Han Wang'

import numpy as np
import matplotlib.pyplot as plt


class R:
    current = np.array([])
    voltage = np.array([])
    clock = 0

    def __init__(self, r, t):
        self.resistance = r
        self.clock = t

    def add_voltage(self, volt):
        self.voltage = volt
        self.current = volt/self.resistance


class R_cyto:
    current = np.array([])
    voltage = np.array([])
    rear_voltage = np.array([])
    clock = 0

    def __init__(self, r, t):
        self.resistor = R(r, t)
        self.clock = t

    def add_vc(self, volt, curr=0):
        self.current = curr
        self.voltage = volt
        self.rear_voltage = volt - curr*self.resistor.resistance


class C:
    current = np.array([])
    voltage = np.array([])
    clock = 0

    def __init__(self, c, t):
        self.capacitance = c
        self.clock = t

    def add_voltage(self, volt):
        self.voltage = volt
        whole_volt = np.append([0], volt)
        self.current = ([self.capacitance*(self.voltage[x]-whole_volt[x])/self.clock for x in range(len(self.voltage))])


class RC:
    current = np.array([])
    voltage = np.array([])
    clock = 0

    def __init__(self, r, c, t):
        self.resistance = r
        self.capacitance = c
        self.clock = t
        self.resistor = R(r, r)
        self.capacitor = C(c, t)

    def add_voltage(self, volt):
        self.voltage = volt
        self.resistor.add_voltage(volt)
        self.capacitor.add_voltage(volt)
        self.current = self.resistor.current + self.capacitor.current


class Unit:
    current_in = np.array([])
    current_out = np.array([])
    voltage_in = np.array([])
    voltage_out = np.array([])
    clock = 0

    def __init__(self, r_c, r, c, t):
        self.r_cyto = R_cyto(r_c, t)
        self.rc = RC(r, c, t)
        self.clock = t

    def add_vc(self, volt, curr):
        self.voltage_in = volt
        self.current_in = curr
        self.rc.add_voltage(volt)
        self.r_cyto.add_vc(volt, curr - self.rc.current)
        self.current_out = self.r_cyto.current
        self.voltage_out = self.r_cyto.rear_voltage


class Injection:
    n = 0

    def __init__(self, synapses):

# operation

a = 3
#current, alpha function, single spike
def alpha(t, a):
    return a*a*t*np.exp(-a*t)


#complex spikes
def rep_alpha(t, a, n):
    c = np.zeros(len(t))
    if n>0:
        for i in range(n):
            c += np.piecewise(t, [t <= i, t > i],[0,lambda t:alpha(t-i,a)])
        return c

time = np.arange(0, 5, 0.02)
y = rep_alpha(time, 3, 3)
r_1 = R(0.2, 0.02)
r_2 = R_cyto(0.05, 0.02)
r_3 = R_cyto(0.05, 0.02)
r_4 = R_cyto(0.05, 0.02)

rc_1 = RC(1, 0.1, 0.02)
rc_2 = RC(1, 0.1, 0.02)
rc_3 = RC(1, 0.1, 0.02)
rc_4 = RC(1, 0.1, 0.02)

cyto = [r_2, r_3, r_4]
membrane = [rc_1, rc_2, rc_3, rc_4]

r_1.add_voltage(y)
rc_1.add_voltage(y)
r_2.add_vc(y, r_1.current-rc_1.current)
rc_2.add_voltage(r_2.rear_voltage)
r_3.add_vc(y, r_2.current-rc_2.current)
rc_3.add_voltage(r_3.rear_voltage)
r_4.add_vc(y, r_3.current-rc_3.current)
rc_4.add_voltage(r_4.rear_voltage)

plt.plot(time, rc_1.voltage)
plt.plot(time, rc_2.voltage)
plt.plot(time, rc_3.voltage)
plt.plot(time, rc_4.voltage)
plt.show()
