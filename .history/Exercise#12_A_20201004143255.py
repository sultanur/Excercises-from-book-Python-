#!/usr/bin/python3
import collections

def most_repeating_words(words):
    return sorted(words, key=max(Counter(words).most_common(1)))   


words = ['this', 'is', 'an', 'elementary', 'test', 'example']    
print(most_repeating_words(words))