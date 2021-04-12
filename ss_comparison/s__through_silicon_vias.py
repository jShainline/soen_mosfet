import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec

from _util import physical_constants, color_dictionary
colors = color_dictionary()

p = physical_constants()

#%%

N_ph = 10
lam = 1.5e-6
V = 0.8
eta_nu = 1e-3

nu = p['c']/lam

C = 2*N_ph*p['h']*nu/(V**2*eta_nu)

print('\nC = {:5.2f}fF with N_ph = {:d}, lam = {:5.2f}um, V = {:5.2f}V, and eta_nu = {:5.2e}'.format(C*1e15,N_ph,lam*1e6,V,eta_nu))
