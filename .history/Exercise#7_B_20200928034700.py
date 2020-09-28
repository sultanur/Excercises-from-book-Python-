#!/usr/bin/python3

#!/usr/bin/python3
import string

def ubbi_dubbi_capitalized(word):
    output = ''
    
    for letter in word: 
        
        if letter in 'aeoui': 
           new_word = (f'ub{letter}')
           output += new_word
        else: 
            new_word = letter
            output += new_word
        
        if letter[0] in string.ascii_uppercase:
            output = output[0:1].capitalize() 
              
        
            
    return output
        
print(ubbi_dubbi_capitalized('Elephant