#!/usr/bin/python3

def average (*numbers): 
    n = 0
    average = 0
    for i in numbers:        
        n+=i
        print(n)
    average = n/len(numbers)
   
print(average(*[10,20,30,40]))