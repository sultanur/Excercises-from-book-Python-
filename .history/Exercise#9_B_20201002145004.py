#!/usr/bin/python3
def odd_even_summ(numbers):
    print(numbers[2:2:2])     
    return numbers[0:1:2]+ numbers[2:2:2]

print(odd_even_summ([1,2,3,4,5,6,7,8]))
      
