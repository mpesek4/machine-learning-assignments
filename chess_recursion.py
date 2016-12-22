# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:37:05 2016

@author: Michael
"""

import sys
import copy
class Node:
    def __init__(self, gamestate, parent, children, depth):
        self.gamestate = gamestate
        self.parent = parent
        self.children = children
        self.player = player
    def __setChildren__(self,c):
        self.children = c
    def __getGamestate(self):
        return self.gamestate
    def __goal__(self):
        return ('b','Q') not in self.gamestate[0] or ('b','Q') not in self.gamestate[1] or \
            ('b','Q') not in self.gamestate[2]  or ('b','Q') not in self.gamestate[3] 
        
       
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
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='w' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'b' :
                            knight_states.append('winner')
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
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='w' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'b':
                            bishop_states.append('winner')
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='b' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'w':
                            queen_states.append('loser')
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
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='w' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'b':
                            rook_states.append('winner')
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='b' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'w':
                            queen_states.append('loser')
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
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='w' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'b':
                            queen_states.append('winner')
                        ## if black can take whites queen this is a failure
                        if gamestate[i+move[0]][j+move[1]][1] == 'Q' and player =='b' and \
                        gamestate[i+move[0]][j+move[1]][0] == 'w':
                            queen_states.append('loser')
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
def win_in_one(gamestate,moves_left,player):
    # if it is blacks move, white cannot win in one move, so call the function again on iterations and decrease moves_left
    
    
    head = Node(gamestate,None, None, 0)
    d = deque()
    deque.append(head)
    depth = 0
    while deque.maxlen > 0:  # Populate tree with all gamestates
        head = deque.pop()
        depth+=1
        if depth > moves_left:
            break
        gamestate = head.getGamestate()
        children = find_legal_moves(gamestate,'w')
        c = []
        for state in children:
            child = Node(state,head,None,depth)
            deque.append(child)
            c.append(child)
        head.setChildren(c)    
           
        
        
        
        
   
        
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
    check = win_in_one(board_state, m, 'w')
    print check