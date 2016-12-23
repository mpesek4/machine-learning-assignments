import sys
import copy
from collections import deque
class Node:
    def __init__(self, gamestate, parent, children, depth):
        self.gamestate = gamestate
        self.parent = parent
        self.children = children
       
        self.depth = depth
        self.score = self.heuristic()
    def heuristic(self):
        if self.parent== None:
            return 0
        previous_state = self.parent.getGamestate()
        minor_pb = 0
        minor_pw = 0
        rook_pw = 0
        rook_pb = 0
        if self.isGoal():
            return 100
        for square in previous_state[0]+previous_state[1]+previous_state[2]+previous_state[3]:
            if (square == ('w','R')):
                rook_pw +=1
            if (square == ('b','R')):
                rook_pb +=1
            if (square == ('w','N')):
                minor_pw +=1
            if (square == ('b','N')):
                minor_pb +=1    
            if (square == ('w','B')):
                minor_pw +=1
            if (square == ('b','B')):
                minor_pb +=1     
        rook_cw = 0
        rook_cb = 0
        minor_cw = 0
        minor_cb = 0
        for square in self.getGamestate()[0]+self.getGamestate()[1]+self.getGamestate()[2]+self.getGamestate()[3]:
            if (square == ('w','R')):
                rook_cw +=1
            if (square == ('b','R')):
                rook_cb +=1
            if (square == ('w','N')):
                minor_cw +=1
            if (square == ('b','N')):
                minor_cb +=1    
            if (square == ('w','B')):
                minor_cw +=1
            if (square == ('b','B')):
                minor_cb +=1     
        total_parent_white = minor_pw+rook_pw
        total_parent_black = minor_pb+rook_pb
        total_current_white = rook_cw+minor_cw
        total_current_black = rook_cb+minor_cb
        score = 0
       
        if total_current_black < total_parent_black:
            score+=10
        if total_current_white < total_parent_white:
            score-=10
        
            
        return score
    def setScore(self,score):
        self.score= score
    def getScore(self):
        return self.score
    def getDepth(self):
        return self.depth
    def setChildren(self,c):
        self.children = c
    def getChildren(self):
        return self.children 
    def getGamestate(self):
        return self.gamestate
    def isGoal(self):
        return (('b','Q') not in self.gamestate[0] + self.gamestate[1] + \
                    self.gamestate[2]+self.gamestate[3]) and \
               (('w','Q')  in self.gamestate[0] +self.gamestate[1] + \
                    self.gamestate[2]+self.gamestate[3] )


def find_legal_moves(gamestate,player):
    # 1: test what kind of piece it is
    # 2: create a process that iterates over all possible moves, and if a move is legal adds a new available gamestate to return
    states = [] # this will be our return, a list of all the new gamestates
    queen_states = []
    rook_states = []
    bishop_states = []
    knight_states = []
    if player == 'b':
        opposing_piece = 'w'
    else:
        opposing_piece = 'b'
    for i in range(0,4):
        for j in range(0,4):
            try:
                if gamestate[i][j][0] not in [player]:
                    continue
            except:
                print 'hello'
            knight_moves = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]
            bishop_moves = [(1,1),(2,2),(3,3),(-1,-1),(-2,-2),(-3,-3),(1,-1),(2,-2),(3,-3),(-1,1),(-2,2),(-3,3)]
            rook_moves = [(1,0),(2,0),(3,0),(-1,0),(-2,0),(-3,0),(0,1),(0,2),(0,3),(0,-1),(0,-2),(0,-3)]
            # queen moves are a concatenation of the above 2 lists
            if gamestate[i][j][1] == 'N':
                for move in knight_moves:
                    if (i+move[0] <=3 and i+move[0] >=0) and (j+move[1] <=3 and j+move[1] >=0) \
                    and gamestate[i+move[0]][j+move[1]][0] in [opposing_piece,'0'] \
                    and gamestate[i+move[0]][j+move[1]][0] not in ['w','Q']:
                        #if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='w' and \
                        #gamestate[i+move[0]][j+move[1]][0] == 'b' :
                        #    knight_states.append('winner')
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='b' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'w':
                            continue
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = (player,'N')
                        knight_states.append(new_gamestate)
            if gamestate[i][j][1] == 'B':
                index = -1
                for m in range (0,12):
                    index+=1
                    move =  bishop_moves[index] 
                    if (i+move[0] <=3 and i+move[0] >=0) and (j+move[1] <=3 and j+move[1] >=0) \
                    and gamestate[i+move[0]][j+move[1]][0] in [opposing_piece,'0'] \
                    and gamestate[i+move[0]][j+move[1]][0]:
                       
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = (player,'B')
                        bishop_states.append(new_gamestate)
                        if gamestate[i+move[0]][j+move[1]][0] in [opposing_piece]:
                            if index < 3:
                                index = 2
                            elif index < 6:
                                index = 5
                            elif index <9:
                                index = 8
                            elif index < 12:
                                break
                    else: # if we hit an illegal move we are able to do a skip (we cannot move through pieces)
                        if index < 3:
                            index = 2
                        elif index < 6:
                            index = 5
                        elif index <9:
                            index = 8
                        elif index < 12:
                            break
                    if index == 11:
                        break
            if gamestate[i][j][1] == 'R':
                index = -1
                for m in range (0,12):
                    index+=1
                    move = rook_moves[index]
                    if (i+move[0] <=3 and i+move[0] >=0) and (j+move[1] <=3 and j+move[1] >=0) \
                    and gamestate[i+move[0]][j+move[1]][0] in [opposing_piece,'0'] \
                    and gamestate[i+move[0]][j+move[1]][0]:
                       
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = (player,'R')
                        rook_states.append(new_gamestate)
                        if gamestate[i+move[0]][j+move[1]][0] in [opposing_piece]:
                            if index < 3:
                                index = 2
                            elif index < 6:
                                index = 5
                            elif index <9:
                                index = 8
                            elif index < 12:
                                break
                    else:
                        if index < 3:
                            index = 2
                        elif index < 6:
                            index = 5
                        elif index <9:
                            index = 8
                        elif index < 12:
                            break
                    if index == 11:
                        break
                        
            if gamestate[i][j][1] == 'Q':
                index = -1
                for m in range (0,24):
                    index+=1
                    queen_moves = bishop_moves+rook_moves
                    move = queen_moves[index]
                    if (i+move[0] <=3 and i+move[0] >=0) and (j+move[1] <=3 and j+move[1] >=0) \
                    and gamestate[i+move[0]][j+move[1]][0] in [opposing_piece,'0'] \
                    and gamestate[i+move[0]][j+move[1]][0]:
                       
                       
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = (player,'Q')
                        queen_states.append(new_gamestate)
                        if gamestate[i+move[0]][j+move[1]][0] in [opposing_piece]:
                            
                            if index < 3:
                               
                                index = 2
                            elif index < 6:
                                index = 5
                            elif index <9:
                                index = 8
                            elif index < 12:
                                index = 11
                            elif index <15:
                                index = 14
                            elif index < 18:
                                index = 17
                            elif index < 21:
                                index= 20
                            elif index < 24:
                                break
                    else:
                        if index < 3:
                            index = 2
                        elif index < 6:
                            index = 5
                        elif index <9:
                            index = 8
                        elif index < 12:
                            index = 11
                        elif index <15:
                            index = 14
                        elif index < 18:
                            index = 17
                        elif index < 21:
                            index= 20
                        elif index < 24:
                            break
                    if index == 23:
                        break
    states = states+queen_states+bishop_states+rook_states+knight_states
    return states
