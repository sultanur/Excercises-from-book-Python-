#!/usr/bin/python3

def average (*numbers): 
    n = 0
    for i in numbers:        
        n+=i
        print(n)
    
    n = n/len(numbers)
    return n
    
   
print(average(*[10,20,30,40]))