import numpy as np
from matplotlib import pyplot as plt

from _util import physical_constants, color_dictionary
p = physical_constants()
colors = color_dictionary()

plt.close('all')

plt.rcParams['axes.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 10

# plt.rcParams['figure.figsize'] = [14,11]
# plt.rcParams['figure.titlesize'] = 8
plt.rcParams['legend.fontsize'] = 8

plt.rcParams['axes.linewidth'] = 0.75
plt.rcParams['axes.labelsize'] = 10

plt.rcParams['legend.fontsize'] = 8
plt.rcParams['legend.loc'] = 'best'

plt.rcParams['lines.linewidth'] = 1
plt.rcParams['lines.markersize'] = 4

plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['xtick.major.bottom'] = True
plt.rcParams['xtick.major.top'] = True
plt.rcParams['xtick.major.size'] = 3
plt.rcParams['xtick.major.width'] = 0.25
plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['xtick.minor.size'] = 1.5
plt.rcParams['xtick.minor.width'] = 0.15

plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['ytick.major.left'] = True
plt.rcParams['ytick.major.right'] = True
plt.rcParams['ytick.major.size'] = 3
plt.rcParams['ytick.major.width'] = 0.25
plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['ytick.minor.size'] = 1.5
plt.rcParams['ytick.minor.width'] = 0.15

# plt.rcParams['grid.color'] = colors['grey4']
# plt.rcParams['grid.linestyle'] = 'solid'
# plt.rcParams['grid.linewidth'] = 0.25

plt.rcParams['figure.autolayout'] = False

plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.format'] = 'pdf' # 'png' # plt.rcParams['axes.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['xtick.labelsize'] = 8

# plt.rcParams['figure.figsize'] = [14,11]
plt.rcParams['figure.titlesize'] = 8
plt.rcParams['legend.fontsize'] = 8

plt.rcParams['figure.autolayout'] = False

plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.format'] = 'pdf' # 'png' # 

# plt.rcParams['figure.autolayout'] = False

#%%
#--- inputs ---#
r_300 = 0.15 # radius of 300-mm wafer
w_wew = 1e-5 # pitch of wafer-edge waveguides
w_spd = 2.5e-5 # pitch of single-photon detectors in 1D
r_f125 = 125e-6/2 # radius of bare fiber
r_f250 = 250e-6/2 # radius of acrylic-clad fiber
gamma = 0.5772 # eulers constant

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

#%% initial random graph as point of reference (Erdos-Renyi APL)

NVec = np.logspace(3,8,1000)
APL_vec = [2,3,4,5] # vector of average path lengths to consider
kExpectation_vec = [10,100,1000,10000]

APL_mat = np.zeros([len(NVec),len(kExpectation_vec)])
kExpectation_mat = np.zeros([len(NVec),len(APL_vec)])
    
for ii in range(len(kExpectation_vec)):
    APL_mat[:,ii] = ( np.log(NVec[:]) - gamma ) / np.log(kExpectation_vec[ii]) + 1/2
    
for ii in range(len(APL_vec)):
    kExpectation_mat[:,ii] = np.exp( ( np.log(NVec[:]) - gamma ) / ( APL_vec[ii] - 0.5 )  )

# plot for paper
tn = 1.1*8.6/2.54
fig, ax = plt.subplots(nrows = 1, ncols = 1, sharex = True, sharey = False, figsize = (tn,tn/1.618))
# fig.suptitle('Erdos-Renyi random graph')

color_list = ['blue3','red3','green3','yellow3']

for ii in range(len(APL_vec)):
    ax.loglog(NVec,kExpectation_mat[:,ii], '-', color = colors[color_list[ii]], label = 'APL = {:d}'.format(APL_vec[ii]))
ax.set_ylabel(r'$\bar{k}$')
ax.set_xlabel(r'Total Nodes, $N_{tot}$')
ax.tick_params(axis = 'both')
ax.grid(which = 'both', axis = 'both')
ax.set_xlim([NVec[0],NVec[-1]])
# ax[1].set_ylim([1,2e5])
# plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout()
plt.show()


#%% average path length vs synapse width

w_sy__vec = np.logspace(-6,-2,1000)
N_n__list = [1e5,1e6,1e7]
p_e__list = [1,10]
p_p__list = [1,10]
w_sy__vec = np.logspace(-6,-3,100)
w_wg__vec = np.logspace(-6,-5,100)
A_syn = w_sy__vec**2
N_syn = A_8/A_syn

L_bar_e = np.zeros([len(w_sy__vec),len(N_n__list),len(p_e__list)])
L_bar_p = np.zeros([len(w_sy__vec),len(N_n__list),len(p_p__list)])
indices_list = []
L_bar__10 = np.zeros([len(w_sy__vec),len(N_n__list)])
indices_list__e = []
indices_list__p = []

for ii in range(len(N_n__list)):
    indices_list__e.append([])
    for jj in range(len(p_e__list)):
        k = p_e__list[jj]*A_8/(w_sy__vec**2 * N_n__list[ii]) 
        L_bar_e[:,ii,jj] = ( np.log(N_n__list[ii]) - gamma ) / np.log(k) + 1/2
        indices_list__e[ii].append( np.where( L_bar_e[:,ii,jj] > 0 ) )

for ii in range(len(N_n__list)):
    indices_list__p.append([])
    for jj in range(len(p_p__list)):
        k = ( p_p__list[jj]/w_wg__vec)*np.sqrt(A_8/N_n__list[ii]) 
        L_bar_p[:,ii,jj] = ( np.log(N_n__list[ii]) - gamma ) / np.log(k) + 1/2
        indices_list__p[ii].append( np.where( L_bar_p[:,ii,jj] > 0 ) )

color_list = ['blue3','green3','yellow3']
linestyle_list = ['solid','dashed','dotted']
fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = False, sharey = False, figsize = (tn,2*tn/1.618))

