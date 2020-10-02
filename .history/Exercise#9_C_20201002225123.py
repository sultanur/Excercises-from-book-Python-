#!/usr/bin/python3

def even_odd_sums(numbers):
    for num, i in enumerate(numbers):
        res = i + (i+1)
        print(i ,' on ', num)
        print(res)        
   
#print(even_odd_sums((10, 20, 30, 40, 50, 60)))
print(even_odd_sums([10, 20, 30, 40, 50, 60]))