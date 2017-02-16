'''Input is an MxN array of costs for slicing up a cutting board. Goal is to minimize the cost of cutting into 1x1 grid pieces,
 everytime you make either a vertical or horizontal cut you pay the cost for that cut plus an additional multiple of that cost,#where the multiple is how many other cuts you pass that were made previously. For example, if you had previously made one horizontal slice, a vertical slice that has a cost of 4 would instead be 4+4 because it is passing through one horizontal slice, therefore each time you make a slice you are increasing the cost of later slices that would pass through that slice.
 
 
 '''

import sys

n = int(raw_input().strip())
for i in range(0,n):
    m_n = raw_input().strip().split(' ')
    h_list = map(int, raw_input().strip().split(' '))
    v_list = map(int, raw_input().strip().split(' '))
    
    # greedy algorithm always choosing the biggest number cost and if there is a tie, most remaining cuts to choose between h/v
    
    h_list.sort(reverse = True)
    v_list.sort(reverse = True)
    h_remaining_cuts = len(h_list)
    v_remaining_cuts = len(v_list)
    
    v_cuts_made = 0
    h_cuts_made = 0
    answer = 0
    h_pointer = 0
    v_pointer = 0
    while(h_remaining_cuts >0 or v_remaining_cuts > 0):
        if(h_remaining_cuts == 0):
            while(v_remaining_cuts> 0):
                answer+= v_list[v_pointer]* (h_cuts_made+1)
                v_pointer+=1
                v_remaining_cuts-=1
        elif(v_remaining_cuts == 0):
            while(h_remaining_cuts> 0):
                answer+= h_list[h_pointer]* (v_cuts_made+1)
                h_pointer+=1
                h_remaining_cuts-=1
        elif(h_list[h_pointer] > v_list[v_pointer]):
            answer += h_list[h_pointer] * (v_cuts_made+1)
            h_pointer+=1
            h_cuts_made+=1
            h_remaining_cuts-=1
        elif(v_list[v_pointer] > h_list[h_pointer]):
            answer+= v_list[v_pointer] * (h_cuts_made+1)
            v_pointer+=1
            v_cuts_made+=1
            v_remaining_cuts-=1
        # else they are the same
        else:
            if h_remaining_cuts >= v_remaining_cuts:
                answer += h_list[h_pointer] * (v_cuts_made+1)
                h_pointer+=1
                h_cuts_made+=1
                h_remaining_cuts-=1
            else:
                answer+= v_list[v_pointer] * (h_cuts_made+1)
                v_pointer+=1
                v_cuts_made+=1
                v_remaining_cuts-=1
            
    print answer % 1000000007
