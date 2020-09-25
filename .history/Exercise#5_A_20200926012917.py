#!/usr/bin/python3
def is_vowel(word): 
    
        if word[0] == vowel: 
            return True 
        

def into_pig(): 
    my_word = input("Enter any word in English ")
    if my_word[0] in 'aeiou': 
        return f'{my_word} way'
    else: 
        return f'{my_word[1:]}{my_word[0]}ay'
        
    
         
print(into_pig())
    
