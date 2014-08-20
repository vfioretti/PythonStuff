"""
 galaxy_aitoff.py  -  description
 ---------------------------------------------------------------------------------
 Function to plot the galaxy in galactic coordinates and AITOFF projection.
 It is possible to plot a set of squares/rings or points as additional feature.
 ---------------------------------------------------------------------------------
 copyright            : (C) 2014 Valentina Fioretti
 email                : fioretti@iasfbo.inaf.it
 ----------------------------------------------
 Usage:
 galaxy_aitoff.py
 ---------------------------------------------------------------------------------
 Parameters (default = None):
 - title: title of the plot
 - source_list: ASCII file (+ path) with the galactic coordinates, in degrees, of the sources				                
 - ring_list: ASCII file (+ path) with the galactic coordinates, in degrees, of the rings center plus the radius
 - vip_sources: flag to load the most famous Gamma-ray sources (Crab, Vela, Geminga, 3C 454.3)
 ---------------------------------------------------------------------------------
 Required data input format: ASCII file (one entry each row)
 - Sources:
 l_1 b_1
 - Rings:
 l_1 b_1 r_1 
 ---------------------------------------------------------------------------------
 Caveats:
 None
 ---------------------------------------------------------------------------------
 Example:
 import galaxy_aitoff as gl
 gl.plgal()
 ---------------------------------------------------------------------------------
 Modification history:
 - 2014/06/30: upper limits are plotted using the bugged lower limit of matplotlib errorbar instead of building arrows.
 
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from math import pi
import sys


def plgal(title='', source_list='', square_list = '', ring_list='', vip_sources=0):
	deg2rad = np.pi/180.
	
	# converting latitude to be plotted in the 180, 90, 0, 270, 180 axis
	def convert_l(l_in):
			if ((l_in >= 0.) & (l_in <= 180.)):
				l_in = l_in*(-1.) 
			if (l_in > 180.):
				l_in = 360. - l_in
			return l_in

	fig = plt.figure(1,figsize=[10,5])
	ax = fig.add_subplot(111, projection='aitoff')

	tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
	ax.set_xticklabels(tick_labels)

	# Loading the sources
	if source_list:
		l_source = []
		b_source = []
		f_read = open(source_list, 'r')
		for line in f_read:
			line = line.strip()
			columns = line.split()
			columns[0] = float(columns[0])  # converting from string to float
			columns[1] = float(columns[1])
			l_in = convert_l(columns[0])*deg2rad
			b_in = columns[1]*deg2rad
			l_source.append(l_in) 
			b_source.append(b_in)
		ax.scatter(l_source, b_source, s=50)

	# Loading the squares
	if ring_list:
		f_read = open(ring_list, 'r')
		for line in f_read:
			line = line.strip()
			columns = line.split()
			columns[0] = float(columns[0])  # converting from string to float
			columns[1] = float(columns[1])
			columns[2] = float(columns[2])
			l_in = convert_l(columns[0])
			b_in = columns[1]
			r_in = columns[2]
			ax.add_artist(Circle(xy=((l_in)*deg2rad, (b_in)*deg2rad), facecolor='none', fill='False', edgecolor='k', radius=r_in*deg2rad)) 

	# Loading the vip sources	
	if vip_sources:
		crab_coord = [convert_l(184.557593)*deg2rad, -5.784197*deg2rad]
		vela_coord = [convert_l(263.552021)*deg2rad, -2.787006*deg2rad]
		geminga_coord = [convert_l(195.13428)*deg2rad, 4.26608*deg2rad]
		diamond_coord = [convert_l(86.1110374)*deg2rad, -38.1837815*deg2rad]
		lcoord = [crab_coord[0], vela_coord[0], geminga_coord[0], diamond_coord[0]]
		bcoord = [crab_coord[1], vela_coord[1], geminga_coord[1], diamond_coord[1]]
		ax.scatter(lcoord, bcoord, color='r', marker='*', s=50)
		
	# Make-up
	plt.grid(True)
	plt.title(title)
	plt.text(0,-(90+15)*deg2rad,'Galactic longitude (degrees)',
      ha='center', va='center')
	plt.ylabel('Galactic latitude (degrees)')

	plt.show()


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    plgal()
    
    
