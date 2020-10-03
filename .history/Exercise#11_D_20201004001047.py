#!/usr/bin/python3

def sort_sum_list(args):  
    return (args, key=sum)

print (sort_sum_list([[2,3,4,5], [2,1,9], [2,9,9,9], [1,1,1,1]]))