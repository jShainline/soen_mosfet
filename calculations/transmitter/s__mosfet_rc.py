#%%
import numpy as np
from matplotlib import pyplot as plt

from _functions import read_lt_data
from _util import physical_constants, color_dictionary

p = physical_constants()
colors = color_dictionary()

plt.close('all')

#%% read lt data
directory = ''          
file_name = 'mosfet_rc__W10um_R100k.raw' #
variables = ['V(rc)']
#not sure how to extract cap from .step param
dC = 0.1 # pF
cap_vec = np.arange(0.1,1+dC,dC)
data_dict, LTobj = read_lt_data(file_name,variables)

#%% plot

fig = plt.figure()
fig.suptitle(file_name)    
ax = fig.gca()
color_list = ['red1','red2','red3','red4','red5','blue5','blue4','blue3','blue2','blue1']
for ii in range(LTobj.case_count):
    ax.plot(1e9*np.asarray(data_dict['time'][ii]),data_dict['V(rc)'][ii], '-', color = colors[color_list[ii]], label = '$C$ = {:3.1f}pF'.format(cap_vec[ii]))

ax.set_xlabel(r'Time [ns]')   
ax.set_ylabel(r'$V_{rc}$ [V]')   
ax.legend(loc = 'upper right')
ax.grid(which = 'major', linewidth = 0.25)

plt.show()

