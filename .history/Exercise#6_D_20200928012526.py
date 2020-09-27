#!/usr/bin/python3
"""Given the name of an Apache logfile,
print the IP address where the response code
is 404"""
def ips_for_404s (): 
    for one_line in open(filename): 
        if ' 404 ' in one_line: 
            print(one_line.split()[0])
            
ips_for_404s()