#!/usr/bin/python3
import random

def guessing_game():
    n = 2    
    #answer_base = random.choice([2, 8, 10, 16])
    answer = random.randint(0, 100)
    while n >= 0:
        n -= 1
        user_guess = int(input("Enter your guessing number: "))
        
        if (answer == user_guess): 
            print("Just right ")
            break
        
        if answer < user_guess:          
            print (f'Your guess {user_guess} is too high')                    
        else:            
            print(f'Your guess of {user_guess} is too low ')
    else: 
        print("Your three chances are up!")       
            
guessing_game()
