# visLightCurve.py  -  description
# ---------------------------------------------------------------------------------
# Plotting the light curve from AGILE data
# ---------------------------------------------------------------------------------
# copyright            : (C) 2013 Valentina Fioretti
# email                : fioretti@iasfbo.inaf.it
# ----------------------------------------------
# Usage:
# visLightCurve.py out_name N_lc "Title" filename1 "label1" filename2 "label2"
# ---------------------------------------------------------------------------------
# Parameters:
# - out_name: name of the saved image
# - N_lc:     number of loaded light curves (<= 5)
# - "Title":  plot title
# - filename: path+name of the file [string]
# - "label":  light curve label 
# ---------------------------------------------------------------------------------
# Required data format: ASCII file
# - column 1 = flux in photons cm-2 s-1
# - column 2 = flux error in photons cm-2 s-1
# - column 3 = error keyword (0 = standard data point, 1 = upper limit)
# - column 4 = time start of the bin [MJD]
# - column 5 = time bin in days
# ---------------------------------------------------------------------------------
# Caveats:
# The script loads a maximum of 5 light curves
# ---------------------------------------------------------------------------------
# Example:
# visLightCurve.py agile_lc 2 "Title" /pathtolc1/lc1.dat "Light curve 1" /pathtolc2/lc2.dat "Light curve 2"
# ---------------------------------------------------------------------------------
# Modification history:
# - 2013/10/15: upper limits are plotted using the bugged lower limit of matplotlib errorbar instead of building arrows.

import numpy as np
import matplotlib.pyplot as plt

import sys


# Import the input parameters
arg_list = sys.argv
out_name = arg_list[1]
N_lc = int(arg_list[2])
plt_title = arg_list[3]

# Plotting environment
fig = plt.figure(1, figsize=(10, 5))
txt = fig.suptitle(plt_title, size = 15)
ax_lc = fig.add_subplot(111)
ax_lc.set_xlabel('Time [MJD]')
ax_lc.set_ylabel('10$^{-8}$ photons cm$^{-2}$ s$^{-1}$')
ax_lc.minorticks_on()
ax_lc.tick_params(axis='x', which='minor', length=7)        
ax_lc.tick_params(axis='y', which='minor', length=7)        
ax_lc.tick_params(axis='x', which='major', length=10)        
ax_lc.tick_params(axis='y', which='major', length=10)        

color_array = ['k','b','r','g','c']
legend_array = []
name_arg = 2
label_arg = name_arg + 1

for jlc in xrange(N_lc): 
    name_arg = name_arg + 2 
    label_arg = label_arg + 2
    lc_name = arg_list[name_arg]
    lc_label = arg_list[label_arg]


    # read the .dat file with the light curve data
    f_lc = open(lc_name, 'r')

    # Reading the data
    flux_lc = []
    err_flux_lc = []
    err_type_lc = []
    t_start_lc = []
    t_bin_lc = []

    for line in f_lc:
        line = line.strip()
        columns = line.split()
        columns[0] = float(columns[0])  # converting from string to float
        columns[1] = float(columns[1])
        columns[2] = int(columns[2])
        columns[3] = float(columns[3])
        columns[4] = float(columns[4])

        flux_lc.append(columns[0])
        err_flux_lc.append(columns[1])
        err_type_lc.append(columns[2])
        t_start_lc.append(columns[3])
        t_bin_lc.append(columns[4])


    flux_lc = np.array(flux_lc) 
    flux_lc = flux_lc/(10**(-8))
    err_flux_lc = np.array(err_flux_lc) 
    err_flux_lc = err_flux_lc/(10**(-8))
    err_type_lc = np.array(err_type_lc) 
    t_start_lc = np.array(t_start_lc) 
    t_bin_lc = np.array(t_bin_lc) 

    t_center_lc = np.zeros(len(t_start_lc))
    for jbin in xrange(len(t_start_lc)):
        t_center_lc[jbin] = t_start_lc[jbin] + t_bin_lc[jbin]/2.

    # Separate the bins with error from upper limits
    where_noupper = np.where(err_type_lc == 0)
    where_upper = np.where(err_type_lc == 1)

    where_noupper = where_noupper[0]
    where_upper = where_upper[0]
    
    uplims = np.zeros(len(flux_lc))
    uplims[where_upper] = True
    color_lc = color_array[jlc]
    
    ax_lc.errorbar(t_center_lc, flux_lc, xerr=(t_bin_lc)/2., yerr=err_flux_lc, marker='o', fmt=color_lc, linestyle='None', elinewidth=1., capsize=0)

    yrange = ax_lc.get_ylim()
    print yrange
    err_flux_lc[where_upper] = (yrange[1] - yrange[0])/20.

    ax_lc.errorbar(t_center_lc, flux_lc, xerr=(t_bin_lc)/2., yerr=err_flux_lc, uplims=uplims, fmt=color_lc, linestyle='None', elinewidth=1., capsize=0)

"""
    if (where_noupper_zero.size):
       flux_lc_noupper = flux_lc[where_noupper]        
       err_flux_lc_noupper = err_flux_lc[where_noupper]
       err_type_lc_noupper = err_type_lc[where_noupper]
       t_center_lc_noupper = t_center_lc[where_noupper]
       t_bin_lc_noupper = t_bin_lc[where_noupper]
       ax_lc.errorbar(t_center_lc_noupper, flux_lc_noupper, xerr=(t_bin_lc_noupper)/2., yerr=err_flux_lc_noupper, fmt=color_lc, linestyle='None', elinewidth=1, capsize=0)

    if (where_upper_zero.size):        
       flux_lc_upper = flux_lc[where_upper]
       err_flux_lc_upper = err_flux_lc[where_upper]
       err_type_lc_upper = err_type_lc[where_upper]
       t_center_lc_upper = t_center_lc[where_upper]
       t_bin_lc_upper = t_bin_lc[where_upper]    
       ax_lc.errorbar(t_center_lc_upper, flux_lc_upper, xerr=(t_bin_lc_upper)/2., fmt=color_lc, linestyle="None", elinewidth=1, capsize=0)

       flux_lc_upper_min = min(flux_lc_upper)
       flux_lc_upper_max = max(flux_lc_upper)
       arrow_l = (flux_lc_upper_max - flux_lc_upper_min)/50  
       ax_lc.errorbar(t_center_lc_upper, flux_lc_upper-arrow_l, yerr=arrow_l, fmt=color_lc, linestyle="None", elinewidth=1, lolims=True)

    plt.text(0.05, 0.9 - jlc*0.05, lc_label, transform=ax_lc.transAxes, color=color_lc, size = 14)
"""

filename_png = out_name + '.png'
plt.grid()
plt.savefig(filename_png, dpi=200)

plt.show()
