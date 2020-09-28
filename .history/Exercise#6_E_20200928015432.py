#!/usr/bin/python3

def ubbi_dubbi (word):
    output = [] 
    for letter in word: 
        if letter in 'aeiou': 
            return  output.append(f'ub {letter}')
        else: 
            return output.append(letter)
        
print (ubbi_dubbi('milk'))
