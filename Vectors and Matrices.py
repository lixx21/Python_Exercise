#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# 1 * 4 dimensional VECTOR
M = np.array([7,8,9,1]);
N = np.array([1,2,3,4]);
print (M + N)

# 3 * 1 dimensional vector x scalar 2
A = np.array([[1],[2], [3]]);
B = 2;
print (A * B);

#Matrix(3*3) x Matrix(3*2) = matrix (3*2)
C = np.array([[1,4,3], [4,5,6], [7,8,9]]);
D = np.array([[0,1], [3,4], [6,7]]);
print(np.dot(C,D));

#Vector(1*3) cross multiplication Vector(1*3) = Vector (1*3). Dimension must be 2 or 3
M = np.array([7,8,9]);
N = np.array([1,2,3]);
print (np.cross(M,N));

#trace matrix diagonal (sum of matrix diagonal)
print(np.trace(C));

#transpose matrix
print(np.transpose(C));

# Matrix Determinan
print(np.linalg.det(C)); #Matrix Singular cuz the determinant result is 0.0

# Matrix Inversion
print(np.linalg.inv(C));

#Constant Matrix
F = np.ones((4,4));
print(F); # Matrix 4 * 4 dimensional, full of 1
G = np.full((4,4),3);
print(G); # Matrix 4*4 dimensional, full of 3
O= np.zeros((4,4));
print(O); # Matrix 4*4 dimensional, full of 0

#Diagonal Matrix
H = np.diag([2,3,1,4]);
print(H);

#Identity Matrix
I = np.eye(5);
print(I);

#Rank Matrix
print(np.linalg.matrix_rank(C));


# In[ ]:




