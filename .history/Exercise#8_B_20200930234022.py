#!/usr/bin/python3

def split_sort_str(some_str):  
    return ''.join((sorted((some_str).split())))

print(split_sort_str('Tom Dick Harry'))