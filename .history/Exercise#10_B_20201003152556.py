#!/usr/bin/python3
def mysum_bigger_than(*items):  
    if not items:   
        return items   
    output = items[0]
    for item in items[1:]:   
        if items[0] =< item: 
            output +=item
        else:   
            continue
    return output
    
print(mysum_bigger_than(5, 5, 20, 30, 60)) 
        