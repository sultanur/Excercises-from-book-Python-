#!/usr/bin/python3


def run_timing(): 
    sum_runs = 0
    number_runs = 0
    while True: 
        one_run = input("Enter 10  km run time: ")
        if not (one_run): 
            break
        print(f'Enter 10  km run time: {one_run}')
        sum_runs += float(one_run)
        number_runs +=1
    
    average_runs = sum_runs/number_runs 
    print(f'Average of {average_runs}, over {number_runs} runs')
    