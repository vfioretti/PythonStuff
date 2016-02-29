"""
 convertFITStoJSON.py  -  description
 ---------------------------------------------------------------------------------
 Function to convert a FITS file to a JSON file
 ---------------------------------------------------------------------------------
 Author               : 2016 Valentina Fioretti
 email                : fioretti@iasfbo.inaf.it
 ----------------------------------------------
 Usage:
 FITStoJSON()
 ---------------------------------------------------------------------------------
 Parameters (default = None):
 - title: title of the plot
 - source_list: ASCII file (+ path) with the galactic coordinates, in degrees, of the sources				                
 - ring_list: ASCII file (+ path) with the galactic coordinates, in degrees, of the rings center plus the radius
 - vip_sources: flag to load the most famous Gamma-ray sources (Crab, Vela, Geminga, 3C 454.3)
 ---------------------------------------------------------------------------------
 Required data input format: ASCII file (one entry each row)
 Optional parameters: color keyword c_1 (integer) for points and fill keyword (0/1) plus fill color 
 (integer) for the rings (f_1 and fc_1)
 - Sources:
 l_1 b_1 (c_1)
 - Rings:
 l_1 b_1 r_1 (f_1 fc_1)
 ---------------------------------------------------------------------------------
 Caveats:
 None
 ---------------------------------------------------------------------------------
 Example:
 import convertFITStoJSON as js
 js.FITStoJSON()
 ---------------------------------------------------------------------------------
 Modification history:
 - 2014/08/20: creation date
 
"""

import numpy as np
import matplotlib as np
from astropy.io import fits
import json

def FITStoJSON(fits_file='', out_file=''):
    hdulist = fits.open(fits_file)

    tbdata = hdulist[1].data
    
    evt_id = tbdata.field('EVT_ID')
    evt_id = evt_id.tolist()
    vol_id = tbdata.field('VOLUME_ID')
    vol_id = vol_id.tolist()
    z_ent = tbdata.field('Z_ENT')
    z_ent = z_ent.tolist()
    e_part = tbdata.field('E_KIN_ENT')
    e_part = e_part.tolist()
    part_id = tbdata.field('PARTICLE_ID')
    part_id = part_id.tolist()
    e_dep = tbdata.field('E_DEP')
    e_dep = e_dep.tolist()

    # translate the fits columns into a dictionary
    fits_dict = {
        'EVT_ID': evt_id,
        'VOLUME_ID': vol_id,
        'Z_ENT': z_ent,
        'E_KIN_ENT': e_part,
        'PARTICLE_ID': part_id,
        'E_DEP': e_dep
    }


    # Open the json
    if (out_file != ''):
        write_file = open(out_file,"w")
    else:
        write_file = open('out.json',"w")

    # write the dictionary into the json
    json.dump(fits_dict,write_file, indent=4)

    # Close the json and fits
    write_file.close()
    hdulist.close()

if __name__ == '__main__':
    FITStoJSON()
    
    
