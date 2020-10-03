#!/usr/bin/python3
from operator import itemgetter

def alphabetize_names(dict_phonebook):    
    return sorted (dict_phonebook, key= itemgetter(1))

def main(): 
    PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
                {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
                {'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}]
    print(alphabetize_names(PEOPLE))