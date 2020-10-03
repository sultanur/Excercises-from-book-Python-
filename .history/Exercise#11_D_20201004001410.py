#!/usr/bin/python3
def sum_elem_lists(numbers_inlist):   
    total = 0
    if not numbers_inlist:   
        return numbers_inlist
    for num in numbers_inlist:    
        total += num
    
    return total

def sort_sum_list(list_of_list):  
    return sorted(list_of_list, key=sum_elem_lists)

print (sort_sum_list([[2,3,4,5], [2,1,9], [2,9,9,9], [1,1,1,1]]))