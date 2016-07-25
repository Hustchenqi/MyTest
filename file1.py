# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:27:26 2016

@author: cvlab
"""
import IPython
print "IPython version:    %6.6s (need at least 1.0)" % IPython.__version__

import numpy as np
print "Numpy version:   %6.6s (need at least 1.7.1)" % np.__version__

import scipy as sp
print "Scipy version:   %6.6s (need at least 0.12.0)" % sp.__version__

import matplotlib
print "Mapltolib version:    %6.6s (need at least 1.2.1)" % matplotlib.__version__

#import sklearn
#print "Scikit-Learn version: %6.6s (need at least 0.13.1)" % sklearn.__version__
# Requests is a library for getting data from the Web
"""
import requests
print "requests version:     %6.6s (need at least 1.2.3)" % requests.__version__
"""
"""
# Networkx is a library for working with networks
import networkx as nx
print "NetworkX version:     %6.6s (need at least 1.7)" % nx.__version__
"""
"""
#BeautifulSoup is a library to parse HTML and XML documents
import BeautifulSoup
print "BeautifulSoup version:%6.6s (need at least 3.2)" % BeautifulSoup.__version__

#MrJob is a library to run map reduce jobs on Amazon's computers
import mrjob
print "Mr Job version:       %6.6s (need at least 0.4)" % mrjob.__version__

#Pattern has lots of tools for working with data from the internet
import pattern
print "Pattern version:      %6.6s (need at least 2.6)" % pattern.__version__
"""
#%%
import matplotlib.pyplot as plt

x = np.linspace(0,10,30)
y = np.sin(x)
z = y + np.random.normal(size=30)* .2
plt.plot(x,y,'ro-', label = 'A since wave')
plt.plot(x,z,'b-',label = 'Noisy sine')
plt.legend(loc = 'upper center')
plt.xlabel("X axis")
plt.ylabel("Y axis")
 #%%