def minimax(node, depth ,alpha,beta, maximizingPlayer):
    if depth == 0 or node.getChildren() == None:
        
        return node.getScore()
    
    if maximizingPlayer:
        bestValue = -1
        for child in node.getChildren():
            v = minimax(child,depth-1,alpha,beta, False)
            bestValue = max(bestValue,v)
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        node.setScore(bestValue)
    else:
        bestValue = 1
        for child in node.getChildren():
            v = minimax(child,depth-1,alpha,beta, True)
            bestValue = min(bestValue,v)
            beta = min(beta,v)
            if beta <=alpha:
                break
        node.setScore(bestValue)

        
def win_in_one(gamestate,moves_left,player,d):
    
   head = Node(gamestate,None, None, 0)
   root = head
   d = []
   d.append(head)
   depth = 0
   while len(d) > 0:  # Populate tree with all gamestates
      
      
               
       head = d[-1]
       d = d[0:-1]

       depth = head.getDepth()
       depth = depth+1
       
       
       if depth % 2 == 0:
           player = 'b'
       else:
           player = 'w'
       
       
       gamestate = head.getGamestate()
       children = find_legal_moves(gamestate,player)
       if depth == moves_left or head.isGoal():
           if head.isGoal():
               head.setScore(100)
#           else:
#               head.setScore(-1)
           
       if head.isGoal():
           continue
       c = []
       for state in children:
           child = Node(state,head,None,depth)
           if child.isGoal():
               child.setScore(100)
#           else:
#               child.setScore(-100)
           if depth <= moves_left+1:
               c.append(child)
               
       # for child in c, order them by heuristic and add to queue in order
       c.sort(key =lambda x: x.getScore())
       for item in c:
           d.append(item)
       
       head.setChildren(c)    
         
   g = minimax(root,moves_left,-100,100,True)
   #print root.getScore()
   if root.getScore() == 100:
       return 'YES'
   else:
       return 'NO'
       
                
        
        
    # figure out all the possible game states

num_of_games = int(raw_input().strip())

for i in range(0,num_of_games):
    board_state = [[0 for i in range(4)] for j in range(4)]
    for i in range(0,4):
        for j in range(0,4):
            board_state[i][j] = ('0',0)
    
    line_1 = raw_input().strip().split()
    w = int(line_1[0])
    b = int(line_1[1])
    m = int(line_1[2])
    for i in range(0,w):
        line_i = raw_input().strip().split()
        piece = line_i[0]
        col = line_i[1]
        row = int(line_i[2])
        if col == 'A':
            col_num = 0
        elif col == 'B':
            col_num = 1
        elif col == 'C':
            col_num = 2
        else:
            col_num = 3
        row = row - 1
        board_state[row][col_num] = ('w',piece)
    for i in range(0,b):
        line_i = raw_input().strip().split()
        piece = line_i[0]
        col = line_i[1]
        row = int(line_i[2])
        if col == 'A':
            col_num = 0
        elif col == 'B':
            col_num = 1
        elif col == 'C':
            col_num = 2
        else:
            col_num = 3
        row = row - 1
        board_state[row][col_num] = ('b',piece)
        ### out board state is set up
        ### now we must test whether or not we can win in one move
    d = {}
    key = id(board_state)
    d[key] = board_state
    check = win_in_one(board_state, m, 'w',d)
    print check# Enter your code here. Read input from STDIN. Print output to STDOUT