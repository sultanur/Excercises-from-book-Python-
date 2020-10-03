#!/usr/bin/python3
def sum_numeric(*items):    
    total = 0
    for item in items:
        try:     
            total += int(item)
        except ValueError:   
            pass
        
    return total
        
    
    

print(sum_numeric(10, 20, 'a', '30','bcd'))