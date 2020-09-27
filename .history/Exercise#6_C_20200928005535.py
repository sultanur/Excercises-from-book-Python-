#!/usr/bin/python

def transpose_str(list_of_words): 
    return [' '.join(transposed) for transposed in  (zip(*[s.split() for s in list_of_words]))]
    

       
    
print(transpose_str(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))