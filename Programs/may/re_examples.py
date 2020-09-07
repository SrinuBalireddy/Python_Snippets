# Write your code here :-)
import re

"""
mo = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
res = mo.search('My num is 123-456-7890')
print('Phone num found: '+ res.group())
print('Phone num found: '+ res.group(0))
print('Phone num found: '+ res.group(1))
print('Phone num found: '+ res.group(2))
print('Phone num found: '+ res.group(3))
print(res.groups())
"""
"""
mo = re.compile(r'Batman|Robin king')
res = mo.search('Batman king and avd')
print(res.group())
res1 = mo.search('Robin king and avd')
print(res1.group())

mo1 = re.compile(r'Bat(man|women|robin)*')
res2 = mo1.search('Batrobinrobin')
print(res2.group())
res3 = mo1.search('Batwomenwomenwomenwomen')
print(res3.group())



mo = re.compile(r'^\d\w+$')
res= mo.search('123asfsf8900')
print(res.group())


mo = re.compile(r'(.at){1,35}')
res= mo.findall('jat$5783938mat3!>@!#$%^&*kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
#print(res)


mo = re.compile('<.*>?')
res = mo.findall('<serve the man> dinner>')
print(res)
res1 = mo.findall('hey!<serve the man> dinner, here')
print(res1)


mo = re.compile(r'Agent \w+')
res = mo.sub('Cencored', 'Agent Alice is undercover for Agent bob')
print(res)

mo1 = re.compile(r'Agent (\w)\w*')
res1 = mo1.sub(r'\1****','Agent Alice is undercover for Agent bob')
print(res1)

"""

phone = re.compile(r'''(
                       (\d{3}|\(\d{3}\))?                        #area code
                       (\s|-|\.)?                               #seperator
                       \d{3}                                    #first 3 digits
                       (\s|-|\.)                                #seperator
                       \d{4}                                    #last 4 digits
                       (\s*(ext|x|ext.)\s*\d{2,5})?             #extension
                    )''',re.VERBOSE)

res = phone.search('(123) 456 7890 ext.   1234')
print(res.groups())

ssn = re.compile(r'\d{12}(\d{4})')
ssnres = ssn.sub(r'************\1','1234567891234567')
#ssnres = ssn.search('1234567891234567')
print(ssnres
)

#mo = re.compile(r',\d{3}+')
mo = re.compile(r'^\d{1,3}(,\d{3})*$')
res = mo.search('2,789')
#print(res.group())

mo = re.compile(r'^[A-Z]+\w+\s+Wantanabe$')
res = mo.search('aruto Wantanabe')
res = mo.search('Alice wantanabe')
#print(res.group())

mo = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$',re.I)
res = mo.search('Alice pets CATS.')
print(res.group())
