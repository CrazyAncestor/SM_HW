import numpy as np
import matplotlib.pyplot as plt
hbar = 6.63e-34/2/np.pi
me = 9.11e-31
eV = 1.6e-19
a = 20* 1e-10
g = 0.1* eV * a

def find_delta(s):
    a = hbar**2 * s
    b = me * g
    return np.arctan(-(b/a))

def s(E):
    return (2*me*E/hbar**2)**0.5

def ka(E):
    s0 = s(E)
    delta = find_delta(s0)
    t = np.cos(delta)
    ka0 = np.arccos(np.cos(s0*a+delta)/t)

    return ka0

def ka_free(E):
    s0 = s(E)
    t = 1
    ka0 = np.arccos(np.cos(s0*a)/t)

    return ka0

E = eV*np.linspace(0,0.9,10000)
kas = []
ka_frees = []
for i in range(len(E)):
    kas.append(ka(E[i]))
    ka_frees.append(ka_free(E[i]))
kas = np.array(kas)
ka_frees = np.array(ka_frees)
plt.plot(kas/np.pi,E/eV,label=r'g=0.1eV $\times$ a')
plt.plot(ka_frees/np.pi,E/eV,label='g=0, free electron')
plt.xlabel(r'ka($\pi$)')
plt.ylabel('Energy(eV)')
plt.legend()
plt.show()