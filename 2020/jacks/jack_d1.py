# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:31:04 2020

@author: Jack McDonough 
Solutions for the first day of Advent of Code 
"""
stars_list = []
go = False
target = 2020
answer = None
with open('aoc_challenge_1_2020.txt','r') as f:
    for line in f:
       stars_list.append(int(line))

'''
two loop solution for first puzzle 
'''
# for i in stars_list:
#       if go:
#            break
#       for j in stars_list:
#           if i + j == 2020:
#               print(i,j)
#               go = True
#               answer = i*j 
#               break

'''
one loop and difference solution for first puzzle
'''
for i in stars_list:
     j = target - i
     if j in stars_list:
         answer = (j,i,i * j)
         print(answer)
         break
  
'''
three loop solution for second puzzle
'''
# for i in stars_list:
#     if go:
#         break
#     for j in stars_list:
#         if go:
#             break
#         for k in stars_list:
#             if i + j + k == target:
#                 answer = (i,j,k,i * j * k)
#                 go = True

'''
two loop solution for second puzzle
'''
answer = None
for i in stars_list:
    if answer:
        break
    for j in stars_list:
        if i != j:
            k = target - i - j
            if k in stars_list:
                answer = (i,j,k,i * j * k)
                print(answer)
                break
            
        if answer:
            break
