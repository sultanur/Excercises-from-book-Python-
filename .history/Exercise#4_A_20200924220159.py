#!/usr/bin/python3
from decimal import Decimal 

def hex_output(in_hex):
    out_in_dig = 0
    for index, one_digit in enumerate(reversed(in_hex)):
        print(f'{index} : {one_digit}')
        out_in_dig += ((16**index) * one_digit)
        print (out_in_dig)



print(hex_output(50))

