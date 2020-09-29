#!/usr/bin/python3
import string

def remove_name(text, names):   
    output = text
    for one_name in names:   
        output = output.replace(one_name, '_'*len(one_name))
        print(one_name)
        print(output)
    return output

remove_name("William Shakespeare  was an English playwright, Emily Dickinson was born in Amherst, Emily Dickinson was born in Amherst, Sir Arthur Conan Doyle KStJ DL (22 May 1859 – 7 July 1930) was a British writer, Count Leo Tolstoy,  usually referred to in English as Leo Tolstoy, was a Russian writer", ["William Shakespeare", "Emily Dickinson"
"Arthur Conan Doyle", "Leo Tolstoy" ])