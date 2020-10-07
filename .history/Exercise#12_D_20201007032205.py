#!/usr/bin/python3
import operator

def format_sort_records(list_of_tuples):   
    output = []
    template ={1:10} {0:10} {2:5.2f}
    for person in sorted(list_of_tuples. key=operator.itemgetter(1, )):   
        output.append(template.format(*person))
    return output

    