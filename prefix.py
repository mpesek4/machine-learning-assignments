

import sys
from sets import Set
from collections import deque
_end = '_end_'
with open("input_file") as f:
  n = int(f.readline().strip())
  s = f.readline().strip().split(' ')
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
    if num == 1:
        return True
    if len(word) == 1:
        return True
    search_structure = (my_trie[word[0]],word[0]+word[1])
    
    
    my_deque = deque() # need to do a depth first search of my nested dictionaries to check if relevant comboes are in secondary_d
    my_deque.append(search_structure) # this is the head of the search, 

    while len(my_deque) > 0:
        head = my_deque.pop()       
        current_dict = head[0]
        search_word = head[1]
        check,num = prefix_finder(secondary_trie,search_word)       
        if check == False:
            return False            
        if len(head[1]) < num:                           
              for element in current_dict.keys():  
                  current_dict = current_dict.get(element, None)
                  if current_dict is not None:
                      for k in current_dict.keys():                         
                          my_deque.append((current_dict, search_word+k))
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
            if exhaustive_check(word,my_trie,secondary_trie,num-1):
                remove_from_trie(secondary_trie,word)
                answer.append(word)
            else: # our exhaustive search failed delete old word, replace with new word
                remove_from_trie(secondary_trie,word)
                add_to_trie(word,secondary_trie)          
total = 0
for element in answer:
    for ch in element:
        total+= ord(ch)            
    
print total   

        
