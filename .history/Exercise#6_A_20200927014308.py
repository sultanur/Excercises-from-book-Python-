#!/usr/bin/python3



def pl_sentence (sentence): 
    output = []
    punctuation = ''
    for word in sentence.split():
        if word[-1] in '?!.,':
            punctuation = word[-1] 
            word = word[:-1]
            if word[0] in 'aeiou':
                output.append(f'{word}way' + punctuation)
            else:
                output.append(f'{word[1:]}{word[0]}ay' + punctuation)
        
        elif word[0] in 'aeiou':
            output.append(f'{word}way')     
        else:
            output.append(f'{word[1:]}{word[0]}ay')
            
    
    return ' '.join(output)
   


print(pl_sentence("Hi Nuray, How was your day?"))        