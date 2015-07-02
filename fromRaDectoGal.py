#! /usr/bin/env python

# fromRaDectoGal.py  -  description
# ---------------------------------------------------------------------------------
# astronomical coordinates conversion
# ---------------------------------------------------------------------------------
# copyright            : (C) 2015 Valentina Fioretti
# email                : fioretti@iasfbo.inaf.it
# ----------------------------------------------
# Usage:
# fromRaDectoGal.py  <ra> <dec>
# ---------------------------------------------------------------------------------
# Parameters (default = None):
# - ra: right ascension in hh mm ss
# - dec: declination in deg m s
# ---------------------------------------------------------------------------------
# Usage:
# J00040+7020 becomes "00 04 00" "+70 20 00"
# > python fromRaDectoGal.py "00 04 00" "+70 20 00"
# Output:
# > l [deg.]:  118.928588067
# > b [deg.]:  7.83127582313
# ---------------------------------------------------------------------------------
# Modification history:
# - 2015/07/02: creation date
 

import astropy
import numpy as np
import matplotlib.pyplot as plt
import sys


arg_list = sys.argv
ra_coord = arg_list[1]
dec_coord = arg_list[2]

from astropy.coordinates import SkyCoord  # High-level coordinates
from astropy.coordinates import ICRS, Galactic, FK4, FK5  # Low-level frames
from astropy.coordinates import Angle, Latitude, Longitude  # Angles
import astropy.units as u


c = SkyCoord(ra_coord, dec_coord, "fk5", unit=(u.hourangle, u.deg))
c2 = c.galactic


print "l [deg.]: ", c2.l.deg
print "b [deg.]: ", c2.b.deg