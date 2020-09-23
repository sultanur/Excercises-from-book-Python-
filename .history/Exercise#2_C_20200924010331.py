#!/usr/bin/python3

def average (*numbers): 
    n = 0
    for i in numbers:        
        n+=i
        print(n)
    
    n = n/len(numbers)
    return n
    
   #return sum(numbers) / len(numbers) #another version by using built-in functions sum() and len()
print(average(*[10,20,30,40]))