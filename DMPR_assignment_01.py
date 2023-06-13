# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:20:01 2023

@author: Plaksha
"""

# imports
import os
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datadir = r"C:\Users\Plaksha\Desktop\DSEB\DMPR\vehicles.csv"


def read_csv():
    df = pd.read_csv(datadir)
    return df

print("Time taken to read CSV: {:.6f} seconds".format(timeit.timeit(read_csv, number=1)))



df = pd.read_csv(r"C:\Users\Plaksha\Desktop\DSEB\DMPR\vehicles.csv")

# XML
start_time = timeit.default_timer()
df.to_xml('df.xml')
print("XML:\t\t\t\t", timeit.default_timer() - start_time)

# CSV
start_time = timeit.default_timer()
df.to_csv('df.csv')
print("CSV:\t\t\t\t", timeit.default_timer() - start_time)

# JSON
start_time = timeit.default_timer()
df.to_json('df.json')
print("JSON:\t\t\t\t", timeit.default_timer() - start_time)

# Excel
start_time = timeit.default_timer()
df.to_excel('df.xlsx')
print("Excel:\t\t\t", timeit.default_timer() - start_time)

# Pickle
start_time = timeit.default_timer()
df.to_pickle('df.pkl')
print("Pickle:\t\t\t", timeit.default_timer() - start_time)

# HDF5
start_time = timeit.default_timer()
df.to_hdf('df.h5', key='df', mode='w')
print("HDF5:\t\t\t\t", timeit.default_timer() - start_time)

# Parquet
start_time = timeit.default_timer()
df.to_parquet('df.parquet')
print("Parquet:\t\t\t", timeit.default_timer() - start_time)

# Feather
start_time = timeit.default_timer()
df.to_feather('df.feather')
print("Feather:\t\t\t", timeit.default_timer() - start_time)





#%% Find the size of a file `file_path` in disk
size = os.path.getsize(r"C:\Users\Plaksha\Desktop\DSEB\DMPR\vehicles.csv")
print(size)
#%%
results.append(['feather', timeit.timeit(lambda: pd.read_feather('data.feather'), number=1), os.path.getsize('data.feather')])

# Write the results to a CSV file
pd.DataFrame(results, columns=['format', 'time', 'size']).to_csv('write_time.csv', index=False)






