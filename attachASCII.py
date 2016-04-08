"""
 attachASCII.py  -  description
 ---------------------------------------------------------------------------------
 attach two ASCII files
 ---------------------------------------------------------------------------------
 copyright            : (C) 2016 Valentina Fioretti
 email                : fioretti@iasfbo.inaf.it
 ----------------------------------------------
 Usage:
 attachASCII.py <filename1> <filename1>  <filename_out>
 ---------------------------------------------------------------------------------
 Parameters:
 - filename1: first file
 - filename2: second file
 - filename_out: second file
 ---------------------------------------------------------------------------------
 Required data format: .dat 
 ---------------------------------------------------------------------------------
 Caveats:
 None
 ---------------------------------------------------------------------------------
 Modification history:
 - 2016/04/04: Creation date
 
"""
from astropy.io import ascii
import sys

# Import the input parameters
arg_list = sys.argv
filename1 = arg_list[1]
filename2 = arg_list[2]
filename_out = arg_list[3]

data1 = ascii.read(filename1, format='no_header')
data2 = ascii.read(filename2, format='no_header')

len_data2 = len(data2)

for jrow in range(len_data2):
	data1.add_row(data2[jrow])
	

ascii.write(data1, filename_out, format='no_header')