# David Vilhena Klein
# 26.10.2023
# Spelling correction
# Lab 15 on http://programarcadegames.com

import re
 
# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

dictionary_list = open(".\pygame\lab15\dictionary.txt")
dictionary_array = []
#put every word in a list
for line in dictionary_list:
    line=line.strip()
    dictionary_array.append(line)
dictionary_list.close

print("--- Linear Search ---")
text = open(".\pygame\lab15\AliceInWonderLand200.txt")
i=1 #line index
for line in text:
    wordsinline = split_line(line)
    for word in wordsinline:
        if dictionary_array.count(word.upper()) == 0:
            print("Line",i, ":", word, "is not in the dictionary.")
    i+=1
text.close()

#-------------Binary Search --------------------------

# Copied out of Worksheet 15
def binary_search(list, number): #number is the element to find
    upper_bound=len(list)-1 #upper bound is the greatest list index
    lower_bound=0 #lower bound is the first element
    done=False #running variable
    while lower_bound <=upper_bound and done==False: 
        middle_pos=(lower_bound + upper_bound)//2 #Set middle_pos inbetween bounds
        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if number < list[middle_pos]:
            upper_bound = middle_pos - 1
        elif number > list[middle_pos]:
            lower_bound = middle_pos + 1
        else:
            done=True
    if done == True:
        return middle_pos
    else:
        return (-1)
#

print("--- Binary Search ---")
text = open(".\pygame\lab15\AliceInWonderLand200.txt")
i=1 # line index
for line in text:
    wordsinline = split_line(line)
    for word in wordsinline:
        if binary_search(dictionary_array, word.upper()) == -1: #use the binary search function
            print("Line",i, ":", word, "is not in the dictionary.")
    i+=1
text.close()

