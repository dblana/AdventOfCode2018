# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:12:15 2018

@author: dimitra
"""

import re
import numpy as np

patches =[]

#line = '##1 @ 236,827: 24x17'

with open('day3_input.txt') as f:
    for line in f:
        numbers = re.findall(r"[0-9']+", line)
        patches.append([int(i) for i in numbers])

width = 0
height = 0
for claim in patches:
    width = max(width, claim[1]+claim[3])
    height = max(height, claim[2]+claim[4])

fabric = np.zeros((width,height))

# Part 1

candidates=[]

for claim in patches:
    if np.all(fabric[claim[1]:claim[1]+claim[3],claim[2]:claim[2]+claim[4]]==0):
        candidates.append(claim[0])
    fabric[claim[1]:claim[1]+claim[3],claim[2]:claim[2]+claim[4]]+=1

print(np.count_nonzero(fabric>1))

# Part 2

for claim_num in candidates:
    claim = patches[claim_num-1]
    if np.all(fabric[claim[1]:claim[1]+claim[3],claim[2]:claim[2]+claim[4]]==1):
        print(claim_num)
        break

