#!/usr/bin/python3
def even_odd_sums(numbers):
    odds = (numbers[1::2])        
    evens =(numbers[0::2])
    return sum(evens), sum(odds)

print(even_odd_sums((10, 20, 30, 40, 50, 60)))
print(even_odd_sums([10, 20, 30, 40, 50, 60]))