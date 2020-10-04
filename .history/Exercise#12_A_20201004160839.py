#!/usr/bin/python3
from collections import Counter
import operator

list_words = ['this', 'is', 'an', 'elementary', 'test', 'example']    

def most_repeating_letter(word):    
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):    
    return max(words, key=most_repeating_letter)

print(most_repeating_word(list_words))