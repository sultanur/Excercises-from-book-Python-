#!/usr/bin/python3
import collections

def most_repeating_words(words):
    return sorted(words, key=Counter(words).most_common(1))   
    