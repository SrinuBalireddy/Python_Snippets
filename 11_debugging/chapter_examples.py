# Write your code here :-)

"""
#example#1

def box(symbol, width , height):

    if len(symbol)!=1:
        raise Exception('Symbol must be a single character string')
    elif width >5:
        raise Exception('Width must be lesser than 5')
    elif height <2:
        raise Exception('Height must be greater than 2')

    print(symbol+str(width+height))

try:
    box('3',4,4)
except Exception as err:
    print('An exception happended: '+str(err))

"""

#example 2
"""
import traceback

try:
    raise Exception('This is the error message')
except:
    errorfile = open('errorinfo.txt','w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('The traceback info was written to errorfile.txt')
"""

#example 3 - factorial
"""
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(6))

import logging
#logging.basicConfig(level=logging.DEBUG, format =' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename ='mylog.txt' ,level=logging.DEBUG, format =' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug('Start of a program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total =1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is '+ str(i)+', total is '+str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
"""

#example 4 - debuguing
"""
print('Enter the first number')
num1 = input()
print('Enter the second number')
num2 = input()
print('The sum is '+ num1 + num2)
"""

#example 5 - breakpoint
"""
import random
heads= 0

for i in range(1,1001):
    if random.randint(0,1) == 1:
        heads+=1
    if i == 500:
        print('Halfway done')

print('Heads came up '+ str(heads) + 'times.')
"""

"""
spam =15

for i in range(20):
    spam-=1
    assert spam<15, 'The spam value is less than 10'
"""

import random

guess =''
