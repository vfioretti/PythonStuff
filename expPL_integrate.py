#! /usr/bin/env python

# expPL_integrate.py  -  description
# ---------------------------------------------------------------------------------
# integrating a power-law with exponential cut-off with different methods
# ---------------------------------------------------------------------------------
# copyright            : (C) 2015 Valentina Fioretti
# email                : fioretti@iasfbo.inaf.it
# ----------------------------------------------
# Usage:
# expPL_integrate.py <k> <gamma> <Ec> <Emin> <Emax>
# ---------------------------------------------------------------------------------
# Parameters (default = None):
# - k = normalization
# - gamma = photon index
# - Ec = cut-off energy
# - Emin = minimum energy
# - Emax = maximum energy
# ---------------------------------------------------------------------------------
# Caveats:
# ---------------------------------------------------------------------------------
# Modification history:
# - 2014/10/10: creation date
 

import pyfits
import numpy as np
import matplotlib.pyplot as plt
import sys


arg_list = sys.argv
k_norm = float(arg_list[1])
gamma = float(arg_list[2])
E_c = float(arg_list[3])
E_min = float(arg_list[4])
E_max = float(arg_list[5])

Earray = np.arange(100, 10000, 10)
ExpPL_plot = np.zeros(len(Earray))

for jbin in xrange(len(Earray)):
	ExpPL_plot[jbin] = k_norm*((Earray[jbin]**(-gamma))*np.exp(-(Earray[jbin])/(E_c)))

fig = plt.figure(1, figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_xlabel('Energy [MeV]')
ax.set_ylabel('ph cm$^{-2}$ s$^{-1}$ MeV$^{-1}$')
ax.set_title('Power-law with exponential cut-off')
ax.set_xscale('log')
ax.plot(Earray, ExpPL_plot, 'k', lw=2)
ax.set_yscale('log')

plt.text(0.7, 0.9, "Norm. = "+str(k_norm), transform=ax.transAxes)
plt.text(0.7, 0.85, "gamma = "+str(gamma), transform=ax.transAxes)
plt.text(0.7, 0.8, "Cut-off E = "+str(E_c)+ " MeV", transform=ax.transAxes)



from scipy import integrate, special
import mpmath

def ExpPL(x):
	return k_norm*(x**(-gamma))*np.exp(-x/E_c)

quad_int = integrate.quad(ExpPL, E_min, E_max)
print 'QUAD integral = ', quad_int[0]

gauss_int = integrate.fixed_quad(ExpPL, E_min, E_max)
print 'FIXED-ORDER GAUSSIAN integral = ', gauss_int[0]


def ExpPL_Wolf(x):
	return E_c*(-k_norm)*(x**(-gamma))*((x/E_c)**gamma)*mpmath.gammainc(1. - gamma, x/E_c)
	
wolf_int = ExpPL_Wolf(E_max) - ExpPL_Wolf(E_min)
print 'WOLFRAM integral = ', wolf_int


"""
def ExpPL_module(x, i):
	return k_norm*(((-E_c)**(i+1))*(x**(-gamma-i))*np.exp(-x/E_c))

iround=0
Upper = ExpPL_module(E_max, iround)
Lower = ExpPL_module(E_min, iround)
Upper_add = Upper
Lower_add = Lower
if (np.fabs(Upper) < np.fabs(Lower)):
	MOD = np.fabs(Upper)
if (np.fabs(Upper) >= np.fabs(Lower)):
	MOD = np.fabs(Lower)

print MOD
while MOD>0.000000000000001:
	iround+=1
	print iround
	print 'Upper = ', Upper
	print 'Lower = ', Lower
	print 'Upper - Lower = ', Upper - Lower
	Upper_add = Upper_add*(-gamma-(iround-1))
	print 'Upper_add = ', Upper_add
	Lower_add = Lower_add*(-gamma-(iround-1))
	print 'Lower_add = ', Lower_add
	if (iround % 2 != 0):
		Upper = Upper - Upper_add
		Lower = Lower - Lower_add
	if (iround % 2 == 0):
		Upper = Upper + Upper_add
		Lower = Lower + Lower_add

	if (np.fabs(Upper_add) < np.fabs(Lower_add)):
		MOD = np.fabs(Upper_add)
	if (np.fabs(Upper_add) >= np.fabs(Lower_add)):
		MOD = np.fabs(Lower_add)
	
	print 'MOD = ', MOD
	
VF_int = Upper - Lower
print 'VF integral = ', VF_int
"""
plt.text(0.2, 0.3, "QUAD = "+str(quad_int[0]), transform=ax.transAxes)
plt.text(0.2, 0.25, "GAUSS = "+str(gauss_int[0]), transform=ax.transAxes)
plt.text(0.2, 0.2, "WOLFRAM = "+str(wolf_int), transform=ax.transAxes)
#plt.text(0.2, 0.15, "VF = "+str(VF_int), transform=ax.transAxes)



plt.show()

