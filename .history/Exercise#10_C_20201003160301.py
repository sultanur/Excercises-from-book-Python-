#!/usr/bin/python3
def sum_numeric(*items):    
    output = items[0]
    for item in items:
        if int(item) == True:     
            output += (item)
        else:   
            continue
        
    return output
        
    
    

print(sum_numeric(10, 20, 'a', '30','bcd'))