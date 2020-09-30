#!/usr/bin/python3

def last_word_file():   
    text = open("random.txt", 'r').read()
    return (sorted(text.split()))[-1]
    
print(last_word_file())
