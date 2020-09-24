#!/usr/bin/python3

def lengths_words(str):
    word_lengths = [len(one_word) for one_word in str]
    print(word_lengths)
    
lengths_words(['hi', 'hello', 'Friday'])
    