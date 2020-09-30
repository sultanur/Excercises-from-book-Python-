#!/usr/bin/python3

def longest_word_file():   
    words = (open("random.txt", 'r').read().split())
    max_len = len(max(words, key=len))
    return [len(word) for word in words if len(word) == max_len]

    
print(longest_word_file())
