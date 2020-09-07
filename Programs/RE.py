# Write your code here :-)
"""
num= '222-333-4444'
#print(len(num))
print(num.partition('-'))
print(num[3])


def isphone(num):
    if len(num)>=12 and num[3]=='-' and num[7]=='-' :
        return True
    else:
        return False

print(isphone(num))

---------------------------------------------------

import re

reg= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
numsearch = reg.search('my num is 222-333-4444')
print('Ph num found-'+str(numsearch))
print('Ph num found :'+numsearch.group())

"""

"""
import re

reg= re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
numsearch = reg.search('my num is 222-333-4444')
print('Ph num found :'+numsearch.group())
print(numsearch.group(1))
print(numsearch.group(2))
print(numsearch.groups())
a,b,c = numsearch.groups()
print(a,b,c,sep='   ')

----------------------------------
import re
reg = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
numsearch = reg.search('my num is 222-333-4444 and (333)-444-5555')
print('Ph num found :'+numsearch.group())


#pipe

import re
reg = re.compile(r'Top|Hanks')
mo = reg.search('Top and Hanks')
print(mo.group())
mo = reg.search('Hanks and Top')
print(mo.group())
mo = reg.findall('Hanks and Top')
print(mo)

reg1 = re.compile(r'Bat(man|Honey|women)')
mo = reg1.search('BatHoney')
print(mo.group())
print(mo.group(1))

reg1 = re.compile(r'Bat(man|Honey|women)?')
mo = reg1.search('Bat')
print(mo.group())
print(mo.group(1))
mo = reg1.search('Batwomen')
print(mo.group())
print(mo.group(1))
"""
"""
import re
reg1 = re.compile(r'Bat(man|Honey|women)?Hero')
mo = reg1.search('BatHero')
print(mo.group())
mo = reg1.search('BatwomenHero')
print(mo.group())
mo = reg1.search('Bat')
mo = reg1.search('BatwomenwomenHero')
print(mo)

print('===========================')

import re
reg1 = re.compile(r'Bat(man|Honey|women)*Hero')
mo = reg1.search('BatwomenHero')
print(mo.group())
mo = reg1.search('BatwomenwomenHero')
print(mo.group())

print('===========================')

import re
reg1 = re.compile(r'Bat(man|Honey|women)+Hero')
mo = reg1.search('BatwomenHero')
print(mo.group())
mo = reg1.search('BatwomenwomenHero')
print(mo.group())
mo = reg1.search('Bat')
print(mo)

"""
"""
#Braces

import re
print(sep=' ')
reg = re.compile(r'(Ha){3,5}')
mo= reg.search('HaHaHaHaHa')
print(mo.group())

print(sep=' ')
reg = re.compile(r'(Ha){3,5}?')
mo= reg.search('HaHaHaHaHa')
print(mo.group())
"""
"""
#Find all
import re

print(sep=' ')
reg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = reg.findall('My num is 222-333-4444 and 333-444-5555')
print(mo)

print(sep=' ')
reg = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = reg.findall('My num is 222-333-4444 and 333-444-5555')
print(mo)
"""
"""
#carrot and dollars

import re
print(sep=' ')
reg = re.compile(r'^Hello')
mo = reg.findall('Hello World')
print(mo)
mo = reg.findall('hello World')
print(mo)

reg = re.compile(r'World$')
mo = reg.findall('Hello World')
print(mo)
mo = reg.findall('hello world')
print(mo)

"""
"""
import re
print(sep=' ')
reg = re.compile(r'.*at')
mo= reg.findall('the cat in the hat sat on the flat mat')
#print(mo)

reg = re.compile(r'First Name: (.*) Last Name: (.*)')
mo= reg.findall('First Name: Srinu Last Name: B')
print(mo)
mo= reg.search('First Name: Srinu Last Name: B')
print(mo.group())
print(mo.group(1))
"""
"""
#sub
import re
reg = re.compile(r'Agent \w+')
mo=reg.sub('Censored','Agent Harry gave the secret documents to Agent Bob')
print(mo)

reg = re.compile(r'Agent (\w)+')
mo=reg.sub('Censored','Agent Harry gave the secret documents to Agent Bob')
print(mo)

reg = re.compile(r'Agent (\w)\w*')
mo=reg.sub(r'\1****','Agent Harry gave the secret documents to Agent Bobr')
print(mo)
"""

#verbose
"""
222-333-4444

import re
reg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (-|\s|\.)
    \d{3}
    (-|\s|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*d{2,5})?
    )''',re.VERBOSE)
mo = reg.findall('my ph num is 222-444-5555 and (222).333-5678')
print(mo)

"""
#Exercise
import re
"""
Q.20
#reg= re.compile(r'(\d\d)?(\d\d\d,)+')
reg= re.compile(r'^\d{1,3}(,\d{3})*$')
res= reg.search('6,789')
print(res.group())

"""
"""
#Q21
#book sol
reg = re.compile(r'^[A-Z][a-z]*\sWatanabe')
res = reg.findall('Alic. Watanabe1')
print(res)

#my sol
reg = re.compile(r'^[A-Z][a-z]*\sWatanabe$')
res = reg.findall('Alic. Watanabe1')
print(res)

"""
#Q22

import re
reg = re.compile(r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.I)
res = reg.findall('Apple')
print(res)
res = reg.findall('Cat')
print(res)
res = reg.findall('Alice eats apples.')
print(res)
res = reg.findall('Bob')
print(res)
res = reg.findall('Carol throws baseballs.')
print(res)
