# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:06:07 2020

@author: Jasen

Load World Ocean Atlas Data
"""
import numpy as np
from netCDF4 import Dataset as dt


#WOA data location
TempFile = '/Users/Jasen/Documents/Data/WOA_Data/AnalyzedMean/woa18_decav_t00_01.nc'
SaltFile = '/Users/Jasen/Documents/Data/WOA_Data/AnalyzedMean/woa18_decav_s00_01.nc'
NO3_File = '/Users/Jasen/Documents/Data/WOA_Data/AnalyzedMean/woa18_all_n00_01.nc'

#WOA data load
TempNC = dt(TempFile, 'r')
SaltNC = dt(SaltFile, 'r')
NO3_NC = dt(NO3_File, 'r')

#Extract location [NOTE:  _NC.variables == ncdisp(), _NC.variables.keys == simple list]

#ROMS reference file
RomsFile = '/Users/Jasen/Documents/Data/ROMS_ICBC/wc12_hycom_20090101_dnref99_ini_Darwin_NuteMap.nc'
RomsNC = dt(RomsFile, 'r')

ROMSlat = np.array(RomsNC.variables[latitude][:], dtype = np.float64)

#Select every point at 1 degree intervals on 0.5 degree locaitons
#Expand domain to include points outside of ROMS wc12 domain for interpolation

#locate indices of WOA lat within ROMS wc12 domain

#Locate indices of WOA lon wihin ROMS wc12 domain

#Subset WOA variables to analyzed structure file (WOAan)

#Compute density at locaiton
