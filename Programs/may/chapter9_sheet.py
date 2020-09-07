# Write your code here :-)
import sys, os
from pathlib import Path
#print(sys.platform)

Path('eggs','spam')

#print(os.getcwd())
#print(Path.cwd())

p = Path.cwd()

#p = r'C:\Users\srinu\Desktop\Python\Programs\may'

#print(os.path.getsize(p))

#print(os.listdir(p))

#print(p/os.listdir(p)[0])

#print(os.path.getsize(p/os.listdir(p)[0]))

for filename in os.listdir(p):
    path = p/filename
    #print(f'{filename} size: {os.path.getsize(path)}')


k = r'C:\Users\srinu\Desktop\Python\Programs\may'

hellofile = open(r'C:\Users\srinu\Desktop\Python\Programs\may\comma_code.py')
#print(hellofile.read())

#hellofile.seek(0)
#print(hellofile.readlines())


##################
"""
import shelve

shelfFile = shelve.open('mydata')
cats = ['a','b','c']
shelfFile['cats'] = cats
shelfFile.close()
"""
import pprint

str = 'The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit'
count = {}

for i in str:
    count.setdefault(i,0)
    count[i] = count[i]+1

#pprint.pprint(count)
pstr = pprint.pformat(count)
#print(pstr)

##########################

"""
def menudisplay(menu, lw, rw):

    print('Sandwich Station'.center(lw+rw,'*'))
    print('')
    for k,v in menu.items():
        print(k.ljust(lw,'.'),v.rjust(rw))

menu = {'Sandwich':'30rs', 'Dosa': '35rs', 'Milkshake': '25rp', 'Idly': '20rs'}
menudisplay(menu, 15, 15)
"""


import requests

res = requests.get('http://127.0.0.1:8000/postsapi/')
"""
print(res.text)
print(res.status_code)
print(requests.codes.ok)

print(dir(res))
"""

from pygments.lexers import get_all_lexers


lexers = [ item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
print(LANGUAGE_CHOICES)
