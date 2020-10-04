#!/usr/bin/python3
from collections import Counter
import operator

def get_shell(string):   
    return string.split(':')[-1]


def popular_shell_count (filename):   
    for line in open(filename, 'r').readlines():
        shells = Counter((line.split(':')[-1]).strip()).most_common(1)[0][1]
        print(shells)
         
        
    #return max(content, key=get_shell)

popular_shell_count('newfile.txt')