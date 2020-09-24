#!/usr/bin/python3
from  decimal import Decimal

def add_decimal(s1, s2): 
    return float(Decimal(s1) + Decimal(s2))

print(add_decimal('23.4', '14.7'))