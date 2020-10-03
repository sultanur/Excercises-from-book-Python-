#!/usr/bin/python3
import collections
def count_vowels(word): 
    total = 0 
    for letter in word.lower():   
        if letter in 'aeiou':   
            total +=1
    return total

def sort_by_vowels(words):
    return (sorted(words, key=count_vowels))
    
            

print(sort_by_vowels(["hello", "Monday", "successful", "administration", "day"]))