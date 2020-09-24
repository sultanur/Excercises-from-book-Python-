#!/usr/bin/python3

def out_digit(): 
    out_dec = 0
    input_hex = input("Enter hex value: ")
    for index, one_digit in enumerate(reversed(input_hex)): 
        if 48 <= ord(one_digit) <= 57: 
            decim_dig = ord(one_digit) - 48
        elif 97 <= ord(one_digit) <= 102: 
            decim_dig = ord(one_digit) - 87            
        
        out_dec += decim_dig * (16 ** index)
    
    print (out_dec)
        
out_digit()