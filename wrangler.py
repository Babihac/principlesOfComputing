"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
codeskulptor.set_timeout(100)
import poc_wrangler_provided as provided
import math

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    res = []
    curr_elem = list1[0]
    res.append(curr_elem)
    for i in range(1,len(list1),1):
        if list1[i] == curr_elem:
            curr_elem = list1[i]
            continue
        curr_elem = list1[i]
        res.append(curr_elem)
    return res
        

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    res = []
    index1 = 0
    index2 = 0
    for i in range(len(list1)):
        if list1[index1] == list2[index2]:
            res.append(list1[index1])
            index1 += 1
            index2 += 1
        elif list1[index1] < list2[index2]:
            index1 += 1
        else:
            index2 += 1
        if index1 >= len(list1) or index2 >= len(list2):
            break
       
    return res

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    res = []
    index1 = 0
    index2 = 0
    while index1 <= len(list1) and index2 <= len(list2):
        if index1 == len(list1) :
            while index2 < len(list2):
                res.append(list2[index2])
                index2 += 1
            break
            
        elif index2 == len(list2) :
            while index1 < len(list1):
                res.append(list1[index1])
                index1 += 1
            break
        else:
            if list1[index1] < list2[index2]:
                res.append(list1[index1])
                index1 += 1
            else:
                res.append(list2[index2])
                index2 += 1
    return res
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) == 1:
        return list1
    middle = len(list1)/2
    arr1 = merge_sort(list1[0:middle])
    arr2 = merge_sort(list1[middle:])
    res = merge(arr1,arr2)
    return res

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [word]
    else:
        first = word[0]
        without_first = gen_all_strings(word[1:])
        res = []
        res.append(first)
        for ch in without_first:  
            res.append(ch)
            for i in range(len(ch)+1):
                res.append(ch[0:i]+first+ch[i:])
        return res

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    res = []
    for line in netfile.readlines():
        res.append(line[:-1])
    return res

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()
test1 = [1]
test2 = [0]
test3 = ['parno']
all_words =  gen_all_strings("tac")
sorted_a = merge_sort(all_words)
res = remove_duplicates(sorted_a)        
    
    
    
    