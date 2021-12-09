#########################################################################
# File Name: re.py
# Author: Walker
# mail:qngskk@gmail.com
# Created Time: Thu Dec  9 15:45:02 2021
#########################################################################
# !/usr/bin/env python3

import re

lines = []
with open('./dc31-space.dat', 'r') as fr:
    while cur_line := fr.readline():
        cur_line = cur_line.replace('\n', '')
        cur_line = re.split(r' +', cur_line)
        cur_line[1] = str(float(cur_line[1]) + 5e5)
        cur_line[2] = str(float(cur_line[2]) - 396e4)
        lines.append(cur_line)

with open('./res.dat', 'w+') as fw:
    for line in lines:
        fw.write(' '.join(line)+'\n')
