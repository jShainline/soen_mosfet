from pylab import *
import numpy as np

from _util import physical_constants, color_dictionary
p = physical_constants()
colors = color_dictionary()

plt.close('all')

#%%
#--- inputs ---#
r_300 = 0.15#radius of 300-mm wafer
w_wew = 1e-5#pitch of wafer-edge waveguides
w_spd = 2.5e-5#pitch of single-photon detectors in 1D
r_f125 = 125e-6/2#radius of bare fiber
r_f250 = 250e-6/2#radius of acrylic-clad fiber

#%%
#--- calculated quantities ---#
h_8 = 2*r_300*np.sin(np.pi/8)
d_8 = 2*r_300*np.sqrt(1-np.sin(np.pi/8)**2)
A_8 = 2*np.sqrt(2)*r_300**2
A_4 = h_8**2
A_spd = w_spd**2
N_spd = A_8/A_spd
A_f125 = (3*np.sqrt(3)/2)*r_f125**2#for hexagonal packing
A_f250 = (3*np.sqrt(3)/2)*r_f250**2#for hexagonal packing
N_f125 = A_4/A_f125
N_f250 = A_4/A_f250

#%%
#--- output info ---#
print('N_wew = ',h_8/w_wew,'wafer-edge waveguides on a 300-mm wafer cut into an octagon per cardinal direction\n\n')
print('N_wew = ',4*h_8/w_wew,'total wafer-edge waveguides on a 300-mm wafer cut into an octagon with cardinal access\n\n')
print('N_spd = ',N_spd,'total vertical photonic communication links on each face of a 300-mm wafer cut into an octagon\n\n')
print('N_f125 = ',N_f125,'optical fibers if 125 um\n\n')
print('N_f250 = ',N_f250,'optical fibers if 250 um\n\n')

#%% synapses

N_n__list = [1e5,1e6,1e7]

w_syn__vec = np.logspace(-6,-3,100)
A_syn = w_syn__vec**2
N_syn = A_8/A_syn

fig, ax = plt.subplots(1,1, figsize = (14,10))
plt.suptitle('fraction of possible synaptic connections versus width of synapse')

color_list = ['blue1','green1','yellow1']
for ii in range(len(N_n__list)):
    k_out = N_syn/N_n__list[ii]
    k_frac = N_n__list[ii]*k_out/(N_n__list[ii]**2) # fraction of possible synaptic connections
    ax.loglog(w_syn__vec*1e6,k_frac, '-', color = colors[color_list[ii]], label = 'N_n = {:4.2e}, 1 plane'.format(N_n__list[ii]))  

color_list = ['blue3','green3','yellow3']
for ii in range(len(N_n__list)):
    k_out = 10*N_syn/N_n__list[ii]
    k_frac = N_n__list[ii]*k_out/(N_n__list[ii]**2) # fraction of possible synaptic connections
    ax.loglog(w_syn__vec*1e6,k_frac, '-', color = colors[color_list[ii]], label = 'N_n = {:4.2e}, 10 planes'.format(N_n__list[ii]))     

ax.grid('on')
ax.set_xlim([w_syn__vec[0]*1e6,w_syn__vec[-1]*1e6])
ax.set_ylim([1/N_n__list[-1],0.1])
ax.set_xlabel(r'Width of synapse [$\mu$m]')
ax.set_ylabel(r'Connection fraction') 
ax.legend()  
plt.show() 



