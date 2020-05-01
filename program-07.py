
# coding: utf-8

# In[54]:


'''
Date created: 4/27/2020
Author: Gargeya Vunnava
Github name: gargeyavunnava
Purdue username: vvunnava
Assignment 07: In this assignment, we take use the earthquake data from USGS and perform graphical analysis to identify 
possible trends in the data
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import scipy as si
import numpy as np

#reading the file downloaded from USGS into a pandas dataframe
df = pd.read_table('all_month.csv', header=0, sep=',')

#dropping nan values
mag = df.mag.dropna()

#Plotting data and storing them as .svg files.
#histrogram
ax1 = mag.plot(kind = 'hist', bins=range(0, 10,1)) #histgram with bin size = 1
ax1.set_xlabel('Magnitude')
ax1.set_title('Histogram of earthquake magnitude data (bin size =1)')
plt.savefig('histogram.svg', dpi =96) # save file as .svg
plt.close() # close plot

#Gaussian kde with width = .05
ax2 = mag.plot(kind = 'kde', bw_method=0.05) #pands.plot.kde -> default is gaussian type, bw_methods = width parameter
ax2.set_xlabel('Magnitude')
ax2.set_title('Gaussian kde plot earthquake magnitude data with width = .05')
plt.savefig('kde.svg', dpi =96)
plt.close()

#lat vs long
lat_long = df[['longitude', 'latitude']].dropna()
ax3 = lat_long.plot('longitude','latitude',kind = 'scatter') #scatter plot
ax3.set_title('Scatter plot of latitude vs longitude')
plt.savefig('lat_vs_long.svg', dpi =96)
plt.close()

#depth CDF plot
depth = np.sort(df['depth'].dropna())
cdf = np.linspace(0, 1, len(depth))
plt.plot(depth, cdf) # plotting CDF
plt.xlabel('Depth (km)')
plt.ylabel('Cumulative Distribution')
plt.title('CDF of earthquake depth data')
plt.savefig('CDF.svg', dpi =96)
plt.close()

#magnitude vs depth scatter plot
mag_vs_dep = df[['mag', 'depth']].dropna()
ax3 = mag_vs_dep.plot('mag','depth',kind = 'scatter') #scatter plot
ax3.set_xlabel('Magnitude')
ax3.set_ylabel('Depth (km)')
ax3.set_title('Magnitude vs Depth scatter plot')
plt.savefig('mag_vs_dep.svg', dpi =96)
plt.close()

#Q-Q plot for magnitude data
si.stats.probplot(mag, dist = 'norm', plot=plt) #qq plot with the help of probplot from scipy
plt.savefig('qq_plot.svg', dpi =96)
plt.close()

