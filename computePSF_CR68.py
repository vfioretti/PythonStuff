"""
 computePSF_CR68.py  -  description
 ---------------------------------------------------------------------------------
 Computing the PSF from the kalman output
 ---------------------------------------------------------------------------------
 copyright            : (C) 2019 Valentina Fioretti
 email                : valentina.fioretti@inaf.it
 ----------------------------------------------
 Usage:
 computePSF_CR68.py <filename> <theta_in> <phi_in>
 ---------------------------------------------------------------------------------
 Parameters:
 - filename: file name
 - theta_in: simulation input theta in deg. (BoGEMMS system of reference)
 - phi_in: simulation input phi in deg. (BoGEMMS system of reference)
 - ene type = MONO [0] or RANGE[1]
 - energy_min: minimum reconstructed energy in MeV
 - energy_max: maximum reconstructed energy in MeV
 - (if MONO): simulation input energy in MeV
 ---------------------------------------------------------------------------------
 Required data format: ASCII
 ---------------------------------------------------------------------------------
 Caveats:
 None
 ---------------------------------------------------------------------------------
 Example:
 computePSF_CR68.py <path+file> 30 225 1 100 400
 ---------------------------------------------------------------------------------
 Creation date:
 - 20/05/2019 by V. Fioretti
 
"""
   

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import sys

import sph_distance as sd

# Import the input parameters
arg_list = sys.argv
filename = arg_list[1]
theta_in = float(arg_list[2])
phi_in = float(arg_list[3])
ene_type = int(arg_list[4])
energy_min = float(arg_list[5])
energy_max = float(arg_list[6])

if ene_type == 0: energy_sel = float(arg_list[7])

theta_sim_all = []
phi_sim_all = []
energy_sim_all = []

f_input = open(filename, 'r')

for line in f_input:
    line = line.strip()
    columns = line.split()
    if (columns[1] != 'NaN'):
        columns[0] = float(columns[0])
        columns[1] = float(columns[1])
        columns[2] = float(columns[2])
        columns[2] = float(columns[2])

        theta_sim_all.append(columns[0]) 
        phi_sim_all.append(columns[1]) 	
        energy_sim_all.append(columns[2]) 

f_input.close()

theta_sim_all = np.array(theta_sim_all)
phi_sim_all = np.array(phi_sim_all)
energy_sim_all = np.array(energy_sim_all)



if (ene_type == 0):
	energy_sel_string = str(energy_sel)
	ene_law = "MONO"

if (ene_type == 1):
    energy_sel_string = str(energy_min)+" - "+str(energy_max)
	ene_law = "RANGE"

where_banda = np.where((energy_sim_all >= energy_min) & (energy_sim_all <= energy_max))
theta_sim = theta_sim_all[where_banda]
phi_sim = phi_sim_all[where_banda]
energy_sim = energy_sim_all[where_banda]



print '-----------------------------------------------------------------'
print '-------------------    Computing PSF   --------------------------'
print '-----------------------------------------------------------------'
print '- input file: ', filename
print '- input energy [MeV]: ', energy_sel_string
print '- input theta [deg.]: ', theta_in
print '- input phi [deg.]: ', phi_in
print '-----------------------------------------------------------------'
print '-------------------          OUTPUT           -------------------'

print '- Number of events: ', len(theta_sim)

mean = theta_sim.mean()
print '- theta mean = ', mean
standard_deviation = theta_sim.std()
print '- theta sigma = ', standard_deviation

mean = phi_sim.mean()
print '- phi mean = ', mean
standard_deviation = phi_sim.std()
print '- phi sigma = ', standard_deviation

mean = energy_sim.mean()
print '- Energy mean = ', mean
standard_deviation = energy_sim.std()
print '- Energy sigma = ', standard_deviation

# Computing the spherical distance
deg_dist = np.zeros(len(theta_sim))
for jtheta in xrange(len(theta_sim)):
	deg_dist[jtheta] = sd.spherical_distance(theta_sim[jtheta], phi_sim[jtheta], theta_in, phi_in)

deg_dist_sorted_index = np.argsort(deg_dist)
deg_dist_sorted = deg_dist[deg_dist_sorted_index]
energy_psf_sorted = energy_sim[deg_dist_sorted_index]

deg_dist_chi = deg_dist_sorted
nevents = len(deg_dist)

cr68 = deg_dist_sorted[int(0.68*nevents)]

cr68_uplimit = deg_dist_sorted[int(0.68*nevents + 0.68*3.*np.sqrt(nevents))]
err_cr68 = cr68_uplimit - cr68
print '- 68% containment radius (3-sigma error): ', np.round(cr68, 5), ' +/- ', np.round(err_cr68, 5)
print '-----------------------------------------------------------------'

