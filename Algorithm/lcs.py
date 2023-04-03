#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 hp_carrot.com, Inc. All Rights Reserved
#
########################################################################

"""
File: /home/luban/daVinci/Algorithm/lcs.py
Author: hanjiatong@hp_carrot.com
Date: 2019/05/21 18:11:57
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
import numpy as np

def get_lcs_pos_lst(s, lcs):
    s1_lcs_pos_lst = []
    last_pos = 0
    for i, char in enumerate(s):
        if char == lcs[last_pos]:
            s1_lcs_pos_lst.append(i)
            last_pos += 1
    return s1_lcs_pos_lst

def char_order(a1, a2):
    if a1 < a2:
        return 1
    elif a1 == a2:
        return 0
    else:
        return -1

def concatenate_using_orderfunc(slst, order_func=char_order):
    """ concatenate all slst using order, that each element count and will find a position."""
    pos_lst = np.zeros(len(slst), np.int32)
    concat_s = []
    end_cnt = 0
    start_char = slst[0][pos_lst[0]]
    start_s_idx = 0

    while end_cnt < len(slst):
        while pos_lst[start_s_idx] >= len(slst[start_s_idx]):
            start_s_idx += 1
        cur_s_idx = start_s_idx
        start_char = slst[cur_s_idx][pos_lst[cur_s_idx]]
        for i in range(len(slst)):
            if pos_lst[i] >= len(slst[i]):
                continue
            order_rslt = order_func(slst[i][pos_lst[i]], start_char)
            if order_rslt > 0:
#print('replace before', start_char, slst[i][pos_lst[i]])
                start_char = slst[i][pos_lst[i]]
#print('replace', start_char, slst[i][pos_lst[i]])
                cur_s_idx = i
#print(start_char, slst[cur_s_idx][pos_lst[cur_s_idx]], cur_s_idx, pos_lst[cur_s_idx])
        concat_s.append(start_char)
        pos_lst[cur_s_idx] += 1
        if pos_lst[cur_s_idx] == len(slst[cur_s_idx]):
            end_cnt += 1
        for i in range(len(slst)):
            if i != cur_s_idx and pos_lst[i] < len(slst[i]):
                if slst[i][pos_lst[i]] == start_char:
                    pos_lst[i] += 1
                    if pos_lst[i] == len(slst[i]):
                        end_cnt += 1
    return concat_s

def find_lcseque(s1, s2):
	 # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
	m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]
	# d用来记录转移方向
	d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]

	for p1 in range(len(s1)):
		for p2 in range(len(s2)):
			if s1[p1] == s2[p2]:            #字符匹配成功，则该位置的值为左上方的值加1
				m[p1+1][p2+1] = m[p1][p2]+1
				d[p1+1][p2+1] = 'ok'
			elif m[p1+1][p2] > m[p1][p2+1]:  #左值大于上值，则该位置的值为左值，并标记回溯时的方向
				m[p1+1][p2+1] = m[p1+1][p2]
				d[p1+1][p2+1] = 'left'
			else:                           #上值大于左值，则该位置的值为上值，并标记方向up
				m[p1+1][p2+1] = m[p1][p2+1]
				d[p1+1][p2+1] = 'up'
	(p1, p2) = (len(s1), len(s2))
	#print numpy.array(d)
	s = []
	while m[p1][p2]:    #不为None时
		c = d[p1][p2]
		if c == 'ok':   #匹配成功，插入该字符，并向左上角找下一个
			s.append(s1[p1-1])
			p1-=1
			p2-=1
		if c =='left':  #根据标记，向左找下一个
			p2 -= 1
		if c == 'up':   #根据标记，向上找下一个
			p1 -= 1
	s.reverse()
	return s

def test():
	print find_lcseque('abdfg','abcdfg')

def test_concate():
    print('abdfg','abcdfg', 'aammmbd')
    print(concatenate_using_orderfunc(['abdfg','abcdfg', 'abd', 'abdfg', 'aammmbd']))

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

