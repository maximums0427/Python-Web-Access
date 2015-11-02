# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 21:52:17 2015

@author: xiaoqin
"""
name = 'mbox-short.txt'
handle = open(name)

base=dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        key_1 = re.findall(' ([0-9]+):',line)
        #print key_1[0]
        #buf.append(key_1)
        base[key_1[0]] = base.get(key_1[0],0)+1
buf = base.items()
buf.sort()
for month,num in buf:
    print month,num
