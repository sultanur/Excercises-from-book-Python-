#!/usr/bin/python3
from collections import Counter
import operator

def popular_shell(filename):   
    shells = Counter(line.split(':')[-1].strip() 
                     for line in open(filename, 'r').readlines()
                     if not line.startswith("#", "\n"))
    return sorted(shells.item(), key=operator.itemgetter(1), reverse=True)
   

print(popular_shell('newfile.txt'))