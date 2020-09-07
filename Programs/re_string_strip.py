# Write your code here :-)
#!python
#re_string_strip.py  - custom function to strip the given characters from a string

"""
1. check if the function has two arguments; first- String , second - character
2. if secong argument is null
    check if the string has any empty spaces
        strip the empty spaces
3. if secong argument is not null
    remove the argument value from the string
"""

import re

def string_strip(name,char):

    if char !='':
        replace_char = re.compile(char)
        print(replace_char.sub('',name))
    elif re.findall('\s',name)!=[]:
        print(re.compile(r'^\s').sub('',name))
    else:
        print('I am in')



string_strip('     Srinu Balireddy  ','')


ltrim=re.compile(r'^\s*')
rtrim=re.compile(r'\s+$')
search = ltrim.findall('   Srinu Balireddy')
print(search)
search = rtrim.findall(' Srinu  ')
print(search)

sub = ltrim.sub('','    Srinu Balireddy     ')
print(sub)
sub = rtrim.sub('','Srinu Balireddy     ')
print(sub)

