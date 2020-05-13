# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:06:07 2020

@author: Jasen

Load World Ocean Atlas Data
"""
import numpy as np
from netCDF4 import Dataset as dt


TempFile = '/Users/Jasen/Documents/Data/WOA_Data/AnalyzedMean/woa18_decav_t00_01.nc'
SaltFile = '/Users/Jasen/Documents/Data/WOA_Data/AnalyzedMean/woa18_decav_s00_01.nc'
NO3_File = '/Users/Jasen/Documents/Data/WOA_Data/AnalyzedMean/woa18_all_n00_01.nc'

TempNC = dt(TempFile, 'r')
SaltNC = dt(SaltFile, 'r')
NO3_NC = dt(NO_File, 'r')