# plt.suptitle('Network average path length versus width of synapse')

for ii in range(len(N_n__list)):
    for jj in range(len(p_e__list)):
        ax[0].semilogx(w_sy__vec[indices_list__e[ii][jj]]*1e6,L_bar_e[indices_list__e[ii][jj],ii,jj][0], linestyle = linestyle_list[jj], linewidth = 1.5, color = colors[color_list[ii]], label = 'N_n = {:4.1e}, p_e = {:d}'.format(N_n__list[ii],p_e__list[jj]))    
        
for ii in range(len(N_n__list)):
    for jj in range(len(p_p__list)):
        ax[1].plot(w_wg__vec[indices_list__p[ii][jj]]*1e6,L_bar_p[indices_list__p[ii][jj],ii,jj][0], linestyle = linestyle_list[jj], linewidth = 1.5, color = colors[color_list[ii]], label = 'N_n = {:4.1e}, p_p = {:d}'.format(N_n__list[ii],p_p__list[jj]))            

ax[0].set_xlim([w_sy__vec[0]*1e6,w_sy__vec[-1]*1e6])
ax[0].set_ylim([1,5]) 
ax[0].set_xlabel(r'$w_{sy}$ [$\mu$m]')
ax[0].set_ylabel(r'$\bar{L}$')
ax[0].legend() 

ax[1].set_xlim([w_wg__vec[0]*1e6,w_wg__vec[-1]*1e6])
ax[1].set_ylim([1,5]) 
ax[1].set_xlabel(r'$w_{wg}$ [$\mu$m]')
ax[1].set_ylabel(r'$\bar{L}$')
ax[1].legend() 

ax[0].grid(which = 'both', axis = 'x')
ax[0].grid(which = 'major', axis = 'y')
ax[1].grid(which = 'both', axis = 'x')
ax[1].grid(which = 'major', axis = 'y')

plt.tight_layout()
plt.show() 

#%% num planes alt alt

N__list = np.logspace(4,7,1000)
w_wg__list = [1.5e-6,3e-6,6e-6]
w_sy__list = np.logspace(-5,-4,6)
L__bar = 2.5

