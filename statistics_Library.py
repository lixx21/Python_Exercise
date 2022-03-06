#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import statistics
import scipy.stats

"""
statistics function for vector
Median || Mid value
Mean || Average
Mode || Most occurs in element
"""
C = np.array([1,7,3,8,5,6,10,8,9])
print ("median using statistics function = ", statistics.median(C))
print("mean using statistics function = ", statistics.mean(C))
print("mode using statistics function = ", statistics.mode(C))

print("=====================================================")

"""
for matrix
Median || Mid value
Mean || Average
Mode || Most occurs in element
"""
print("median using numpy function = ", np.median(C))
print("mean using numpy function = ", np.mean(C))
print("mode using scipy function = ", scipy.stats.mode(C, axis=None))

print("=====================================================")


"""
in every columns in matrix
Median || Mid value
Mean || Average
Mode || Most occurs in element
"""
A = np.array([[8,3,3], [3,3,1], [8,9,1]])
print(np.median(A, axis=0))
print(np.mean(A, axis=0))
print(scipy.stats.mode(A, axis=0))

print("=====================================================")

"""
in every rows in matrix
Median || Mid value
Mean || Average
Mode || Most occurs in element
"""
B = np.array([[1,2,1], [2,3,2], [8,8,1]])
print(np.median(B,axis=1))
print(np.mean(B, axis=1))
print(scipy.stats.mode(B, axis=1))

print("=====================================================")

#Variance and standard deviation and range
print(np.var(B))
print(np.std(B))
print(np.ptp(B))

print("=====================================================")

#in every columns
print(np.var(B, axis=0))
print(np.std(B, axis=0))
print(np.ptp(B, axis=0))

print("=====================================================")

#in every rows
print(np.var(B, axis=1))
print(np.std(B, axis=1))
print(np.ptp(B, axis=1))


# In[ ]:




