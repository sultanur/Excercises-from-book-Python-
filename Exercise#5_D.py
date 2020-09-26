#!/usr/bin/python3
import string

def punctuation(my_word): 
    punctuation = ''
    if my_word[-1] in '!.:,?':
        punctuation = my_word[-1]
        my_word = my_word[:-1] 
        print(f'{my_word[:-1] }')
        print(my_word)
        print(punctuation)
        
        
        
        
    if my_word[0] in 'aeiou': 
        result = f'{my_word} way'+punctuation
    else: 
        result = f'{my_word[1:]}{my_word[0]}ay'+punctuation
        
    return result   
    
         
print(punctuation('wine!'))