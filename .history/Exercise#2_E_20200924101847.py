#!/usr/bin/python3

def sum_obj(obj): 
    if not type(obj) is int: 
        raise TypeError("Object is not int")
    else: 
        for one_obj in obj:  
            return sum(one_obj)
  
print(sum_obj([2, 4]))
