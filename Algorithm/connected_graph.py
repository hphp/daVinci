#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: connected_graph.py
Author: hanjiatong(hanjiatong@)
Date: 2016/12/26 13:42:58
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))

dot_lst = ["A", "B", "C", "D", "E", "F", "G"]
connected = {"A":["F"], "F": ["G"], "B":["C", "D"], "C":["D"], "D":["D"]}

label_dic = {}
def label(dot, LABEL):
    if dot in label_dic:
        return
    label_dic[dot] = LABEL
    if dot in connected:
        for connected_dot in connected[dot]:
            label(connected_dot, LABEL)

if __name__ == "__main__":
    LABEL = 0
    for dot in dot_lst:
        label(dot, LABEL)
        LABEL += 1

    for dot in label_dic:
        print dot, label_dic[dot]
