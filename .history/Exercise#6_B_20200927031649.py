#!/usr/bin/python3

def word_per_line(): 
    output = []
    file = open("Lorem_Ipsum.txt", "r")
    for n,  line in enumerate(file): 
        words_in_line = line.split()
       
        if not words_in_line: 
            continue
        
        if n >= 10: 
            break
        
        if n >=len(words_in_line):
            output.append(words_in_line[-1])
        else:
            output.append(words_in_line[n])
            
    return ' '.join(output)
             
        
print(word_per_line())
        
    
    