p_e__mat = np.zeros([len(N__list),len(w_sy__list)])
for ii in range(len(w_sy__list)):
    k = np.exp( ( np.log(N__list) - gamma ) / (L__bar-1/2) )
    p_e__mat[:,ii] = np.ceil( k * w_sy__list[ii]**2 * N__list/A_8 )
 
p_p__mat = np.zeros([len(N__list),len(w_sy__list)])
for ii in range(len(w_wg__list)):
    k = np.exp( ( np.log(N__list) - gamma ) / (L__bar-1/2) )
    p_p__mat[:,ii] = np.ceil( k * w_wg__list[ii] * np.sqrt(N__list/A_8) )
        
fig, ax = plt.subplots(nrows = 1, ncols = 1, sharex = True, sharey = False, figsize = (tn,tn/1.618))
# plt.suptitle('Ratio of waveguide area to electronic synapse circuit area\nw_wg = {:3.1f}um; L_apl = {:d}'.format(w_wg*1e6,L_apl))
# color_list = ['blue3','green3','yellow3']
# color_list__e = ['blue5','blue4','blue3','blue2','blue1','green5','green4','green3','green2','green1','yellow5','yellow4','yellow3','yellow2','yellow1','red5','red4','red3','red2','yellow1']
color_list__e = ['blue5','blue3','blue1','green1','green3','green5']
linestyle_list = ['solid','dashed','dashed','dashed','dashed','solid']
linewidth_list = [2,1.5,1.5,1.5,1.5,2]
for ii in range(len(w_sy__list)):
    ax.loglog(N__list,p_e__mat[:,ii], linestyle = linestyle_list[ii], linewidth = linewidth_list[ii], color = colors[color_list__e[ii]], label = 'w_sy = {:3.1f}um'.format(w_sy__list[ii]*1e6))    

# linestyle_list = ['dashed','dotted','dashdot']
linestyle_list = ['solid','solid','solid']
color_list__p = ['red5','red3','red1']
for ii in range(len(w_wg__list)):
    ax.loglog(N__list,p_p__mat[:,ii], linestyle = linestyle_list[ii], linewidth = 2, color = colors[color_list__p[ii]], label = 'w_wg = {:3.1f}um'.format(w_wg__list[ii]*1e6))    
        
# ax.set_xlim([N__list[0],N__list[-1]])
ax.set_xlim([3e4,5e6])
ax.set_ylim([1,3e1])

ax.set_ylabel(r'Number of planes ($p_p$ or $p_e$)')
ax.set_xlabel(r'$N_{300}$')

ax.grid('on', which = 'both', axis = 'both')

plt.subplots_adjust(wspace=0, hspace=0)
 
ax.legend() 

plt.tight_layout()
plt.show() 


#%% squid size estimate

I_c__vec = np.logspace(-5,-3,1000)

fig, ax = plt.subplots(nrows = 1, ncols = 1, sharex = True, sharey = False, figsize = (tn,tn/1.618)) 
# fig.suptitle('Washer size vs squid Ic for beta_L = 1')
w_sq = p['Phi0']/(p['mu0']*I_c__vec)
w_sy = 2*w_sq
ax.loglog(I_c__vec*1e6,w_sq*1e6, '-', color = colors['blue3'], label = 'w_sq') # , label = 'Isy = {:5.2f}uA'.format(Isy) 
ax.loglog(I_c__vec*1e6,w_sy*1e6, '-', color = colors['red3'], label = 'w_sy') # , label = 'Isy = {:5.2f}uA'.format(Isy) 
     
ax.set_xlabel(r'$I_{c}$ [$\mu A$]') 
ax.set_ylabel(r'$w_{sq}$ and $w_{sy}$ [$\mu m$]') 
ax.grid('on', which = 'both', axis = 'both')
ax.set_xlim([I_c__vec[0]*1e6,I_c__vec[-1]*1e6])
# ax.set_ylim([1,1e2])
ax.legend()

# fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = True, sharey = False, figsize = (14,11)) 
# # fig.suptitle('Washer size vs squid Ic for beta_L = 1')

