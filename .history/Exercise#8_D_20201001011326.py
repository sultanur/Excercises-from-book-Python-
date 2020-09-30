#!/usr/bin/python3

def longest_word_file():   
    text = (open("random.txt", 'r').read().split())
    print(text)

    
print(longest_word_file())
