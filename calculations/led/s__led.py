#%%
import numpy as np
from matplotlib import pyplot as plt

from _functions import read_lt_data
from _util import physical_constants, color_dictionary

p = physical_constants()
colors = color_dictionary()

plt.close('all')

#%%

N_ph = 1e3
eta = 1e-4
I_led = 15e-6 # amps

t_on = p['e']*N_ph/(eta*I_led) # s

print('t_on = {:4.2f}ns'.format(t_on*1e9))