# ax[0].loglog(I_c__vec*1e6,2*p['Phi0']*I_c__vec*1e21/(2*np.pi), '-', color = colors['blue3']) # , label = 'Isy = {:5.2f}uA'.format(Isy)
# ax[0].set_ylabel(r'$E_{sq}$ [zJ]') 
# ax[0].grid('on', which = 'both', axis = 'both')

# w_sq = p['Phi0']/(np.pi*p['mu0']*I_c__vec)
# w_sy = 3*w_sq
# ax[1].loglog(I_c__vec*1e6,w_sq*1e6, '-', color = colors['blue3'], label = 'w_sq') # , label = 'Isy = {:5.2f}uA'.format(Isy) 
# ax[1].loglog(I_c__vec*1e6,w_sy*1e6, '-', color = colors['red3'], label = 'w_sy') # , label = 'Isy = {:5.2f}uA'.format(Isy) 
     
# ax[1].set_xlabel(r'$I_{c}$ [$\mu A$]') 
# ax[1].set_ylabel(r'$w_{sq}$ and $w_{sy}$ [$\mu m$]') 
# ax[1].grid('on', which = 'both', axis = 'both')
# ax[1].set_xlim([I_c__vec[0]*1e6,I_c__vec[-1]*1e6])
# ax[1].set_ylim([1,1e2])
# ax[1].legend()

# plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout()
plt.show()


#%% from Bryce

## Calculations
Cap = np.geomspace(1e-16, 1e-14, 1000)
V_dd = .8
N = 1000
e = 1.6e-19
E_photon = 1.3e-19
E_bit = E_photon*Cap*V_dd/e 
E_sup = 1e-15

freqs = np.geomspace(1e6, 1e9, 1000)
C_low = 1e-16
C_mid = 1e-15
C_high = 1e-14

Popt_low = freqs*N*E_photon*C_low*V_dd/e 
Popt_mid = freqs*N*E_photon*C_mid*V_dd/e 
Popt_high = freqs*N*E_photon*C_high*V_dd/e 
Popt_sup = freqs*N*E_sup/(1000)

## Plotting
fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = False, sharey = False, figsize = (tn,2*tn/1.618))
red_list = ['red1','red3','red5']
blue_list = ['blue1', 'blue3', 'blue5']

ax[0].loglog(1e15*Cap, 1e15*E_bit, '-', color = colors[red_list[1]], label = 'Semiconductor')
ax[0].axhline(1, ls='--', color = colors[blue_list[1]], label = 'Superconductor' )
intersection = Cap[np.min(np.where(E_bit > E_sup))]
ax[0].axvspan(1e15*np.min(Cap), 1e15*intersection, alpha=0.1, color = colors[red_list[1]])
ax[0].axvspan(1e15*intersection, 1e15*max(Cap), alpha=0.1, color = colors[blue_list[1]])

ax[1].loglog(freqs, Popt_high, '-', color = colors[red_list[2]], label = '10 fF')
ax[1].loglog(freqs, Popt_mid, '-', color = colors[red_list[1]], label = '1 fF')
ax[1].loglog(freqs, Popt_low, '-', color = colors[red_list[0]], label = '100 aF')
ax[1].loglog(freqs, Popt_sup, '-', color = colors[blue_list[1]], label = 'SNSPD')

ax[0].set_ylabel(r'$E_{opt}$ (fJ)')
ax[0].set_xlabel(r'Semiconductor Receiver Capacitance (fF)')
ax[0].legend(prop={'size':8}) 
ax[0].tick_params(axis = 'both')
ax[0].grid(which = 'both', axis = 'both')
ax[0].set_xlim([1e15*Cap[0],1e15*Cap[-1]])

ax[1].set_xlabel(r'Maximum Spiking Frequency (Hz)')
ax[1].set_ylabel(r'Peak Optical Power (W)')
ax[1].legend(prop={'size':8})
ax[1].tick_params(axis = 'both')
ax[1].grid(which = 'both', axis = 'both')
ax[1].set_xlim([freqs[0],freqs[-1]])

plt.subplots_adjust(wspace=0, hspace=.5)
# fig.savefig('opticalv2')

plt.tight_layout()
plt.show()
