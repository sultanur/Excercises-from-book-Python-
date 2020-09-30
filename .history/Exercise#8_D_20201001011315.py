#!/usr/bin/python3

def longest_word_file():   
    text = (open("random.txt", 'r').read().split())
    print(text)
    return (sorted(text.split()))[-1]
    
print(longest_word_file())
