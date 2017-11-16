#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:59:32 2017

@author: kunal
"""
import numpy as np
"""
A simple class that contains functions to create random_projections matrix and compute projected matrix S
This class takes the mode to create random_projections as a parameter and a value epsilon depending on
which it determines the maxmium number of dimensions required for the projected matrix to be compliant with
JL-Lemma
"""
class Random_Projection:
    """
    There are 3 different modes for computation
    1 - returns a matrix containing vectors drawn from a N(0, 1) distribution
    2 - returns a matrix containing values (-1, +1) with P(0.5, 0.5)
    3 - returns a matrix containing values(-1, 0, +1) with P(0.16, 0.68, 0.16)
    """
    def __init__(self, mode, eps, dim):
        self.mode = mode
        self.eps = eps
        self.dim = dim
        
    """
    Returns a simple matrix of dimensions dim*k where the vectors contain values drawn from N(0, 1)
    Args: 
            dim - # of features in data
            k - #desired number of features
    Returns:
            numpy array/matrix
    """  
    def random_projection_with_normal(dim, k):
        #Reshape this into a matrix with dim-rows and k-columns
        projection_matrix = np.random.normal(0, 1, dim*k).reshape((dim, k))
        return projection_matrix
    
    """
    Returns a simple matrix of dimensions dim*k where the vectors contain values -1, 1 chosen with equal 
    probability
    Args: 
            dim - # of features in data
            k - #desired number of features
    Returns:
            numpy array/matrix
    """
    def random_projection_sparse_1(dim, k):
        projection_matrix = np.random.choice([-1, 1], size=dim*k, replace=True).reshape((dim, k))
        return projection_matrix
    
    """
    Returns a simple matrix of dimensions dim*k where the vectors contain values -1, 0, 1 chosen with
    probabilities [1/6, 2/3, 1/6]
    Args: 
            dim - # of features in data
            k - #desired number of features
    Returns:
            numpy array/matrix
    """   
    def random_projection_sparse_2(dim, k):
        projection_matrix = np.random.choice([-1, 0, 1], size=dim*k, replace=True, p=[1/6, 2/3, 1/6])
        projection_matrix = projection_matrix.reshape((dim, k))
        return projection_matrix
    
    """
    Returns an array of reduced dimensions
    Args:
            A - Feature matrix
            p - projection matrix
            
    Returns:
            a numpy array of dimension n*k where n is the number of samples and k is the reduced number of
            features required.
    """
    def reduce_dimension_standard(A, p):
        return A.dot(p)
    
    """
    Returns an array of reduced dimensions. This contains bit vectors where the value is 1 at places the
    dot product value is positive.
    Args:
            A - Feature matrix
            p - projection matrix
            
    Returns:
            a numpy array of dimension n*k where n is the number of samples and k is the reduced number of
            features required.
            
    Todo:
            Check is bitarray could be used instead of numpy array in this case. We'll end up using 
            even lesser space!!!
    """
    def reduce_dimension_signed(A, p):
        projected_matrix = []
        for document in A:
            res = []
            for ran_vec in p:
                ip = document.dot(ran_vec)
                if(ip >= 0):
                    res.append(1)
                else:
                    res.append(0)
            projected_matrix.append(np.asarray(res))
        return np.asarray(projected_matrix)
        