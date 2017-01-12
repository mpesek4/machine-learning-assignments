#!/bin/python

import sys


n = int(raw_input().strip())
number = raw_input().strip()
# your code goes here
answer = 0
zeros = []
ones = []
twos = []
threes = []
fours = []
fives = []  
sixes = []
sevens = []
eights = []
nines = []
for i in range(0,n):
     #these lists hold the positions of our numbers, so we can easily tell as example there is a 4 after a 3
    if number[i] == '0':
        zeros.append(i)
    if number[i] == '1':
        ones.append(i)
    if number[i] == '2':
        twos.append(i)
    if number[i] == '3':
        threes.append(i)    
    if number[i] == '4':
        fours.append(i)
    if number[i] == '5':
        fives.append(i)   
    if number[i] == '6':
        sixes.append(i)
    if number[i] == '7':
        sevens.append(i)
    if number[i] == '8':
        eights.append(i)
    if number[i] == '9':
        nines.append(i)
# divisibility requires the last 3 numbers are divisible by 8, the latter two (of 3) only differ whether the first number is odd or even
# otherwise there is a pattern
running_sum = 0
# for subsequences of length one its easy enough, only 0 and 8 are divisible by 8
running_sum+= len(eights)+len(zeros)
#substrings of length 2 are 00 08 16 24 32 65 72 80 88 96
# each combo represented as    
six_after_one = 0
for i in range(0,len(ones)):
    for j in range(0,len(sixes)):
        if sixes[j] >ones[i]:
            six_after_one += 1
running_sum+= six_after_one                
four_after_two = 0
for i in range(0,len(twos)):
    for j in range(0,len(fours)):    
         if fours[j] >twos[i]:
                four_after_two += 1
running_sum+= four_after_two
two_after_three = 0
for i in range(0,len(threes)):
    for j in range(0,len(twos)):
        if twos[j] >threes[i]:
            two_after_three += 1
running_sum+= two_after_three
zero_after_four = 0
for i in range(0,len(fours)):
    for j in range(0,len(zeros)):
        if zeros[j] >fours[i]:
            zero_after_four += 1
running_sum+= zero_after_four
eight_after_four = 0
for i in range(0,len(fours)):
    for j in range(0,len(eights)):
        if eights[j] >fours[i]:
            eight_after_four += 1
running_sum+= eight_after_four
six_after_five = 0
for i in range(0,len(fives)):
    for j in range(0,len(sixes)):
        if sixes[j] >fives[i]:
            six_after_five += 1
running_sum+= six_after_five
four_after_six = 0
for i in range(0,len(sixes)):
    for j in range(0,len(fours)):
        if fours[j] >sixes[i]:
            four_after_six += 1
running_sum+= four_after_six
two_after_seven = 0
for i in range(0,len(sevens)):
    for j in range(0,len(twos)):
        if twos[j] >sevens[i]:
            two_after_seven += 1
running_sum+= two_after_seven
zero_after_eight = 0
for i in range(0,len(eights)):
    for j in range(0,len(zeros)):
        if zeros[j] >eights[i]:
            zero_after_eight += 1
running_sum+= zero_after_eight
eight_after_eight = 0
for i in range(0,len(eights)):
    for j in range(0,len(eights)):
        if eights[j] >eights[i]:
            eight_after_eight += 1
running_sum+= eight_after_eight
six_after_nine = 0
for i in range(0,len(nines)):
    for j in range(0,len(sixes)):
        if sixes[j] >nines[i]:
            six_after_nine += 1
running_sum+= six_after_nine          
    

