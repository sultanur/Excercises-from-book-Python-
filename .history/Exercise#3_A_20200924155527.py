#!/usr/bin/python3


def run_timing(): 
    sum_runs = 0
    n = 0
    while True: 
        my_time = input(float("Enter 10  km run time: "))
        print(f'Enter 10  km run time: {my_time}')
        sum_runs += my_time
        n +=1
average = sum_runs/n 
print(f'Average of {average}, over {n} runs')
    