# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:31:24 2018

@author: dimitra
"""

file = 'day2_input.txt'
lines = open(file).read().splitlines()

# Part 1

def count_letters(string):
    '''It counts how many times each letter appears in a string'''
    letters = {}
    for letter in string:
        if letter in letters:
            letters[letter]+=1
        else:
            letters[letter]=1    
    return letters

twice = 0
threetimes = 0

for line in lines:
    letters = count_letters(line)
    if 2 in letters.values():
        twice +=1
    if 3 in letters.values():
        threetimes +=1

print(twice * threetimes)

# Part 2

def differ_by_one(string1, string2,length):
    '''If two strings only differ by one character, returns True'''
    
    if string1 == string2:
        return False
    diff=0
    for index in range(length):
        if string1[index] != string2[index]:
            diff+=1
        if diff>1:
            return False
    return True

length = len(lines[0])

for index1 in range(len(lines)-1):
    for index2 in range(index1+1,len(lines)):
        if differ_by_one(lines[index1],lines[index2],length):
            print(lines[index1])
            print(lines[index2])
            break
        else:
            continue
        break
    
