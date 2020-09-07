# Write your code here :-)
from pathlib import Path
myfiles = ['account.txt','details.csv','invite.docx']
for filename in myfiles:
    print(Path(r'c:\users\srinu',filename))

import os
p = Path(r'C:\Users\srinu\Desktop\Python')
#os.makedirs('C:/Users/srinu/Desktop/Python/9readingwritingfiles/new')

print(os.listdir(Path.cwd()))
#print(Path.home())
print(os.path.getsize(r'C:\Users\srinu\Desktop\Python\9readingwritingfiles\practice.py'))
print(os.listdir(r'C:\Users\srinu\Desktop\Python'))

totalsize =[]
for filename in os.listdir(r'C:\Users\srinu\Desktop\Python'):
    totalsize.append(os.path.getsize(Path(r'C:\Users\srinu\Desktop\Python',filename)))

print(totalsize)
print(len(totalsize))


p = Path(r'C:\Users\srinu\Desktop\Python')
print(p.glob('*'))
print(list(p.glob('New Text Document?.txt')))


##########################3

import pprint
cats =[ {'name':'abc','desc':'chubby'},{'name':'bcd','desc':'doll'}]
print(pprint.pformat(cats))
fileobj = open('mycats.py','w')
fileobj.write('cats ='+ pprint.pformat(cats)+'\n')
fileobj.close()

import mycats

print(mycats.cats)
print(mycats.cats[0]['name'])

cats =[ {'name':'abc','desc':'chubby'},{'name':'bcd','desc':'doll'}]
print(pprint.pformat(cats))
a=pprint.pprint(cats)
b=pprint.pformat(cats)
print(a,b ,sep='-')



"""
p = Path(r'C:\Users\srinu\Desktop\Python\9readingwritingfiles\practice.py')
print(p)
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

a = r'C:\Users\srinu\Desktop\Python\9readingwritingfiles\practice.py'
k = os.path.split(a)
print(k)
print(k[0])
print(k[1].split('.'))
print(a.split(os.sep))

"""




