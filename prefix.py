# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:16:16 2017

@author: Michael
"""
from sets import Set
from collections import deque
_end = '_end_'
s = ["A","ABC","ABCDE","ABCDF","ABCDZ","ABCDEF"]
# your code goes here
s.sort(reverse= True)
s.sort(lambda x,y: cmp(len(y),len(x)))
my_trie = dict()
secondary_trie = dict()
# method that creates a dictionary
def add_to_trie(word, my_trie):
    current_dict = my_trie
    for char in word:
        current_dict = current_dict.setdefault(char, {})
    current_dict[_end] = _end
    return my_trie
def prefix_finder(my_trie, word):
    current_dict = my_trie
    num = len(word)
    for char in word:
        if char in current_dict:
            current_dict = current_dict[char]
        else:
            return False,-1
        # word has been found, but it is also necessary to return the size of the word that has it as a prefix
        # continue

    while len(current_dict) <=1:        
        keys = current_dict.keys()
        current_dict = current_dict[keys[0]]
        num+=1
    return True,num
def remove_from_trie(trie, word):
    current_dict = trie
    path = [current_dict]
    for letter in word:
        current_dict = current_dict.get(letter, None)
        path.append(current_dict)
        if current_dict is None:
            # the trie doesn't contain this word.
            break
    else:
        deleted_branches = []
        for current_dict, letter in zip(reversed(path[:-1]), reversed(word)):
            if len(current_dict[letter]) <= 1:
                deleted_branches.append((current_dict, letter))
            else:
                break
        if len(deleted_branches) > 0:
            del deleted_branches[-1][0][deleted_branches[-1][1]]        
def exhaustive_check(word,my_trie,secondary_trie,num):
    # just because a inbetween is found for a pair, doesn't mean there is an inbetween for all the other words in our subset
    # this function goes to the main trie, and makes sure every branch off of our prefix is satisfied in the secondary tree,
    # otherwise it does not get added
    # example: if ABC and ACD were added to our subset and we have AC in our secondary-an invalid prefix pair-the string A
    # would be valid because AC is an in between with ACD, BUT there is no valid in between-ie AB doiesnt exist- for A and ABC
    # thus A is actually NOT a valid addition
    current_dict = my_trie
    
    i = 0 #keep track of iterations before num
    for char in word:
        current_dict = current_dict[char] 
    word_check = deque()
    root_dict = current_dict
    while True:
        keys = current_dict.keys()
        new_dicts = []
        for d in keys: # this saves all the other dictionaries we need to iterate through
            new_dicts.append(current_dict[d])
        for element in keys:           
            if word+element < num:
                word_check.append(word+element)
            while len(word_check) > 0:
                x= word_check.popleft()
                c,n = prefix_finder(secondary_trie,x)
                if c == False:
                    return False
          
        for thing in new_dicts:
            while True:
                keys = current_dict.keys()
                new_dicts = []
                for d in keys: # this saves all the other dictionaries we need to iterate through
                    new_dicts.append(current_dict[d])
                for element in keys:           
                    if word+element < num:
                        word_check.append(word+element)
                    while len(word_check) > 0:
                        x= word_check.popleft()
                        c,n = prefix_finder(secondary_trie,x)
                        if c == False:
                            return False
            
    return True

answer = []
for word in s:
    check,num = prefix_finder(my_trie,word)
    if check == False:
        add_to_trie(word,my_trie)
        answer.append(word)   
    else:
        check,num = prefix_finder(secondary_trie,word)
        num-=1
        if check == False:
            add_to_trie(word,secondary_trie)
        else: # expanding on above, we found an intermediate, now we can add to main list, then delete the intermediate
            if exhaustive_check(word,my_trie,secondary_trie,num):
                remove_from_trie(secondary_trie,word)
                answer.append(word)
            else: # our exhaustive search failed delete old word, replace with new word
                remove_from_trie(secondary_trie,word)
                add_to_trie(word,secondary_trie)          
total = 0
for element in answer:
    for ch in element:
        total+= ord(ch)            
print answer        
print total   

        
