#!/usr/bin/python3
from collections import Counter
import operator
 
def most_repeated_vowels(word): 
    total_vowels = ''
    for letter in word.lower():     
        if letter in 'aeuoi':    
           total_vowels += letter    
    return Counter(total_vowels).most_common
    

print(most_repeated_vowels('elementary'))
    