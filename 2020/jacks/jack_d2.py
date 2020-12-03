# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:49:39 2020

@author: jackm
"""
'''
constants and list for data write in
'''
puzzle_data = []
ANSWER = 0
with open('aoc_challenge_2_2020.txt','r') as f :
    for line in f:
        puzzle_data.append(line)

'''
tokenization of date
'''
for line in puzzle_data:
    tokens = line.split()
    ranges = tokens[0]
    letter = tokens[1][0]
    password = tokens[2]
    min_occur = int(ranges.split('-')[0])
    max_occur = int(ranges.split('-')[1])
    COUNT_OCCUR = 0

    for i in password:
        if i == letter:
            COUNT_OCCUR += 1

    if min_occur <= COUNT_OCCUR <= max_occur:
        ANSWER  += 1
    
#    if password[min_occur-1] == letter or password[max_occur - 1] == letter:
#        if password[min_occur-1] != password[max_occur - 1]:
#            ANSWER += 1

print(ANSWER)