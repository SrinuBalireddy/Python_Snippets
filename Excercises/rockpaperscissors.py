# Write your code here :-)
#! python3.8
# rockpaperscissors.py - Game
"""
#####Rules########
rock beats scissors
scissors beats paper
paper beats rock
"""

"""
Ask user to pick an option (rock paper scissors)
generate a random number and assign rock paper scissors values to 0,1,2 respectively
compare the game logic and display the winner
"""

import random
user=''
computer=''

print("Let's play rock paper scissors game")

def comvalue():
    for i in range(1,4):
        if i==1:
            computer='r'
            print('Rock')
        if i==2:
            computer='p'
            print('Paper')
        if i==3:
            computer='s'
            print('Scissor')

comvalue()
