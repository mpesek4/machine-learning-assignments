''' Problem description: given array a1....an and range of (M,P) find the value 
within range that maximizes the function argmin{|aj-M|, 1<= i <= n}
if multiple solutions print the smallest one'''

import sys
import math
n = raw_input().strip()
arr = map(int,raw_input().strip().split(' '))
p_q = map(int,raw_input().strip().split(' '))
arr.sort()
p_q.sort()
# find the biggest gap within our range
p = p_q[0]
q= p_q[1]

max_gap =0
max_gap_index = 0
out_of_range = False
for i in range (0,len(arr)-1):
    # general plan is to find the biggest gap in our sorted array because the middle value of that gap
    # is the correct value of our function barring some edge cases
    if arr[i] > q:
        break
    if arr[i+1] < p:
        continue # these 2 achecks above make sure we are within our range
    if arr[i+1]-arr[i] > max_gap:
        if (arr[i+1]+arr[i]) / 2 > q:
            gap_check = q-arr[i]
            if gap_check > max_gap:
                max_gap = gap_check
                max_gap_index= i
                out_of_range = True
                optimal = q
        else:
            max_gap = arr[i+1]-arr[i]
            max_gap_index = i
if out_of_range == False:
    optimal = (arr[max_gap_index]+arr[max_gap_index+1]) / 2

# need to check if a number inside of our range but outside of the array is better, 2 simple checks

maximized_min_diff = optimal - arr[max_gap_index]


start = p
index = p_q[0]
found = False
while index < arr[0]:
    # first check is making sure any values between P and arr[0] maximize our function
    if abs(index- arr[0]) >= maximized_min_diff:
        optimal=index
        maximized_min_diff = abs(index- arr[0])
        break
    index+=1
index = p_q[-1]

while index > arr[-1] and index>= p_q[0]:
    # second check is to make sure any numbers between arr[-1] and Q maximize our function
    if index - arr[-1] > maximized_min_diff:
        optimal = index
        break
    index-=1
print optimal

    