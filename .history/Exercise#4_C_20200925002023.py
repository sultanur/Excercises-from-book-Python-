#!/usr/bin/python3
def name_triangle(): 
    my_name = input("Enter your name:")
    for i in range(len(my_name)): 
        print(my_name[:i+1])
        
name_triangle()