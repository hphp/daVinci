#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2018 hp_carrot.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: daVinci/Algorithm/bfs.py
Author: hanjiatong@hp_carrot.com
Date: 2018/03/29 00:17:44
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
 
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

