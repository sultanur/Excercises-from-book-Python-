#!/usr/bin/python3

def my_sum(*arg, start = 0): 
    output = start
    for i in arg: 
        output += i
    return output
print (my_sum(*[10,20,30]))