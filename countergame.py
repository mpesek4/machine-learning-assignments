
# simple game, take a value N, players take turns either halving it if N is a power of 2, or subtracting the closest power
# of 2 that is less than N from N, if N=1 the person whose turn it is loses
import math

powers_of_2 = []
for i in range(0,67):
    powers_of_2.append(math.pow(2,i))

for i in range(0,1):
    n = 13174607262084689114  
    turns_taken = 0
    while n > 1:
        if n in powers_of_2:
            n = n/2            
        else:
            # search for a power of 2 that is bigger
            index = 0
            for i in range(0,67):
                if powers_of_2[i] > n:
                    index = i
                    break
                pass
            n = n-math.pow()
        turns_taken+=1
    print turns_taken
    if turns_taken % 2 == 0:
        print "Richard"
    else:
        print "Louise"