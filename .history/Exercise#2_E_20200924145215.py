#!/usr/bin/python3

def is_int(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False


def sum_ints(items):
    return sum(is_int(one_item)
               for one_item in items)

my = ('2', 5, 'a')   
print(sum_ints(my)) 