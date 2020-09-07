# Write your code here :-)
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
except KeyboardInterrupt:
    sys.exit()
