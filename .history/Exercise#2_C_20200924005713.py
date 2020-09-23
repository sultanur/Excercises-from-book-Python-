#!/usr/bin/python3

def average (*numbers): 
    n = 0
    for i in numbers:        
        n+=i
    n = n/len(numbers)
   
print(average(*[10,20,30,40]))