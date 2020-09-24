#!/usr/bin/python3

def sum_obj(obj): 
    s = 0
    if not type(obj) is int: 
        raise TypeError("Object is not int")
    else: 
        s += obj
        return s
    
print(sum_obj("23, 45, 67"))
