# Write your code here :-)
"""
bday = {'Srinu':'Nov24','Sow':'Oct16'}

for k in bday.items():
    print(list(k))

name = input('Enter the name:')
if name in bday:
    print(name+'\'s Birthday is on '+bday[name])
else:
    askbday = input('When is '+ name +'\'s bday?:')
    bday[name]=askbday
    print('Birthday db has been updated')

print(bday)

for k in bday.item():
   print(k)
-----------------------------------

picnic={'cakes':2,'cream':4}
print(picnic.get('cakes',0))

picnic.setdefault('eggs',4)
print(picnic)

picnic.setdefault('eggs',5)
print(picnic)
"""

import pprint
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count={}

for char in message:
    count.setdefault(char,0)
    count[char]=count[char]+1

#print(count)
pprint.pprint(count)
#print(pprint.pformat(count))
