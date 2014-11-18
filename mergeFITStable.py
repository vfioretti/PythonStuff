#! /usr/bin/env python

# mergeFITStable.py  -  description
# ---------------------------------------------------------------------------------
# attach two FITS tables and save the output in a new FITS file
# with the same extension of one of the files
# ---------------------------------------------------------------------------------
# copyright            : (C) 2014 Valentina Fioretti
# email                : fioretti@iasfbo.inaf.it
# ----------------------------------------------
# Usage:
# mergeFITStable.py <file1> <file2> <file_new>
# ---------------------------------------------------------------------------------
# Parameters (default = None):
# - file1 = file name of the first file
# - file2 = file name of the second file
# - file_new = file name of new FITS file
# ---------------------------------------------------------------------------------
# Caveats:
# The subtraction is file1 - file2
# ---------------------------------------------------------------------------------
# Modification history:
# - 2014/10/10: creation date
 

import pyfits
import numpy as np
import matplotlib.pyplot as plt
import sys


arg_list = sys.argv
name_file1 = arg_list[1]
name_file2 = arg_list[2]
name_file_new = arg_list[3]

file1 = pyfits.open(name_file1)
file1.info()
data1 = file1[1].data 
hdr1 = file1[1].header

file2 = pyfits.open(name_file2)
file2.info()
data2 = file2[1].data 
hdr2 = file2[1].header

nrows1 = data1.shape[0]
nrows2 = data2.shape[0]
nrows = nrows1 + nrows2

file_new_hdu = pyfits.BinTableHDU.from_columns(file1[1].columns, nrows=nrows, header = hdr1)
for colname in file1[1].columns.names:
	file_new_hdu.data[colname][nrows1:] = file2[1].data[colname]
	
file_new_hdu.writeto(name_file_new, clobber=True)



file1.close()
file2.close()
