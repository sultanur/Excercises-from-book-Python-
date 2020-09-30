#!/usr/bin/python3

def longest_word_file():   
    words = (open("random.txt", 'r').read().split())
    max_len = len(max(words, key=len))
    return [(word) for word in words if len(word) == max_len]

def main():       
    print(longest_word_file())
    print (len(longest_word_file()))
