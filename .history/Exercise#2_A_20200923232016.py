#!/usr/bin/python3

def my_sum (*number): 
    n = 0
    for i in number: 
        n+=i
    return n

print(my_sum(100, 200, 300))
        
    