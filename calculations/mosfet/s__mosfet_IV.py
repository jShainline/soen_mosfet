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
# file_name = 'nmos_IV_sweep__Vt_0.70V__Nd_3e16.raw' #
# file_name = 'nmos_IV_sweep__Vt_0.86V__Nd_5e16.raw' #
file_name = 'nmos_IV_sweep__Vt_0.86V__Nd_5e16__Vg_1-3V__Vs_3V__W_1um__L_1um.raw' #
variables = ['V(ds)','V(vg)','Id(M2)']
data_dict, LTobj = read_lt_data(file_name,variables)

#%% for a given Vds, Vg and desired Ids, find required W/L

Vds_vec = np.asarray([2,2.5,3]) # V
Ids_vec = np.asarray([10,15,20])*1e-6 # A

# make cleaner Vg vec
num_vg = len(data_dict['V(vg)'])
Vg_vec = np.zeros([num_vg])
for ii in range(num_vg):
    Vg_vec[ii] = data_dict['V(vg)'][ii][0]

w_array = np.zeros([len(Vds_vec),len(Ids_vec),len(Vg_vec)])
for ii in range(len(Vg_vec)):
    for jj in range(len(Vds_vec)):
        _ind_Vds = ( np.abs( data_dict['V(ds)'][ii] - Vds_vec[jj] ) ).argmin()
        for kk in range(len(Ids_vec)):
            Ids_0 = data_dict['Id(M2)'][ii][_ind_Vds]            
            w_array[jj,kk,ii] = Ids_vec[kk]/Ids_0
            
#%% IVs
    
fig, ax = plt.subplots(nrows = 1, ncols = 1, sharex = False, sharey = False)
# plt.title(file_name, loc = 'center', y = 1.0)   
fig.suptitle(file_name)
    
color_list = ['blue1','blue2','blue3','blue4','blue5','green5','green4','green3','green2']
for ii in range(len(data_dict['V(ds)'])):
    ax.plot(data_dict['V(ds)'][num_vg-ii-1], 1e6*data_dict['Id(M2)'][num_vg-ii-1], '-', color = colors[color_list[num_vg-ii-1]], label = 'Vg = {:4.2f}V'.format(data_dict['V(vg)'][num_vg-ii-1][0]))
ax.set_xlabel(r'$V_{ds}$ [V]')
ax.set_ylabel(r'$I_{ds}$ [$\mu$A]')
ax.legend(loc = 'upper left')
ax.grid(which = 'major', linewidth = 0.25)

# plt.show()

#%% plot
fig, axs = plt.subplots(nrows = 2, ncols = 1, sharex = False, sharey = False)
# plt.title(file_name, loc = 'center', y = 1.0)   
fig.suptitle(file_name)
    
color_list = [['blue5','blue3','blue1'],
              ['green5','green3','green1'],
              ['yellow5','yellow3','yellow1']]
for ii in range(len(Ids_vec)):
    for jj in range(len(Vds_vec)):
        axs[0].plot(Vg_vec, w_array[jj,ii,:], '-', color = colors[color_list[ii][jj]], label = 'Vds = {:4.2f}V; Ids = {:4.2f}uA'.format(Vds_vec[jj],1e6*Ids_vec[ii]))
        axs[1].plot(Vg_vec, w_array[jj,ii,:], '-', color = colors[color_list[ii][jj]], label = 'Vds = {:4.2f}V; Ids = {:4.2f}uA'.format(Vds_vec[jj],1e6*Ids_vec[ii]))
axs[0].set_xlabel(r'$V_{gs}$ [V]')
axs[0].set_ylabel(r'W/L')
axs[0].set_xlim([1,3.0])
axs[0].set_ylim([0,30])
axs[0].legend()
axs[0].grid(which = 'major', linewidth = 0.25)

axs[1].set_xlabel(r'$V_{gs}$ [V]')
axs[1].set_ylabel(r'W/L')
axs[1].set_xlim([2,3])
axs[1].set_ylim([0,4])
axs[1].legend()
axs[1].grid(which = 'major', linewidth = 0.25)

plt.show()

#%% resistance
    
# color_list = ['blue2','blue3','blue4','blue5',
#               'green2','green3','green4','green5',
#               'yellow2','yellow3','yellow4','yellow5',
#               'red2','red3','red4','red5']
# fig = plt.figure()
# fig.suptitle(file_name)    
# ax = fig.gca()
# for ii in range(LTobj.case_count):
#     ax.plot(data_dict['V(ds)'][ii],np.asarray(data_dict['V(ds)'][ii])/np.asarray(data_dict['Id(M2)'][ii]), '-', color = colors[color_list[ii]], label = 'Vg = {:4.2f}V'.format(data_dict['V(vg)'][ii][0]))

# ax.set_xlabel(r'$V_{ds}$ [V]')   
# ax.set_ylabel(r'$R_{ds}$ [$\Omega$]')   
# ax.legend(loc = 'upper right')
# ax.grid(which = 'major', linewidth = 0.25)

# plt.show()



