#!/usr/bin/python3
from collections import Counter
import operator
 
def most_repeated_vowels(word): 
    total_vowels = ''
    for letter in word.lower():     
        if letter in 'aeuoi':    
           total_vowels += letter 
           #print(total_vowels)   
    return Counter(total_vowels).most_common(1)[0][1]
    
def most_repeatedvowel_word(words):    
    return max(words, key=most_repeated_vowels)

list_words = ['this', 'is', 'an', 'elementary', 'test', 'example']    

print( most_repeatedvowel_word(list_words))
    