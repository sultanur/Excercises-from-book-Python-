#!/usr/bin/python3
from decimal import Decimal 

def hex_output(in_hex): 
    for index, one_digit in in_hex: 
        print(f'{index} : {one_digit}')



print(hex_output('0x50'))

