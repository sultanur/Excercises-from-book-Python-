#!/usr/bin/python3
import collections

def sort_by_vowels(words):
    for word in words:   
        if word in 'aouie':      
            len_vowels = Counter(word)
    
            return sorted(words, key=len_vowels)

print(sort_by_vowels(["hello", "today", "was", "great", "day"]))