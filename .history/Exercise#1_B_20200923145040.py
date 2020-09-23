#!/usr/bin/python3
import random

def guessing_game(): 
    base_random = random.choice([2, 8, 10, 16])
    answer = random.randint(0,100)
    print(base_random) 
    while True: 
        user_guess = int(input("Enter your guess: "), base_random)
        if user_guess == answer: 
            print(f'Just right! answer is {user_guess}')
            break
        if user_guess < answer: 
            print(f'The guess number {user_guess} is too low, try again ')
        else: 
            print(f'The guess number {user_guess} is so high, try again')
            
    guessing_game()
    
    