#!/usr/bin/python3
import string

def into_pig(): 
    my_word = input("Enter any word in English ")
    if my_word[0] in 'aeiou': 
        result = f'{my_word} way'
    else: 
        result = f'{my_word[1:]}{my_word[0]}ay'
    
    if my_word[0] in string.ascii_uppercase:
        result = result.capitalize()
    return result   
    
         
print(into_pig())
    
