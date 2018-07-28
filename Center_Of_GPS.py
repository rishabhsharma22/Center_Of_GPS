# -*- coding: utf-8 -*-


import numpy as np


def center(gps_data_file_loc):
    latitude= []
    longitude = []
    with open(gps_data_file_loc,'r') as fp:
        line = fp.readline()
        print(line)
        while line:
            lat,long = line.split()
            latitude.append(float(lat))
            longitude.append(float(long))
            line = fp.readline()
            
        return np.mean(np.asarray(latitude)),np.mean(np.asarray(longitude))



            
    
    