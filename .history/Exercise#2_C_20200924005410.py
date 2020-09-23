#!/usr/bin/python3

def average_list (*numbers): 
    n = 0
    for i in numbers: 
        n+=i
    n = n/len(numbers)
    print (f'average = {numbers}')
    
    average_list(*[10,20,30,40])