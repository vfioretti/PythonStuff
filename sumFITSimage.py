#! /usr/bin/env python

# sumFITSimage.py  -  description
# ---------------------------------------------------------------------------------
# summing the pixels of two images and save the output in a new FITS file
# with the same extension of one of the files
# ---------------------------------------------------------------------------------
# copyright            : (C) 2014 Valentina Fioretti
# email                : fioretti@iasfbo.inaf.it
# ----------------------------------------------
# Usage:
# sumFITSimage.py <file1> <file2> <file_new>
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
image1 = file1[0].data 
hdr1 = file1[0].header

file2 = pyfits.open(name_file2)
file2.info()
image2 = file2[0].data 
hdr2 = file2[0].header

naxis1_file1 = hdr1['NAXIS1']
naxis2_file1 = hdr1['NAXIS2']

naxis1_file2 = hdr2['NAXIS1']
naxis2_file2 = hdr2['NAXIS2']

image_new = image2

if ((naxis1_file1 != naxis1_file2) or (naxis2_file1 != naxis2_file2)):
	print "ERROR: the dimension of the two images is different"


for irow in xrange(naxis1_file1): 
	row_image1 = image1[irow]
	row_image2 = image2[irow]
	row_image_new = []
	for jcol in xrange(naxis2_file1): 
		row_image_new.append(row_image1[jcol] - row_image2[jcol])
	image_new[irow] = row_image_new



file_new_hdu = pyfits.PrimaryHDU(image_new, header = hdr1)
file_new = pyfits.HDUList([file_new_hdu])
file_new.writeto(name_file_new, clobber=True)

file1.close()
file2.close()
file_new.close()