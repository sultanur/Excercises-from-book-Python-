#!/usr/bin/python3
from decimal import Decimal 

def hex_output(in_hex):
    out_in_hex = 0 
    for index, one_digit in enumerate(reversed(in_hex)):
        print(f'{index} : {one_digit}')
        out_in_hex = 16**index
        print (out_in_hex)



print(hex_output('50'))

