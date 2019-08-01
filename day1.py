# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:05:25 2018

@author: dimitra
"""

file = 'day1_input.txt'

lines = open(file).read().splitlines()


# Part 1
one_line = ''.join(lines)
print(eval(one_line))

# Part 2
frequencies = []
len_lines = len(lines)

current_freq = 0
index = 0
while current_freq not in frequencies:
    frequencies.append(current_freq)
    current_freq += int(lines[index])
    index +=1
    if index == len_lines:
        index=0
