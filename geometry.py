#!/bin/python
from __future__ import print_function
import sys
import math

w,h = 20,16

circleX,circleY,r = 100,100,1

x1,y1,x3,y3 = 6,8,4,2

def in_Circle(x,y,circleX,circleY,r):
    # function that checks whether or not a cartesian point is inside a defined circle
    # euclidean distance from point to center of circle must be <= r
    e_distance_squared = math.pow(x-circleX,2)+math.pow(y-circleY,2)
    r_squared = math.pow(r,2)
    if(e_distance_squared <= r_squared):
        return True
    else:
        return False
def in_Square(x1,y1,x3,y3):
    #populate a table with the pixels that are blackened
    explored = set()
    if float(y3-y1)/(x3-x1) == 1 or float(y3-y1)/(x3-x1) == -1:
        # square is not angled, can just do an easy loop
        startx = min(x3,x1)
        endx = max(x3,x1)
        starty = min(y3,y1)
        endy = max(y3,y1)
        for i in range(startx,endx+1):
            for j in range(starty,endy+1):
                explored.add((i,j))
        return explored       
    midpoint_x = float(x1+x3) / 2
    midpoint_y = float(y1+y3) / 2
    change_in_y = abs(y3-midpoint_y)
    change_in_x = abs(x3-midpoint_x)
    # translate to new points
    if x1 ==x3 or y1 == y3:
        x2 = midpoint_x+(midpoint_y-y1)
        y2 = midpoint_y+(midpoint_x-x1)    
        x4 = midpoint_x-(midpoint_y-y1)
        y4 = midpoint_y-(midpoint_x-x1)
    elif x1 < x3 and y1<y3:
        x2 = midpoint_x-(change_in_y)
        y2 = midpoint_y+(change_in_x)    
        x4 = midpoint_x+(change_in_y)
        y4 = midpoint_y-(change_in_x)
    elif x1 <x3 and y1 > y3:
        x2 = midpoint_x+(change_in_y)
        y2 = midpoint_y-(change_in_x)    
        x4 = midpoint_x-(change_in_y)
        y4 = midpoint_y+(change_in_x)
    elif x1 > x3 and y1 < y3:
        temp = x1
        x1 = x3
        x3 = temp
        temp = y1
        y1 = y3
        y3 = temp
        midpoint_x = float(x1+x3) / 2
        midpoint_y = float(y1+y3) / 2
        change_in_y = abs(y3-midpoint_y)
        change_in_x = abs(x3-midpoint_x)
        x2 = midpoint_x+(change_in_y)
        y2 = midpoint_y-(change_in_x)    
        x4 = midpoint_x-(change_in_y)
        y4 = midpoint_y+(change_in_x)
#        temp = x2
#        x2 = x4
#        x4 = temp
#        temp = y2
#        y2 = y4
#        y4 = temp
    else:
        temp = x1
        x1 = x3
        x3 = temp
        temp = y1
        y1 = y3
        y3 = temp
        midpoint_x = float(x1+x3) / 2
        midpoint_y = float(y1+y3) / 2
        change_in_y = abs(y3-midpoint_y)
        change_in_x = abs(x3-midpoint_x)
        x2 = midpoint_x-(change_in_y)
        y2 = midpoint_y+(change_in_x)    
        x4 = midpoint_x+(change_in_y)
        y4 = midpoint_y-(change_in_x)
