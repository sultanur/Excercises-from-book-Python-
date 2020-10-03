#!/usr/bin/python3
def sort_absvalues(numbers):
     return sorted(numbers, key=abs)  
 
print(sort_absvalues([4,8,-2,-10,-22,3,9])) 
    