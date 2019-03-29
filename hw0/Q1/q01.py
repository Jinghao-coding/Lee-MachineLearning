# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:52:35 2019

@author: JingHao
"""

import numpy as np

with open("data/matrixA.txt", "r") as lines:
    matrixA = lines.readline().split(",")
    matrixA = list(map(int,matrixA))
    
with open("data/matrixB.txt", "r") as lines:
    matrixB = lines.readlines()
    matrixB = [item.strip().split(',') for item in matrixB]
    matrixB = [list(map(int, item)) for item in matrixB]
    #print(matrixB)
        
A = np.array(matrixA)
B = np.array(matrixB)

#print(A,A.shape)
#print(B,B.shape)
C = A.dot(B)
C = np.sort(C)
np.savetxt("ans_one.txt", C, fmt="%d")
print("Success!") 