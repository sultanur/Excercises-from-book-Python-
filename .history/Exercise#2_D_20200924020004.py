#!/usr/bin/python3

def lengths_words(str):
    word_lengths = [len(one_word) for one_word in str]
    #print(word_lengths)
    return [min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)]
    
    
lengths_words(['hi', 'hello', 'Friday'])
    