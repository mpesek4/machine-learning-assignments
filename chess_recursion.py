# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:37:05 2016

@author: Michael
"""

import sys
def find_legal_moves(gamestate,i,j,player):
    # 1: test what kind of piece it is
    # 2: create a process that iterates over all possible moves, and if a move is legal adds a new available gamestate to return
    states = [] # this will be our return, a list of all the new gamestates
    if player == 'b':
        opposing_piece == 'w'
    else:
        opposing_piece == 'b'
    for i in range(0,4):
        for j in range(0,4):
            knight_moves = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]
            bishop_moves = [(1,1),(2,2),(3,3),(-1,-1),(-2,-2),(-3,-3),(1,-1),(2,-2),(3,-3),(-1,1),(-2,2),(-3,3)]
            rook_moves = [(1,0),(2,0),(3,0),(-1,0),(-2,0),(-3,0),(0,1),(0,2),(0,3),(0,-1),(0,-2),(0,-3)]
            # queen moves are a concatenation of the above 2 lists
            if gamestate[i][j][1] == 'N':
                for move in knight_moves:
                    if (i+move[0] <=3 and >=0) and (j+move[1] <=3 and >=0) and gamestate[i+move[0]][j+move[1]][0] in \                                  [opposing_piece,'0']:
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = ('B',player)
            if gamestate[i][j][1] == 'B':
                for move in bishop_moves:
                    if (i+move[0] <=3 and >=0) and (j+move[1] <=3 and >=0) and gamestate[i+move[0]][j+move[1]][0] in \                                  [opposing_piece,'0']:
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = ('B',player)

            if gamestate[i][j][1] == 'R':
                for move in rook_moves:
                    if (i+move[0] <=3 and >=0) and (j+move[1] <=3 and >=0) and gamestate[i+move[0]][j+move[1]][0] in \                                  [opposing_piece,'0']:
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = ('B',player) 
            if gamestate[i][j][1] == 'Q':
                for move in bishop_moves+rook_moves:
                    if (i+move[0] <=3 and >=0) and (j+move[1] <=3 and >=0) and gamestate[i+move[0]][j+move[1]][0] in \                                  [opposing_piece,'0']:
                        new_gamestate = copy.deepcopy(gamestate)
                        new_gamestate[i][j] = ('0',0)
                        new_gamestate[i+move[0]][j+move[1]] = ('B',player)
def win_in_one(gamestate,moves_left,player):
    # if it is blacks move, white cannot win in one move, so call the function again on iterations and decrease moves_left
    if player == 'black':
        for i in range(0,4):
            for j in range(0,4):
                if gamestate[i][j][0] == 'b': # we found a piece we can move, find all legal moves
                    find_legal_moves(gamestate,i,j,'b')
    # figure out all the possible game states

num_of_games = int(raw_input().strip())

for i in range(0,num_of_games):
    board_state = [4][4]
    for i in range(0,4):
        for j in range(0,4):
            board_state[i][j] = (0,0)
    
    line_1 = raw_input().strip()
    w = int(line_1(0))
    b = int(line_1(1))
    m = int(line_1(2))
    for i in range(0,w):
        line_i = raw_input().strip()
        piece = line_i(0)
        col = line_i(1)
        row = int(line_i(2))
        if col == 'A':
            col_num = 0
        elif col == 'B':
            col_num = 1
        elif col == 'C':
            col_num = 2:
        else:
            col_num = 3:
        row = row - 1
        board_state[row][col_num] = ('w',piece)
    for i in range(0,b):
        line_i = raw_input().strip()
        piece = line_i(0)
        col = line_i(1)
        row = int(line_i(2))
        if col == 'A':
            col_num = 0
        elif col == 'B':
            col_num = 1
        elif col == 'C':
            col_num = 2:
        else:
            col_num = 3:
        row = row - 1
        board_state[row][col_num] = ('b',piece)
        ### out board state is set up
        ### now we must test whether or not we can win in one move
        check = win_in_one(board_state, m, 'w')