#        temp = x2
#        x2 = x4
#        x4 = temp
#        temp = y2
#        y2 = y4
#        y4 = temp
    
    explored.add((midpoint_x,midpoint_y))
    fx1 = int(math.floor(x1))
    fx2 = int(math.floor(x2))
    fx3 = int(math.floor(x3))
    fx4 = int(math.floor(x4))
    fy1 = int(math.floor(y1))
    fy2 = int(math.floor(y2))
    fy3 = int(math.floor(y3))
    fy4 = int(math.floor(y4))
    explored.add((x2,y2))
    explored.add((x1,y1))
    explored.add((x3,y3))
    explored.add((x4,y4))
    
        
    # going clockwise we need to do x1 to x2, x2 to x3, x3 to x4, and x4 to x1 to check 4 quadrants
    # we also need to know which direction we are going in
    cx1,cx2,cy1,cy2 = int(fx1),int(fx2),int(fy1),int(fy2)
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    
    if direction == "downright":
        for i in range(cx1+1,cx2+1):
            for j in range(cy1,cy2+1):
                if j == cy1:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upright":
        for i in range(cx1,cx2+1):
            for j in range(cy1,cy2+1):
                if cx1==i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upleft":
        for i in range(cx2,cx1+1):
            for j in range(cy2+1,cy1+1):
                if cx2 ==i:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy2)/(i-cx2) >= float(cy1-cy2) / (cx1-cx2):
                    explored.add((i,j))
    if direction == "downleft":
        for i in range(cx2+1,cx1+1):
            for j in range(cy1,cy2+1):
              
                if cx1 == i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))    
                    
    cx1,cx2,cy1,cy2 = int(fx2),int(fx3),int(fy2),int(fy3)
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    
    if direction == "downright":
        for i in range(cx1+1,cx2+1):
            for j in range(cy1,cy2+1):
                if j == cy1:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upright":
        for i in range(cx1,cx2+1):
            for j in range(cy1,cy2+1):         
                if cx1==i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upleft":
        for i in range(cx2,cx1+1):
            for j in range(cy2+1,cy1+1):
                if cx2 ==i:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy2)/(i-cx2) >= float(cy1-cy2) / (cx1-cx2):
                    explored.add((i,j))
    if direction == "downleft":
        for i in range(cx2+1,cx1+1):
            for j in range(cy1,cy2+1):
                if cx1 == i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))                   
    cx1,cx2,cy1,cy2 = int(x3),int(x4),int(y3),int(y4)
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    
    if direction == "downright":
        for i in range(cx1+1,cx2+1):
            for j in range(cy1,cy2+1):
                if j == cy1:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upright":
        for i in range(cx1,cx2+1):
            for j in range(cy2,cy1+1):
                if cx1==i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upleft":
        for i in range(cx2,cx1+1):
            for j in range(cy2+1,cy1+1):
                if cx2 ==i:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy2)/(i-cx2) >= float(cy1-cy2) / (cx1-cx2):
                    explored.add((i,j))
    if direction == "downleft":
        for i in range(cx2+1,cx1+1):
            for j in range(cy1,cy2+1):
                if cx1 == i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))    
    cx1,cx2,cy1,cy2 = int(fx4),int(fx1),int(fy4),int(fy1)
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    
    if direction == "downright":
        for i in range(cx1+1,cx2+1):
            for j in range(cy1,cy2+1):
                if j == cy1:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upright":
        for i in range(cx1,cx2+1):
            for j in range(cy2,cy1+1):
                if cx1==i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))
    if direction == "upleft":
        for i in range(cx2,cx1+1):
            for j in range(cy2+1,cy1+1):
                if cx2 ==i:
                    explored.add((i,j))
                    continue
                # if the slope is bigger we add it
                if float(j-cy2)/(i-cx2) >= float(cy1-cy2) / (cx1-cx2):
                    explored.add((i,j))
    if direction == "downleft":
        for i in range(cx2+1,cx1+1):
            for j in range(cy1,cy2+1):
                if cx1 == i:
                    explored.add((i,j))
                    continue
                # if the slope is smaller we add it
                if float(j-cy1)/(i-cx1) <= float(cy2-cy1) / (cx2-cx1):
                    explored.add((i,j))    
    return explored
explored = in_Square(x1,y1,x3,y3)
for y in range(0,h):
    for x in range(0,w):
        if in_Circle(x,y,circleX,circleY,r) or (x,y) in explored:
            print("#",end='')
        else:
            print(".",end='')
    print()