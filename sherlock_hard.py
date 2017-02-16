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
for i in range (0,len(arr)-1):
    if arr[i] < p:
        continue
    if arr[i] > q:
        break
    if arr[i+1]-arr[i] > max_gap:
        if (arr[i+1]+arr[i]) / 2 > q:
            gap_check = q-arr[i]
            if gap_check > max_gap:
                max_gap = gap_check
                max_gap_index= i
        else:
            max_gap = arr[i+1]-arr[i]
            max_gap_index = i

optimal = (arr[max_gap_index]+arr[max_gap_index+1]) / 2

# need to check if a number outside of range can get same result

maximized_min_diff = optimal - arr[max_gap_index]

additional_check_left = arr[0]-maximized_min_diff
additional_check_right = arr[0]+maximized_min_diff
start = p
index = 0
while p_q[index] < arr[0]:
    if abs(p_q[index]- arr[0]) >= maximized_min_diff:
        optimal=p_q[index]
        break
    index+=1
index = p_q[-1]
while index > arr[-1] and index> 0:
    if p_q[index]- arr[-1] >= maximized_min_diff:
        optimal = p_q[index]
    index-=1
print optimal