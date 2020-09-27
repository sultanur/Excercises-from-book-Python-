#!/usr/bin/python3
def ips_for_404s (): 
    for one_line in open(filename): 
        if ' 404 ' in one_line: 
            print(one_line.split()[0])
            
ips_for_404s()