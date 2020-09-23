#!/usr/bin/python3

def average_inlist (*numbers): 
    n = 0
    for i in numbers: 
        n+=i
    n = n/len(numbers)
    print (f'average = {numbers}')