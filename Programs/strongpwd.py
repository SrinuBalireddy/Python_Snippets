# Write your code here :-)
#!python 3.8
#strongpwd.py - validate the password strength

"""
steps-
1. Take input from the user
2. Check the no. of characters in the string(should be >=8)
3. should contain both upper and lower case
4. Atleast one digit
"""

pwd='abcsdkliK7'
uppercount=0
lowercount=0
decimal=0


if len(pwd)>=8:
    for i in pwd:
        if i.isupper():
            uppercount+=1
        else:
            lowercount+=1
    for i in pwd:
        if i.isdecimal():
            decimal+=1
    if uppercount==0:
        print('Password should have atleast one uppercase letter')
    elif lowercount==0:
        print('Password should have atleast one lowercase letter')
    elif decimal==0:
        print('Password should have atleast one digit')
else:
    print('Password should have atleast 8 characters')


if len(pwd)>=8 and uppercount!=0 and lowercount!=0 and decimal!=0:
    print('Password is accepted')

print(uppercount ,lowercount,decimal, sep=' ')




