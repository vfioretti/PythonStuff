"""
 sph_distance.py  -  description
 ---------------------------------------------------------------------------------
 Computing the spherical distance in degrees
 ---------------------------------------------------------------------------------
 copyright            : (C) 2014 Valentina Fioretti
 email                : fioretti@iasfbo.inaf.it
 ----------------------------------------------
 Usage:
 Result = sph_distance(theta1, phi1, theta2, phi2)
 ---------------------------------------------------------------------------------
 Parameters:
 - theta1, phi1 = position in spherical distance (in degrees) of point 1
 - theta2, phi2 = position in spherical distance (in degrees) of point 2
 - Result = Spherical distance in degrees
 ---------------------------------------------------------------------------------
 Caveats:
 None
 ---------------------------------------------------------------------------------
 Modification history:
 - 2014/07/10: added description
"""

import math

def spherical_distance(theta1, phi1, theta2, phi2):

	if ((theta1 == theta2) and (phi1 == phi2)):
		return 0;

	from_deg_to_rad = math.pi/180.0
        
	phi1 = (theta1)*from_deg_to_rad
	phi2 = (theta2)*from_deg_to_rad
        
	theta1 = theta1*from_deg_to_rad
	theta2 = theta2*from_deg_to_rad
		        
	# Computing the sperical distance in degrees:
	# Given (theta1, phi1) and (theta2, phi2) of two points 
	# on the sphere of radius R 
	# d_rad = arccos(sin(theta1)sin(theta2)cos(phi1 - phi2) + cos(theta1)cos(theta2)) 
	# d_length = R*d_rad 
	
	sph_dist = (180.0)*math.acos( (math.sin(theta1)*math.sin(theta2)*math.cos(phi1 - phi2) + math.cos(theta1)*math.cos(theta2)) )
	return sph_dist