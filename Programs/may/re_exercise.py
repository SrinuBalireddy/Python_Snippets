# Write your code here :-)
import re

phex = re.compile(r'''(
                      (\d{3}|\(\d{3}\))?
                      (-|\.)?
                      \d{3}
                      (-|\.)
                      \d{4}
                      )''',re.VERBOSE)

emailex = re.compile(r'''(
                         ([a-zA-Z0-9])+
                         @
                         ([a-zA-Z0-9])+
                         (\.[a-zA-Z0-9]{2,4})
                         )''', re.VERBOSE)

with open('userdata.txt') as f:
    data = f.read()
    phres = phex.findall(data)
    print('Phone numbers list: \n')
    for i in range(len(phres)):
        print(phres[i][0])

    emailres = emailex.findall(data)
    print('Email list: \n')
    for i in range(len(emailres)):
        print(emailres[i][0])
