# Write your code here :-)
#! python 3.8
# multiplicationquiz.py #finding out multiplication
"""
import random,time

totalQ = 10
correct = 0

for i in range(1,totalQ+1):
    a=1
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    ans = num1*num2
    #sleep = time.sleep(8)
    #print(sleep)
    user = int(input('#%s %s*%s = ' % (i,num1,num2)))
    #if time.sleep(9):
    #    print('Out of time')
    #else:
        #print(user)
    if user != ans:
        while a<3:
            print('Incorrect Answer')
            user = int(input('#%s %s*%s = ' % (i,num1,num2)))
            a+=1
        else:
            print('Out of chances.Moving to the next Q ')

    else:
        print('Correct answer')
        correct+=1
    time.sleep(0.5)

print('Your score : %s/%s ' % (correct,totalQ))
"""

import random,time

totalQ = 10
correct = 0

for i in range(1,totalQ+1):
    a=1
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    ans = num1*num2
    #sleep = time.sleep(8)
    #print(sleep)
    user = int(input('#%s %s*%s = ' % (i,num1,num2)))
    while not time.sleep(9):
        if user != ans:
            while a<3:
                print('Incorrect Answer')
                user = int(input('#%s %s*%s = ' % (i,num1,num2)))
                a+=1
            else:
                print('Out of chances.Moving to the next Q ')

        else:
            print('Correct answer')
            correct+=1
        time.sleep(0.5)

    else:
        print('Out of time')


print('Your score : %s/%s ' % (correct,totalQ))


