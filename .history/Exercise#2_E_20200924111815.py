#!/usr/bin/python3



def is_intable(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False

is_instable(one_item)
def sum_intable(items):
    return sum(is_instable(one_item)
               for one_item in items)
my = [2, 4, 7]   
print(sum_intable(my))