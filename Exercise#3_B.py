#!/usr/bin/python3
def place_floats (ffl, before, after): 
    to_str = str(ffl)
    indexx = to_str.index('.')
    return to_str[indexx - before:indexx+after+1]

print(f'{place_floats (1234.5678, 2,3)}')
    