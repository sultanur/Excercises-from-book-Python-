#!/usr/bin/python3
from decimal import Decimal 

def hex_output(in_hex): 
    for index, one_digit in enumerate(reversed(in_hex)):
        print(f'{index} : {one_digit}')
        output_in_hex = sum(16**index)
        index +=1



print(hex_output('50'))