for z in range(0,n):
    is_even = True
    if int(number[z]) % 2 == 0:
        is_even = True
    else:
        is_even = False
    
    if(is_even):
        six_after_one = 0
        for i in range(z,len(ones)):
            for j in range(0,len(sixes)):
                if sixes[j] >ones[i]:
                    six_after_one += 1
        running_sum+= (i+1)*(i+1)*six_after_one                
        four_after_two = 0
        for i in range(z,len(twos)):
            for j in range(z,len(fours)):
                if fours[j] >twos[i]:
                    four_after_two += 1
        running_sum+= (i+1)*(i+1)*four_after_two
        two_after_three = 0
        for i in range(z,len(threes)):
            for j in range(z,len(twos)):
                if twos[j] >threes[i]:
                    two_after_three += 1
        running_sum+= (i+1)*(i+1)*two_after_three
        zero_after_four = 0
        for i in range(z,len(fours)):
            for j in range(z,len(zeros)):
                if zeros[j] >fours[i]:
                    zero_after_four += 1
        running_sum+= (i+1)*(i+1)*zero_after_four
        eight_after_four = 0
        for i in range(z,len(fours)):
            for j in range(z,len(eights)):
                if eights[j] >fours[i]:
                    eight_after_four += 1
        running_sum+= (i+1)*(i+1)*eight_after_four
        six_after_five = 0
        for i in range(z,len(fives)):
            for j in range(z,len(sixes)):
                if sixes[j] >fives[i]:
                    six_after_five += 1
        running_sum+= (i+1)*(i+1)*six_after_five
        four_after_six = 0
        for i in range(z,len(sixes)):
            for j in range(z,len(fours)):
                if fours[j] >sixes[i]:
                    four_after_six += 1
        running_sum+= (i+1)*(i+1)*four_after_six
        two_after_seven = 0
        for i in range(z,len(sevens)):
            for j in range(z,len(twos)):
                if twos[j] >sevens[i]:
                    two_after_seven += 1
        running_sum+= (i+1)*(i+1)*two_after_seven
        zero_after_eight = 0
        for i in range(z,len(eights)):
            for j in range(z,len(zeros)):
                if zeros[j] >eights[i]:
                    zero_after_eight += 1
        running_sum+= (i+1)*(i+1)*zero_after_eight
        eight_after_eight = 0
        for i in range(z,len(eights)):
            for j in range(z,len(eights)):
                if eights[j] >eights[i]:
                    eight_after_eight += 1
        running_sum+= (i+1)*(i+1)*eight_after_eight
        six_after_nine = 0
        for i in range(z,len(nines)):
            for j in range(z,len(sixes)):
                if sixes[j] >nines[i]:
                    six_after_nine += 1
        running_sum+= (i+1)*(i+1)*six_after_nine   
    elif(is_even == False):
        # use the other pattern of digits that are divible by 8
        four_after_zero = 0
        for i in range(z,len(zeros)):
            for j in range(z,len(fours)):
                if fours[j] >zeros[i]:
                    four_after_zero += 1
        running_sum+= (i+1)*(i+1)*four_after_zero
        two_after_one = 0
        for i in range(z,len(ones)):
            for j in range(z,len(twos)):
                if twos[j] >ones[i]:
                    two_after_one += 1
        running_sum+= (i+1)*(i+1)*two_after_one
        zero_after_two = 0
        for i in range(z,len(twos)):
            for j in range(z,len(zeros)):
                if zeros[j] >twos[i]:
                    zero_after_two += 1
        running_sum+= (i+1)*(i+1)*zero_after_two
        eight_after_two = 0
        for i in range(z,len(twos)):
            for j in range(z,len(eights)):
                if eights[j] >twos[i]:
                    eight_after_two += 1
        running_sum+= (i+1)*(i+1)*eight_after_two
        six_after_three = 0
        for i in range(z,len(threes)):
            for j in range(z,len(sixes)):
                if sixes[j] >threes[i]:
                    six_after_three += 1
        running_sum+= (i+1)*(i+1)*six_after_three
        four_after_four = 0
        for i in range(z,len(fours)):
            for j in range(z,len(fours)):
                if fours[j] >fours[i]:
                    four_after_four += 1
        running_sum+= (i+1)*(i+1)*four_after_four
        two_after_five = 0
        for i in range(z,len(fives)):
            for j in range(z,len(twos)):
                if twos[j] >fives[i]:
                    two_after_five += 1
        running_sum+= (i+1)*(i+1)*two_after_five
        zero_after_six = 0
        for i in range(z,len(sixes)):
            for j in range(z,len(zeros)):
                if zeros[j] >sixes[i]:
                    zero_after_six += 1
        running_sum+= (i+1)*(i+1)*zero_after_six
        eight_after_six = 0
        for i in range(z,len(sixes)):
            for j in range(z,len(eights)):
                if eights[j] >sixes[i]:
                    eight_after_six += 1
        running_sum+= (i+1)*(i+1)*eight_after_six
        six_after_seven = 0
        for i in range(z,len(sevens)):
            for j in range(z,len(sixes)):
                if sixes[j] >sevens[i]:
                    six_after_seven += 1
        running_sum+= (i+1)*(i+1)*six_after_seven
        four_after_eight = 0
        for i in range(z,len(eights)):
            for j in range(z,len(fours)):
                if fours[j] >eights[i]:
                    four_after_eight += 1
        running_sum+= (i+1)*(i+1)*four_after_eight
        two_after_nine = 0
        for i in range(z,len(nines)):
            for j in range(z,len(twos)):
                if twos[j] >nines[i]:
                    two_after_nine += 1
        running_sum+= (i+1)*(i+1)*two_after_nine
print running_sum        
        