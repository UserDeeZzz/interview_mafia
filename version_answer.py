#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: deez
@file: version_answer.py
@time: 2020/3/20
"""

from itertools import zip_longest

def diff_version(v1,v2):

    handled_v1 = [int(v) for v in v1.split('.')]
    handled_v2 = [int(v) for v in v2.split('.')]
    for i,j in zip_longest(handled_v1,handled_v2,fillvalue=0):
        if i > j :
            return 1
        elif i< j:
            return -1
    return 0

if __name__ == '__main__':
    assert diff_version('0.1','1.1') == -1
    assert diff_version('1.0.1','1') == 1
    assert diff_version('7.5.2.4','7.5.3') == -1
    assert diff_version('1.01','1.001') == 0
    assert diff_version('1.0','1.0.0') == 0
    print("success")