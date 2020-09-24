#!/usr/bin/python3



def is_intable(one_item):
    try:
        int(one_item)
        return True
    except ValueError:
        return False


def sum_intable(items):
    return sum(is_intable(one_item)
               for one_item in items)
my = ('a', 'a', 'a')   
print(sum_intable(my)) 