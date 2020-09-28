#!/usr/bin/python3

import string
import re

def edit_file ():        
        text_in_lines = open("names.txt", "r").read()
        pattern = '[0-9.]'
        list = [re.sub(pattern, '', i) for i in text_in_lines]
       
        open("new_file.txt", "w").writelines(list)
        print(open("new_file.txt", "r").read())
        
edit_file()
