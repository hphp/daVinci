#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: /home/users/hanjiatong/daVinci/Algorithm/mth.py
Author: hanjiatong(hanjiatong@)
Date: 2017/12/12 17:46:48
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
import numpy as np
import math

def quadratic_equation(a, b, c, x):
    return a*x*x + b*x + c

def linear_equation(a, b, x):
    return a*x + b

def linear_y_by_equation(equation, x):
    a, b = equation
    return linear_equation(a, b, x)

import scipy.optimize
def sci_quadratic(a, b, c, y):
    return scipy.optimize.fsolve(lambda x: a*x**2 + b*x + c-y, x0=270)

def sci_linear_by_equation(equation, y):
    a, b = equation
    return scipy.optimize.fsolve(lambda x: a*x + b - y, 0)

def sci_linear(a, b, y):
    return scipy.optimize.fsolve(lambda x: a*x + b - y, 0)
#import sympy
#print(sympy.solve('x**2 + 2*x + 1'))

def simple_quadratic(a, b, c, y):
    return sci_quadratic(a, b, c, y)

def test_linear():
    x = sci_linear(1, 3, 0)
    y = linear_equation(1, 3, x[0])
    print(x, y)

def test_quadratic():
    x = sci_quadratic(1, 3, -4, 0)
    y = quadratic_equation(1, 3, -4, x[0])
    print('simple', x, y)
    x = sci_quadratic(1, 3, 0, 4)
    y = quadratic_equation(1, 3, 0, x[0])
    print('convert_simple', x, y)
    x = sci_quadratic(0.00018603518281245, -0.32579516303101785, 370.228573080556, 358.52187093098956)
    print('sci_quadratic_x', x)
    y = quadratic_equation(0.00018603518281245, -0.32579516303101785, 370.228573080556, x[0])
    print('sci_quadratic_y', y)


    x = sci_quadratic(-0.00023886989140270917, -0.6135094803705541, 594.4693885315477, 358.52187093098956)
    print('sci_quadratic_x', x)
    y = quadratic_equation(-0.00023886989140270917, -0.6135094803705541, 594.4693885315477, x[0])
    print('sci_quadratic_y', y)

    x = sci_quadratic(-0.005154998875102689, 2.897626351062985, 193.8636846553545, 259)
    print('sci_quadratic_x', x)
    y = quadratic_equation(-0.005154998875102689, 2.897626351062985, 193.8636846553545, x[0])
    print('sci_quadratic_y', y)
    y = quadratic_equation(-0.005154998875102689, 2.897626351062985, 193.8636846553545, 530)
    print('sci_quadratic_y', y)

def GeneralEquationLine(xy1, xy2):
    first_x, first_y = xy1
    second_x, second_y = xy2
    # 一般式 Ax+By+C=0
    A = second_y-first_y
    B = first_x-second_x
    C = second_x*first_y-first_x*second_y
    return A,B,C

def GetIntersectPointofGenLines(Line1, Line2):
    A1, B1, C1 = Line1
    A2, B2, C2 = Line2
    m=A1*B2-A2*B1
    if m==0:
        return None
    else:
        x=(C2*B1-C1*B2)/m
        y=(C1*A2-C2*A1)/m
    return x,y

def GetIntersectPoints(x1,y1,x2,y2,x3,y3,x4,y4):
    Line1 =GeneralEquation(x1,y1,x2,y2)
    Line2 = GeneralEquation(x3,y3,x4,y4)
    return GetIntersectPointofGenLines(Line1, Line2)

def getline_by_parallelgenline_and_point(parallel_line, xy):
    A, B, C = parallel_line
    x0, y0 = xy
    pA, pB = [A, B]
    pC = - (A*x0 + B*y0)
    return [pA, pB, pC]

def fitline_by_points_k(k, xy):
    x0, y0 = xy
    A = k
    B = -k*x0 + y0
    return [A, B]

def y_of_line(line, x):
    A, B = line
    return A*x+B

def TranPointSlopToGeneral(LinePS):
    k, b = LinePS
    return [k, -1, b]

def fitline(x, y):
    from scipy.optimize import curve_fit
    def f(x, A, B): # this is your 'straight line' y=f(x)
        return A*x + B
    A,B = curve_fit(f, x, y)[0] # your data x, y to fit
    return [A, B]

def testfitline():
    x = [1, 2, 3]
    y = [31, 39, 50]
    A, B = fitline(x, y)
    print(A, B)

