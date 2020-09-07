# Write your code here :-)

import time

char = '*'
condition1 = True
condition2 = True
i=0

while True:
    while condition1:
        print(' '*i,char*8)
        i+=1
        time.sleep(0.1)

        if i == 5:
            condition1 = False
    else:
        i-=1
        print(' '*i,char*8)
        time.sleep(0.1)

        if i == 0:
            condition1=True

"""
import time
indent = 0
indentIncreasing  = True

while True:
    print(' '*indent,end='')
    print('*******')
    time.sleep(0.1)

    if indentIncreasing:
        indent+=1
        if indent ==10:
            indentIncreasing = False
    else:
        indent-=1
        if indent == 0:
            indentIncreasing = True
"""








