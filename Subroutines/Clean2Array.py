# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:13:34 2020

@author: Jasen
"""
import numpy as np

def Clean2Array(var1, var2):
    """ removes nans from two arrays maintaining index size """
    if var1.size == var2.size :
        #find nan in array 1
        inan1 = np.argwhere(np.isnan(var1))
                
        #delete location of nan in array 2
        new_var2 = np.delete(var2, inan1)
        new_var1 = np.delete(var1, inan1)
        
        #find nan in new array 2
        inan2 = np.argwhere(np.isnan(new_var2))
        clean_var1 = np.delete(new_var1, inan2)
        clean_var2 = np.delete(new_var2, inan2)
        
        Arrays = (clean_var1, clean_var2)
        
    else :
        Arrays = 'arrays not the same size'
        
    return Arrays
        
    
