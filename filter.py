# -*- coding: utf-8 -*-
"""
Name: Bar Dalal
Class: Ya4
"""

import numpy as np


def FindResult(arr, Filter):
    """
    The function gets two square matrices: the one consists of float positive numbers and the other (filter) is 3X3 (from 0.0 to 5.0)
    The function returns a matrix which contains the scalar multiplications of the filter and a 3X3 slice from the given matrix
    """
    result= np.zeros([arr.shape[0]-2, arr.shape[1]-2], dtype= float) # the matrix to return
    for line in range (arr.shape[0] - 2): # pass over the lines
        for column in range (arr.shape[1] - 2): # pass over the columns  
            c= arr[line :line + 3, column :column + 3] # a 3X3 slice from the given matrix
            result[line, column]= Calc(c, Filter) # put the scalar multiplication in the suitable place   
    return result


def Calc(c, Filter):
    """
    The function gets a 3X3 slice from a matrix and other 3X3 matrix (filter)
    The function returns their scalar multiplication
    """
    scalar= 0 # the scalar multiplication
    for x in range (3):
        lineC = c[x:x+1][0] # a line from the slice
        lineF= Filter[x:x+1][0] # a line fron the filter
        scalar= scalar + np.dot(lineC, lineF) # scalar multiplication of two lines- one from each matrix 
    return scalar
    

def main():
    arr= np.array([[1, 0, 1, 1, 0, 2, 1, 4], [1, 3, 1, 2, 0, 0, 1, 0],
                  [1.5, 3, 0, 2.8, 0, 0.4, 7, 1], [6, 0, 0, 4, 0, 1, 0, 0], 
                  [10, 3, 1, 20, 0, 0, 4, 0], [2, 2, 2, 2, 0, 0, 2, 0],
                  [1.75, 3.25, 1, 2, 0, 0, 1, 0.2], [0.1, 3.1, 1.1, 2.1, 0, 0, 1.5, 0]]) # 8X8 matrix
    Filter= np.random.rand(3, 3) # 3X3 matrix which contains random float numbers from 0.0 to 1.0
    print ("arr: ", arr)
    print ("Filter: ", Filter)
    while arr.shape[0] >= Filter.shape[0] and arr.shape[1] >= Filter.shape[1]:
        arr= FindResult(arr, Filter)
        print ("the result is: " , arr)
        Filter= np.random.rand(3, 3) # 3X3 matrix which contains random float numbers from 0.0 to 1.0
        print ("Filter: ", Filter)
   
 
if __name__ == "__main__":
    main()
