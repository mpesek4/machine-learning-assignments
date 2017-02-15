

'''
This program takes in a list of word and creates a subset of those words that hold the following properties:
    1. no words in the subset are prefix neighbors IN **THE ORIGINAL SET** ie, [a,ab,abc]
      a,abc is a proper subset because although a is a prefix neighbor of abc, ab is inbetween in the original set
     2. the ordinal sum of the subset is maximized, ie no better solution
     
     prefix neighbor definition:  A and C are prefix neighbors if A is a prefix of C and
                     if no B exists in original set, where A is a prefix of B
                 and B is a prefix of C.

'''
from sets import Set
from collections import deque
_end = '_end_'
with open("input_file.txt") as f:
  n = int(f.readline().strip())
  s = f.readline().strip().split(' ')

s.sort(lambda x,y: cmp(len(y),len(x)))
my_trie = dict()
secondary_trie = dict()
# method that creates a dictionary
def add_to_trie(word, my_trie):
    current_dict = my_trie
    for char in word:
        current_dict = current_dict.setdefault(char,{})                                    
    current_dict[_end] = _end
    return my_trie
    

def dfs(my_trie, current_color,current_word, answer, flag):
    # DFS is practical because we always add the longest word on any branch,
    # then skip prefix neighbors through a coloring process,
    # since this coloring can be overrided by other branches coloring, we store words we KNOW
    # cannot be in our answer in a hashmap so that a less optimal branch doesn't re-color a node
    # that has already been deemed inappropriate
    keys = my_trie.keys()
    if len(keys)==1 and keys[0] == '_end_':
        answer.append(current_word)
        return 'red'  
    for element in keys: # standard DFS loop
        if element == '_end_':
            continue
        current_word+=element
        color= dfs(my_trie[element], current_color,current_word,answer,flag)
        current_word = current_word[:-1]
        if color == 'red': # depending on which branch is explored, colors may be overridden
                        # if any branch returned a red though, we know we can't add the word as it is a prefix
                        # neighbor of one of the branches, we flag it in a hasmap to make sure we don't add it
                        flag[current_word] = True

    if color == 'black' and '_end_' in keys: # we only add nodes that have the black color passed down to them
                                # if at any point a red was passed down it was flagged and we dont add it
        if current_word not in flag:
            answer.append(current_word)
            return 'red'
        else:
            return 'black'
    elif color == 'red' and '_end_' in keys: # if we find a node that is inappropriate, we return black
                                            # because we have found an in between node that makes the next candidate
                                        # appropriate
                                        # example ABCDEF was chosen, if we find ABCD it is inapproriate, but then ABC
                                        # will be passed black and be deemed appropriate
        return 'black'
    elif color == 'black' and current_word in flag: # if we add an appropriate node, the next prefix will be deemed
    # inapprorpriate, example ABCD is added, ABC will be passed RED, then AB will be passed BLACK
        return 'red'
    else:
        return color
    
        
for word in s:
    add_to_trie(word,my_trie)    
        
answer = []        
root_lvl = my_trie.keys()
flagmap = {}
for element in root_lvl:
    dfs(my_trie[element],'black',element,answer,flagmap)

total = 0
for element in answer:
    for ch in element:
        total+= ord(ch)            
print answer    
print total   

        
