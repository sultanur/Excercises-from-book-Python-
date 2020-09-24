#!/usr/bin/python3
from decimal import Decimal 

def hex_output(in_hex):
    out_in_dig = 0
    for index, one_digit in enumerate(reversed(in_hex)):
        #print(f'{index} : {one_digit}')
        if one_digit == 'a':  
            one_digit = 10
        elif one_digit == 'b':            
            one_digit = 11
        elif one_digit == 'c': 
            one_digit = 12
        elif one_digit == 'd': 
            one_digit = 13
        elif one_digit == 'e': 
            one_digit = 14
        elif one_digit == 'f': 
            one_digit = 15
        out_in_dig += ((16**index) * int(one_digit))
    print (out_in_dig)



hex_output('4a')

