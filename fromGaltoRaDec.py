#! /usr/bin/env python

# fromGaltoRaDec.py  -  description
# ---------------------------------------------------------------------------------
# astronomical coordinates conversion
# ---------------------------------------------------------------------------------
# copyright            : (C) 2015 Valentina Fioretti
# email                : fioretti@iasfbo.inaf.it
# ----------------------------------------------
# Usage:
# fromGaltoRaDec.py  <l> <b>
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
 

import astropy
import numpy as np
import matplotlib.pyplot as plt
import sys


arg_list = sys.argv
l_coord = float(arg_list[1])
b_coord = float(arg_list[2])

from astropy.coordinates import SkyCoord  # High-level coordinates
from astropy.coordinates import ICRS, Galactic, FK4, FK5  # Low-level frames
from astropy.coordinates import Angle, Latitude, Longitude  # Angles
import astropy.units as u


c = SkyCoord(l_coord, b_coord, "galactic", unit="deg")
c2 = c.transform_to(FK5(equinox='J2000'))

print "RA [deg.]: ", c2.ra.deg
print "DEC [deg.]: ", c2.dec.deg
print "RA [hms]: ", c2.ra.hms
print "DEC [hms]: ", c2.dec.hms