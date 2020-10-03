#!/usr/bin/python3
import operator 
PEOPLE = [{'first':'Barack', 'last':'Obama',
           'email':'president@whitehouse.gov'},
          {'first':'Vladimir', 'last':'Putin',
           'email':'president@kremvax.ru'},
          {'first':'Reuven', 'last':'Lerner',
           'email':'reuven@lerner.co.il'}
          ]

def alphabetize_names(list_of_dicts):   
    return sorted(list_of_dicts, key= operator.itemgetter('last', 'first'))
    


print(alphabetize_names(PEOPLE))