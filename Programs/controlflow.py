# Write your code here :-)
"""
name='Srinu'
pwd='Password1'
if name=='Srinu':
    print('Hello '+name)
    if(pwd =='Password'):
        print('Your password is: '+pwd)
    else:
        print('Wrong Password')

spam = 1
while spam <5:
    print(spam)
    spam= spam+1


----------------------------------------------------------------
# break and continue

while True:
    print('who are you')
    name=input()
    if name != 'Srinu':
        continue
    print('Hello Srinu, welcome''Whats the password')
    pwd = input()
    if pwd=='xyz':
        break
print('Access Denied')


--------------------------------------------------------------------
#truthy and falsy values

name=''
while not name:
    print('enter your name')
    name=input()
print('How many guests?')
guests = int(input())
if guests:
    print('ensure enough space is avaialable')
print('done')

name=''
while not name:
    print('enter your name')
    name=input()
print('Enter number of guests?')
guests = int(input())
if guests:
    print('have enough space')
print('done')

--------------
for i in range(5,-10,-2):
    print(i)
-----------------

import random
number = random.randint(1,10)
print(number)

---------------------------------------

#guess the number

from random import *
print('Guessing game')
secret = randint(1,50)
print(secret)
print('Guess a number between 1 and 50')
guess = int(input())
while guess != secret:
    if guess >secret:
        print('Guess a smaller number:')
        guess = int(input())
    elif guess < secret:
        print('Guess a bigger number:')
        guess = int(input())


print('Whoaa!! you guesses it right')


from random import *
print('Guessing game')
secret = randint(1,50)
print(secret)
print('Guess a number between 1 and 50')
guess = int(input())
i=0
while i<4:
    if guess >secret:
        print('Guess a smaller number:')
        guess = int(input())
        i+=1
    elif guess < secret:
        print('Guess a bigger number:')
        guess = int(input())
        i+=1
    else:
        break

if guess == secret:
    print('Whoaa!! you guesses it right')
else:
    print('you ran out of chances')
------------------------------------------------

print('enter a number')
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')

--------------------------------------------
"""

for i in range(1,11):
    print(i)

a=1
while a<11:
    print(a)
    a+=1
