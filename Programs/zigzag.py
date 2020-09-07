# Write your code here :-)
"""
        *******
       *******
      *******
     *******
    *******
     *******
      *******
       *******
        *******
"""
"""
---------------------------------------------------------
import time,sys
indent=20

def indentzero():
    while True:
        global indent
        print(' '*indent,end='')
        print('*********')
        time.sleep(0.1)
        indent=indent+1
        if indent == 20:
            indentfive()

def indentfive():
    while True:
        global indent
        print(' '*indent,end='')
        print('*********')
        time.sleep(0.1)
        indent=indent-1
        while indent == 0:
            indentzero()
try:
    indentfive()
Except KeyboardInterrupt:
    sys.exit()

----------------------------------------
"""
#book solution

import time,sys
indent = 20
indentIncreasing = True

try:
    while True:
        print(' '*indent,end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent -1
            if indent == 0:
                indentIncreasing=False
        else:
            indent = indent +1
            if indent == 20:
                indentIncreasing=True

except KeyboardInterrupt:
    sys.exit()








