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
file_name = 'mosfet_led__W20um.raw' #
variables = ['V(ds)','V(led)','I(D1)','V(vg)']
data_dict, LTobj = read_lt_data(file_name,variables)

#%% organize data

num_vg = len(data_dict['V(vg)'])
Vg_vec = np.zeros([num_vg])
for ii in range(num_vg):
    Vg_vec[ii] = data_dict['V(vg)'][ii][0]
    
#%% plot
fig, axs = plt.subplots(nrows = 2, ncols = 1, sharex = True, sharey = False)
fig.suptitle(file_name)    
color_list_1 = ['red1','red2','red3','red4','red5']
color_list_2 = ['blue1','blue2','blue3','blue4','blue5']
axs[0].plot(data_dict['V(ds)'][ii],data_dict['V(ds)'][ii], '-', color = colors['yellow3'], label = '$V_{ds}$')  
for ii in range(num_vg):
    axs[1].plot(data_dict['V(ds)'][ii],np.asarray(data_dict['I(D1)'][ii])*1e6, '-', color = colors[color_list_1[ii]], label = '$V_g$ = {:4.2f}V'.format(Vg_vec[ii]))
    axs[0].plot(data_dict['V(ds)'][ii],data_dict['V(led)'][ii], '-', color = colors[color_list_2[ii]], label = '$V_g$ = {:4.2f}V'.format(Vg_vec[ii]))

axs[1].set_xlabel(r'$V_{ds}$ [V]')
axs[1].set_ylabel(r'$I_{led}$ [$\mu$A]')  
axs[0].set_ylabel(r'$V_{led}$ [V]')   
axs[0].legend(loc = 'upper left')
axs[1].legend(loc = 'upper left')
axs[0].grid(which = 'major', linewidth = 0.25)
axs[1].grid(which = 'major', linewidth = 0.25)



# fig = plt.figure()
# fig.suptitle(file_name)    
# ax = fig.gca()
# ax2 = ax.twinx()
# color_list_1 = ['red1','red2','red3','red4','red5']
# color_list_2 = ['blue1','blue2','blue3','blue4','blue5']
# for ii in range(num_vg):
#     ax2.plot(data_dict['V(ds)'][ii],np.asarray(data_dict['I(D1)'][ii])*1e6, '-', color = colors[color_list_1[ii]], label = '$V_g$ = {:4.2f}V'.format(Vg_vec[ii]))
#     ax.plot(data_dict['V(ds)'][ii],data_dict['V(led)'][ii], '-', color = colors[color_list_2[ii]], label = '$V_g$ = {:4.2f}V'.format(Vg_vec[ii]))
# ax.plot(data_dict['V(ds)'][ii],data_dict['V(ds)'][ii], '-', color = colors['yellow3'], label = '$V_{ds}$')  

# ax2.set_xlabel(r'$V_{ds}$ [V]')
# ax2.set_ylabel(r'$I_{led}$ [$\mu$A]', color = colors['red3'])
# ax2.tick_params(axis = 'y', labelcolor = colors['red3'])    
# ax.set_ylabel(r'$V_{led}$ [V]', color = colors['blue3'])
# ax.tick_params(axis = 'y', labelcolor = colors['blue3'])    
# ax2.legend(loc = 'upper left')
# ax.legend(loc = 'lower left')