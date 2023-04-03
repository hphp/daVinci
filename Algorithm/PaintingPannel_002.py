#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2018 hp_carrot.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: Algorithm/PaintingPannel_002.py
Author: hanjiatong@hp_carrot.com
Date: 2018/03/05 18:20:50
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
"""
一块长长的白色板子长B unit（B<16000)，你有K（<100)支彩笔，彩笔 i 最多可以涂连续的Li
unit，如果使用该彩笔，则必须要覆盖到某个特殊位置Si，每一个uniq最多被一只彩笔涂上
求这些彩笔可以覆盖板子最长的长度有多少unit
主要考察：是否理解题意、是否合理设计建模、书写是否流畅、边界条件是否考虑周全
"""
def max_painted(PenInfoLst, BLength):
    """
        define Pen{
            PaintLength
            NessSpot
        }
        NessSpot range in [1, BLength]
    """
    PenInfo = sorted(PenInfoLst.item(), key = lambda ele: ele.NessSpot)

    pen_count = len(PenInfo)
    import numpy as np
    max_painted = np.zeros((pen_count+1, BLength+1))
    for i, item in enumerate(PenInfo):
        """
        """
        idx = i+1
        paintlength = item[1]
        nessspot = item[2]
        cant_reach_max = max(nessspot - paintlength, 0)
        could_reach_max = min(nessspot + paintlength - 1, BLength+1)
        for spot in range(0, nessspot):
            max_painted[idx][spot] = max_painted[idx-1][spot]
        for spot in range(nessspot, could_reach_max):
            max_painted[idx][spot] = max_painted[idx][spot-1]
            this_spot_cant_reach_max = max(spot - paintlength, 0)
            for last_spot in range(this_spot_cant_reach_max, spot):
                max_painted[idx][spot] = max(max_painted[idx][last_spot], max_painted[idx-1][spot-1] + 1)
 
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

