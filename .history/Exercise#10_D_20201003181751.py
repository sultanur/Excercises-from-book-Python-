#!/usr/bin/python3
def combine_dicts(*args):    
    output = {}
    for d in args:   
        for key, value in d.items():   
            if key in output:   
                try:   
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
                    
            else:   
                output[key] = value
                
            return output
        
print (combine_dicts({'foo': 12, 'bar': 14}, {'moo': 52, 'car': 641}, {'doo': 6, 'tar': 84}))       