#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2018 hp_carrot.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: daVinci/Algorithm/match.py
Author: hanjiatong@hp_carrot.com
Date: 2018/10/27 18:15:20
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
import numpy as np

def get_tag_pairs(tag_fpath):
    dic = {}
    for line in open(tag_fpath, 'r+'):
        line = line.strip()
        if len(line) < 2:
            continue
        if len(line.strip().split('\t')) != 2:
            print('line', line, line.strip().split('\t'))
        k, tag = line.strip().split('\t')
        dic[k] = tag
    return dic

def query_std_tag(k_tag_dic, std_tag_dic):
    query_stdtag_dic = {}
    for k in k_tag_dic:
        if k in std_tag_dic:
            query_stdtag_dic[k] = std_tag_dic[k]
    return query_stdtag_dic

def query_tag_arr(k_tag_dic, query_stdtag_dic):
    tag_arr = np.unique(np.asarray([ query_stdtag_dic[k] for k in k_tag_dic if k in query_stdtag_dic]))
    return tag_arr

def ac_mean_by_tag(tag_fpath, std_tag_fpath):
    k_tag_dic = get_tag_pairs(tag_fpath)
    std_tag_dic = get_tag_pairs(std_tag_fpath)
    query_stdtag_dic = query_std_tag(k_tag_dic, std_tag_dic)

    tag_whole_ac = 0
    tag_arr = query_tag_arr(k_tag_dic, query_stdtag_dic)
    for tag in tag_arr:
        tag_correct = 0
        tag_total = 0
        for k in k_tag_dic:
            if query_stdtag_dic[k] == tag:
                tag_total += 1
                if k_tag_dic[k] == tag:
                    tag_correct += 1
        tag_ac = tag_correct * 100. / tag_total
        tag_whole_ac += tag_ac
    return tag_whole_ac / tag_arr.shape[0]

def tag_klst_dic_by_k_tag(k_tag_dic):
    tag_klst_dic = {}
    for k in k_tag_dic:
        tag = k_tag_dic[k]
        if tag not in tag_klst_dic:
            tag_klst_dic[tag] = []
        tag_klst_dic[tag].append(k)
    return tag_klst_dic

def tag_performance_at_alltag(k_tag_dic, std_tag_dic):
    query_stdtag_dic = query_std_tag(k_tag_dic, std_tag_dic)
    query_stdtag_arr = query_tag_arr(k_tag_dic, query_stdtag_dic)
    tag_klst_dic = tag_klst_dic_by_k_tag(k_tag_dic)
    stdtag_klst_dic = tag_klst_dic_by_k_tag(query_stdtag_dic)

    stdtag_predicttag_cnt_dic = {}
    for stdtag in stdtag_klst_dic:
        supposed_k_cnt = len(stdtag_klst_dic[stdtag])
        stdtag_predicttag_cnt_dic[stdtag] = {}
        for tag in query_stdtag_arr:
            stdtag_predicttag_cnt_dic[stdtag][tag] = 0
        for supposed_k in stdtag_klst_dic[stdtag]:
            predicttag = k_tag_dic[supposed_k]
            if predicttag not in stdtag_predicttag_cnt_dic[stdtag]:
                stdtag_predicttag_cnt_dic[stdtag][predicttag] = 0
            stdtag_predicttag_cnt_dic[stdtag][predicttag] += 1

    return stdtag_predicttag_cnt_dic

def show_tag_performance_at_alltag(tag_fpath, std_tag_fpath):
    import relation

    k_tag_dic = get_tag_pairs(tag_fpath)
    std_tag_dic = get_tag_pairs(std_tag_fpath)
    query_stdtag_dic = query_std_tag(k_tag_dic, std_tag_dic)
    stdtag_klst_dic = tag_klst_dic_by_k_tag(query_stdtag_dic)
    query_stdtag_arr = query_tag_arr(k_tag_dic, query_stdtag_dic)
    stdtag_predicttag_cnt_dic = tag_performance_at_alltag(k_tag_dic, std_tag_dic)
    stdtag_lst = [item[0] for item in sorted(stdtag_klst_dic.items(), key=lambda ele: len(ele[1]), reverse=True) if len(stdtag_klst_dic[item[0]]) > 0]
    show_stdtag_lst = [ relation.init_label_name.c285label_name_dic[label] for label in stdtag_lst]
    print('\t'.join(['value'] + show_stdtag_lst))
    for stdtag in stdtag_lst:
        r = []
        for predicttag in stdtag_lst:
            r.append(stdtag_predicttag_cnt_dic[stdtag][predicttag])
        print('\t'.join([relation.init_label_name.c285label_name_dic[stdtag] + "_"+str(len(stdtag_klst_dic[stdtag]))] + [str(v) for v in r]))

def count_correct_tag(tag_fpath, std_tag_fpath):
    k_tag_dic = get_tag_pairs(tag_fpath)
    std_tag_dic = get_tag_pairs(std_tag_fpath)
    correct = 0
    total = len(k_tag_dic)
    for k in k_tag_dic:
        if k in std_tag_dic and std_tag_dic[k] == k_tag_dic[k]:
            correct += 1
    return correct, total

def show_ac_mean_by_tag(tag_fpath, std_tag_fpath):
    print(ac_mean_by_tag(tag_fpath, std_tag_fpath))

def show_correct_tag_cnt(tag_fpath, std_tag_fpath):
    correct, total = count_correct_tag(tag_fpath, std_tag_fpath)
    print(correct, total, correct * 100. / total)

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

