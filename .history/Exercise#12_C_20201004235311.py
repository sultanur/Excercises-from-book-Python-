#!/usr/bin/python3
from collections import Counter
import operator

def popular_shell(filename):   
    shells = Counter(line.split(':')[-1].strip() 
                     for line in open(filename, 'r').readlines()
                     if not line.startswith(("#", "\n")))
    print(shells)
    return sorted(shells.items(), key=operator.itemgetter(1))
   

print(popular_shell('newfile.txt'))