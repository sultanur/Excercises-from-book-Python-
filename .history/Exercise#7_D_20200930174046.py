#!/usr/bin/python3
import string
def URL_encode_chars(url_encoded_str):
    output = []
    stand_word = string.ascii_letters+ string.digits
    for one_char in url_encoded_str: 
        if one_char in stand_word:   
            output.append(one_char)
        else:   
            output.append(hex(ord(one_char)).replace('0x', '%20'))  
            
    return output

print(URL_encode_chars('https://www.w3schools.com/python/ref_string_split.asp   '))
           
    