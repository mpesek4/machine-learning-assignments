
from __future__ import print_function
import sys
import math
from fractions import Fraction
w,h = raw_input().strip().split(' ')
w,h = [int(w),int(h)]
circleX,circleY,r = raw_input().strip().split(' ')
circleX,circleY,r = [int(circleX),int(circleY),int(r)]
circleX = Fraction(circleX)
circleY = Fraction(circleY)
r= Fraction(r)
x1,y1,x3,y3 = raw_input().strip().split(' ')
x1,y1,x3,y3 = [int(x1),int(y1),int(x3),int(y3)]
x1 = Fraction(x1)

x3 = Fraction(x3)
y1 = Fraction(y1)
y3 = Fraction(y3)

# your code goes here

def power_of(x,y):
    i=x
    for j in range(0,y-1):
        i = i*x
    return i
    
def in_Circle(x,y,circleX,circleY,r):
    # function that checks whether or not a cartesian point is inside a defined circle
    # euclidean distance from point to center of circle must be <= r
    e_distance_squared = power_of(x-circleX,2)+power_of(y-circleY,2)
    r_squared = power_of(r,2)
    if(e_distance_squared <= r_squared):
        return True
    else:
        return False
def in_Square(x1,y1,x3,y3):
    #populate a table with the pixels that are blackened
    explored = set()
    if x1!=x3 and (y3-y1)/(x3-x1) == 1 or (y3-y1)/(x3-x1) == -1:
        # square is not angled, can just do an easy loop
        startx = min(x3,x1)
        endx = max(x3,x1)
        starty = min(y3,y1)
        endy = max(y3,y1)
        for i in range(int(startx),int(endx+1)):
            for j in range(int(starty),int(endy+1)):
                explored.add((i,j))
        return explored       
    midpoint_x = (x1+x3) / Fraction(2)
    midpoint_y = (y1+y3) / Fraction(2)
    change_in_y = midpoint_y-y1
    change_in_x = midpoint_x-x1
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
        x2 = midpoint_x+change_in_y
        y2 = midpoint_y-change_in_x
        x4 = midpoint_x-change_in_y
        y4 = midpoint_y+change_in_x
            
         

    else:
        x2 = midpoint_x+change_in_y
        y2 = midpoint_y-change_in_x
        x4 = midpoint_x-change_in_y
        y4 = midpoint_y+change_in_x
#        temp = x2
#        x2 = x4
#        x4 = temp
#        temp = y2
#        y2 = y4
#        y4 = temp
    
    explored.add((midpoint_x,midpoint_y))
#    fx1 = math.floor(x1)
#    fx2 = imath.floor(x2)
#    fx3 = int(math.floor(x3))
#    fx4 = int(math.floor(x4))
#    fy1 = int(math.floor(y1))
#    fy2 = int(math.floor(y2))
#    fy3 = int(math.floor(y3))
#    fy4 = int(math.floor(y4))
    explored.add((x2,y2))
    explored.add((x1,y1))
    explored.add((x3,y3))
    explored.add((x4,y4))
    cx1,cx2,cy1,cy2 = x1,x2,y1,y2
    if (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2<cy1) and (y4>=y1):
        #upleft
        # need to change to clockwise
        temp = x2
        x2 = x4
        x4 = temp
        temp = y2
        y2 =y4
        y4=temp
    elif (cx2 < cx1) and (cy2 > cy1) and (y4>=y1):
        # downleft need to change to clockwise
        temp = x2
        x2 = x4
        x4 = temp
        temp = y2
        y2 =y4
        y4=temp
    elif (cx1<cx2) and (cy1<cy2) and (x4>=x1):
        #downright and need to go clockwise
        temp = x2
        x2 = x4
        x4 = temp
        temp = y2
        y2 =y4
        y4=temp
    elif cx1<cx2 and cy1>cy2 and x4<=x1:
        #upright and need to go clockwise
        temp = x2
        x2 = x4
        x4 = temp
        temp = y2
        y2 =y4
        y4=temp
        
    else:
        pass
        
    # going clockwise we need to do x1 to x2, x2 to x3, x3 to x4, and x4 to x1 to check 4 quadrants
    # we also need to know which direction we are going in
    
    
    def add_to_set(x1,x2,y1,y2, direction,explored):
        
        if direction == "upright": # good upright
            for i in range(int(math.ceil(x1)),int(math.floor(x2+1))):
                for j in range(int(math.floor(y2)),int(math.floor(y1+1))):
                    if i==x1:
                        continue
                    if y1==j:
                        explored.add((i,j))
                        continue
                    # if the slope is smaller we add it
                    if Fraction(j-y1)/(i-x1) >= Fraction(y2-cy1) / (x2-x1):
                        explored.add((i,j))
        if direction == "downright": # good? 
            for i in range(int(math.floor(x1)),int(math.floor(x2+1))):
                for j in range(int(math.ceil(y1)),int(math.floor(y2+1))):
                    if i == x1:
                        explored.add((i,j))
                        continue
                    # if the slope is bigger we add it
                    if Fraction(j-y1)/(i-x1) >= Fraction(y2-y1) / (x2-x1):
                        explored.add((i,j))
        if direction == "downleft": # good?
            for i in range(int(math.floor(x2)),int(math.floor(x1+1))):
                for j in range(int(math.floor(y1)),int(math.floor(y2+1))):
                    if i == x2:
                        explored.add((i,j))
                        continue
                    # if the slope is smaller we add it
                    if Fraction(j-y2)/(i-x2) <= Fraction(y1-y2) / (x1-x2):
                        explored.add((i,j))   
        if direction == "upleft":
            for i in range(int(math.ceil(x2)),int(math.floor(x1+1))):
                for j in range(int(math.floor(y2)),int(math.floor(y1+1))):
                    if x1 ==i:
                        explored.add((i,j))
                        continue
                    # if the slope is bigger we add it
                    if Fraction(j-y1)/(i-x1) >= Fraction(y2-y1) / (x2-x1):
                        explored.add((i,j))
    cx1,cx2,cy1,cy2 = x1,x2,y1,y2
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
        
    
        
    
    add_to_set(cx1,cx2,cy1,cy2,direction,explored)                    
                    
    cx1,cx2,cy1,cy2 = x2,x3,y2,y3
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    
    add_to_set(cx1,cx2,cy1,cy2,direction,explored) 
                                      
    cx1,cx2,cy1,cy2 = x3,x4,y3,y4
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    add_to_set(cx1,cx2,cy1,cy2,direction,explored) 
    
    cx1,cx2,cy1,cy2 = x4,x1,y4,y1
    if (cx2>cx1) and (cy2>cy1):
        direction = "downright"
    elif (cx2>cx1) and (cy2<cy1):
        direction = "upright"
    elif (cx2<cx1) and (cy2>cy1):
        direction = "downleft"
    else:
        direction = "upleft"
    
    add_to_set(cx1,cx2,cy1,cy2,direction,explored) 
    
    return explored

explored = in_Square(x1,y1,x3,y3)
for y in range(0,h):
    for x in range(0,w):
        if in_Circle(x,y,circleX,circleY,r) or (x,y) in explored:
            print("#",end='')
        else:
            print(".",end='')
    print()