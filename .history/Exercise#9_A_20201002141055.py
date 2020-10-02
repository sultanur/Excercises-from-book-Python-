#!/usr/bin/python3
def firstlast(sequence):   
    return sequence[:1] + sequence[-1:]

print(firstlast('abcdef'))
print(firstlast([1,2,3,4,5,6,7,8]))
print(firstlast(1,2,3,4,5,6,7,8,9))  