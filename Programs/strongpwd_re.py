# Write your code here :-)
#!python 3.8
#strongpwd_re.py - Validating the password strength

import re
passstrong=False

def pwdstrength():

    password = input('Enter the password: ')

    char_expr  = re.compile(r'\w{8,}')  #To check the password length
    upper_expr = re.compile(r'[A-Z]')   #To check the uppercase letter
    lower_expr = re.compile(r'[a-z]')   #To check the lowercase letter
    digit_expr = re.compile(r'[0-9]')   #To check the digits

    if char_expr.findall(password)==[]:
        print('Password should have atleast 8 characters')
    elif upper_expr.findall(password)==[]:
        print('Password should have atleast one uppercase letter')
    elif lower_expr.findall(password)==[]:
        print('Password should have atleast one lowercase letter')
    elif digit_expr.findall(password)==[]:
        print('Password should have atleast one digit')
    else:
        print('Your password is strong. Good Job!')
        global passstrong
        passstrong=True
        return

while not passstrong:
    pwdstrength()



