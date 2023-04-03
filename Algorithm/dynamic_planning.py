#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2019 hp_carrot.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: Algorithm/dynamic_planning.py
Author: hanjiatong@hp_carrot.com
Date: 2019/08/01 21:44:37
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
import numpy as np

def min_cost_AB_lst_wise_baseonA(lstA, lstB, cost_function):
  cA = len(lstA)
  cB = len(lstB)
  min_cost_arr = np.zeros((cA, cB))
  for i in range(cA):
    for j in range(cB):
      min_cost_arr[i][j] = np.Infinity

  matching = {}
  for i in range(cA):
    matching[i] = {}
    for j in range(cB):
      min_cost = np.Infinity
      if i == 0 and j == 0:
        min_cost = cost_function(lstA[i], lstB[j])
        min_cost_arr[i][j] = min_cost
        matching[i][j] = i
      elif i == 0:
        min_cost_arr[i][j] = np.Infinity
        matching[i][j] = None
      elif j == 0:
        min_cost = cost_function(lstA[i], lstB[j])
        if min_cost < min_cost_arr[i][j]:
          min_cost_arr[i][j] = min_cost
          matching[i][j] = i
        if min_cost_arr[i-1][j] < min_cost:
          min_cost = min_cost_arr[i-1][j]
          matching[i][j] = matching[i-1][j]
          min_cost_arr[i][j] = min_cost
      else:
        if min_cost_arr[i-1][j] < min_cost:
          min_cost = min_cost_arr[i-1][j]
          matching[i][j] = matching[i-1][j]
        matching_cost = min_cost_arr[i-1][j-1] + cost_function(lstA[i], lstB[j])
        if matching_cost < min_cost:
          min_cost = matching_cost
          matching[i][j] = i
        min_cost_arr[i][j] = min_cost
  return min_cost_arr, matching

def cost(A, B):
  return abs(A - B)

def test_min_cost_AB_lst_wise_baseonA(lstA, lstB):
  min_cost_arr, matching = min_cost_AB_lst_wise_baseonA(lstA, lstB, cost)
  print(lstA)
  print(lstB)
  print(min_cost_arr)
  print(matching)

def testA():
  lstA = [1, 3, 7, 100]
  lstB = [3, 8, 50]
  test_min_cost_AB_lst_wise_baseonA(lstA, lstB)

def testB():
  lstA = [1, 3, 7, 100]
  lstB = [3, 8, 60]
  test_min_cost_AB_lst_wise_baseonA(lstA, lstB)

if __name__ == "__main__":
  import inspect, sys
  current_module = sys.modules[__name__]
  funnamelst = [item[0] for item in inspect.getmembers(current_module, inspect.isfunction)]
  if len(sys.argv) > 1:
      index = 1
      while index < len(sys.argv):
          if '--' in sys.argv[index]:
              index += 2
          else:
              break
      func = getattr(sys.modules[__name__], sys.argv[index])
      func(*sys.argv[index+1:])
  else:
      print >> sys.stderr, '	'.join((__file__, "/".join(funnamelst), "args"))