def points_projects_to_line(xy, line):
    x0, y0 = xy
    m, b = line
    x1 = (m*y0+x0-m*b)/(m*m+1);
    y1 = (m*m*y0+m*x0+b)/(m*m+1);
    return [x1, y1]

def calEuclideanDistance(vec1,vec2):
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)
    dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return dist

def MSE(A, B, axis=1):
    mse = ((A - B) ** 2).mean(axis=axis)
    return mse

def stupid_softmax(x):
    """Compute the softmax of vector x."""
    exp_x = np.exp(x)
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x

def simple_softmax(x):
    """Compute the softmax in a numerically stable way."""
    x = x - np.max(x)
    exp_x = np.exp(x)
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x

def softmax(x):
    """
    Compute the softmax function for each row of the input x.

    Arguments:
    x -- A N dimensional vector or M x N dimensional np matrix.

    Return:
    x -- You are allowed to modify x in-place
    """
    orig_shape = x.shape
    if len(x.shape) > 1:
        # Matrix
        exp_minmax = lambda x: np.exp(x - np.max(x))
        denom = lambda x: 1.0 / np.sum(x)
        x = np.apply_along_axis(exp_minmax,1,x)
        denominator = np.apply_along_axis(denom,1,x) 
        
        if len(denominator.shape) == 1:
            denominator = denominator.reshape((denominator.shape[0],1))
        
        x = x * denominator
    else:
        # Vector
        x_max = np.max(x)
        x = x - x_max
        numerator = np.exp(x)
        denominator =  1.0 / np.sum(numerator)
        x = numerator.dot(denominator)
    assert x.shape == orig_shape
    return x

def segment_center(PA, PB):
    center = []
    for A, B in zip(PA, PB):
        center.append((A+B)/2.)

    return center

def segment_distance(SA, SB):
    c1 = segment_center(SA[0], SA[1])
    c2 = segment_center(SB[0], SB[1])
    return distance(c1, c2)

def distance(v1, v2):
    dist = np.linalg.norm(np.asarray(v1) - np.asarray(v2))
    return dist
    import math
    sumxx = 0
    sumyy = 0
    sumxy = 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return math.sqrt(sumxx*sumyy)

def simple_cosine(v1, v2):
    import math
    sumxx = 0
    sumyy = 0
    sumxy = 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def cosine(a, b):
    from scipy import linalg, mat, dot
    return dot(a,b.T)/linalg.norm(a)/linalg.norm(b)

def expand2size(single_arr, expand_size):
    expand_arr = np.zeros(tuple([expand_size]) + tuple(single_arr.shape))
    for j in range(expand_size):
        expand_arr[j] = np.asarray(single_arr, np.float32)
    return expand_arr

def cntsystem_sparse2dense(sparse_arr, dense_sparse_matrix):
    """all arr is one-hot."""
    dense_arr = np.zeros((sparse_arr.shape[0], dense_sparse_matrix.shape[0]))
    for denseidx in range(dense_sparse_matrix.shape[0]):
        sparseidx = np.argmax(dense_sparse_matrix[denseidx])
        sparseidx_pos = np.where(np.argmax(sparse_arr, axis=1) == sparseidx)
        for pos in sparseidx_pos[0]:
            dense_arr[pos][denseidx] = 1
    return dense_arr

def test_cntsystem_sparse2dense():
    sparse_arr = np.zeros((3, 6))
    sparse_arr[0][5] = 1
    sparse_arr[1][2] = 1
    sparse_arr[2][2] = 1
    dense_sparse_matrix = np.zeros((2, 6)) # 2->0, 5->1
    dense_sparse_matrix[0][2] = 1
    dense_sparse_matrix[1][5] = 1
    dense_arr = cntsystem_sparse2dense(sparse_arr, dense_sparse_matrix)
    print('dense_arr', dense_arr)
# expect : [ [ 0, 1], [1, 0] , [ 1, 0]]

def test_softmax():
    a = np.arange(10)
    print(softmax(a))

if __name__ == "__main__":
    import inspect, sys
    current_module = sys.modules[__name__]
    funnamelst = [item[0] for item in inspect.getmembers(current_module, inspect.isfunction)]
    if len(sys.argv) > 1:
        func = getattr(sys.modules[__name__], sys.argv[1])
        func(*sys.argv[2:])
    else:
        print >> sys.stderr, '    '.join((__file__, "/".join(funnamelst), "args"))

