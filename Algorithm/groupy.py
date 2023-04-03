#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2019 hp_carrot.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: Algorithm/groupy.py
Author: hanjiatong@hp_carrot.com
Date: 2019/08/27 14:50:56
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))

def lst_of_number(lst, min_groupup_sum=200):
  """
    args: lst(of numbers.)
    return: groupid_center_dic
      groupid_centerinfo_dic == {groupid: {'centeridx': centeridx, 'groupsum': groupsum}
    algorithm:
      1. loop to get all groupid_lst;
      2. center of groupid_indexes_dic
  """
  length = len(lst)
  groupid = 0
  groupid_indexes_dic = {}
  groupid_centeridx_dic = {}
  last_status = False
  for i in range(length):
    if not last_status:
      if lst[i] == 0:
        pass
      else:
        groupid_indexes_dic[groupid] = []
        groupid_indexes_dic[groupid].append(i)
    else:
      if lst[i] > 0:
        groupid_indexes_dic[groupid].append(i)
      else:
        groupid += 1
    last_status = lst[i] > 0

  new_groupid = 0
  newgroupid_centerinfo_dic= {}
  for groupid in sorted(groupid_indexes_dic.keys()):
    group_sum = sum([lst[i] for i in groupid_indexes_dic[groupid]])
    if group_sum < min_groupup_sum:
      continue
    else:
      temp_sum = 0
      i = 0
      for i in groupid_indexes_dic[groupid]:
        temp_sum += lst[i]
        if temp_sum >= group_sum / 2. or abs(temp_sum - group_sum/2.) < 0.1*group_sum/2.:
          break
      newgroupid_centerinfo_dic[new_groupid] = {'centeridx': i, 'groupsum': group_sum, 'startidx': groupid_indexes_dic[groupid][0], 'endidx': groupid_indexes_dic[groupid][-1]}
      new_groupid += 1

  return newgroupid_centerinfo_dic

def test_lst_of_number():
  A = [0, 0, 1, 2, 4, 0, 0, 8, 9, 0, 19, 0, 20, 300]
  print(lst_of_number(A, 10))
  A = [0, 0, 1, 2, 0, 100, 200, 300, 400, 0, 4, 0, 0, 8, 9, 0, 19, 0, 20, 300]
  print(lst_of_number(A, 10))

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

