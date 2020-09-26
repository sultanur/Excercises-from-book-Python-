#!/usr/bin/python3
import string


def two_vowels(my_word): 
    number_vowels = len(set(my_word) & set('aeiou'))
    if number_vowels > 1: 
        return f'{my_word} way'
    else: 
        return f'{my_word[1:]}{my_word[0]}way'
        
print(two_vowels('nara'))
     
    