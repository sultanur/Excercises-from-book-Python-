#!/usr/bin/python3

def even_odd_sums(numbers):
    odds = (numbers[1::2])        
    evens =(numbers[2::2])
    res = numbers[0] + sum(odds) - sum(evens) 
    return res    
   
print(even_odd_sums((10, 20, 30, 40, 50, 60)))
print(even_odd_sums([10, 20, 30, 40, 50, 60]))

    
