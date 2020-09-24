#!/usr/bin/python3

def sum_obj(obj): 
    if not type(obj) is int: 
        raise TypeError("Object is not int")
    else: 
        for one_obj in obj:  
            return sum(one_obj)
objects = ["34", "45", "56", "77"]   
print(sum_obj(objects))
