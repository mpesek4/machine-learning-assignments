# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:16:16 2017

@author: Michael
"""

import sys
from sets import Set


s = ["AA", "AB", "ABD", "ABDE", "ABC"]
# your code goes here
a= Set()
b= Set()
i = 0
max_index = 0
last_added = ""
while i < len(s):
    if i in b:
        i+=1
        continue   
    if last_added.startswith(s[i]):
        i+=1
        continue
    if i+1 >= len(s):
        a.add(s[i])
        break
    if s[i+1].startswith(s[i]) == False:
        a.add(s[i])
        i+=1
        continue
    max_pf = s[i+1]
    count = 0
    for j in range(i+1,len(s)):
        if s[j].startswith(s[i]) and len(s[j]) >= len(s[j-1]):
            max_pf = s[j]
            max_index = j
            count+=1  
    while max_index > i:
        if s[max_index].startswith(s[max_index-1]):
            b.add(max_index-1)
            max_index-=1
        else:
            break
            
    a.add(max_pf)
    last_added = max_pf
    i+=1    
total = 0
print a




        
