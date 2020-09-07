# Write your code here :-)
#First program
"""
items=[['ahk','bwods','caaf','drhr'],
       ['elll','fd','gdrsg','hferf'],
       ['ikokok','jjjsss','kw','lwww'],
       ['mertyuii','nk','ooooo','pllklp'],
       ['mertyuii','nk','ooooo','pllklp']]
rows=0
col=0
for i in items:
    rows=len(i)
    col=col+1


print(rows,col)


##################

import re
pattern= r'bat(women|men|girl)?ok'
string1 = 'batmen, bat, batgirl,batwomen,batok'
print(re.findall(pattern,string1))
print(re.search(pattern,string1).group())


###########3

import re

num = int(input())

for i in range(num):
    ph_num = '8745A69852'
    num_expr= re.compile(r'^(7|8|9)(\d){9}$')
    num_search = num_expr.search(ph_num)
    if num_search != None:
        print('YES')
    else:
        print('NO')
"""

##########
"""
def eggs(some):
    some.append('Hello')
    print(id(some))

spam=[1,2,3]
print(id(spam))
eggs(spam)
print(spam)
print(id(spam))
"""

##############
"""
import pprint
allguests = {'Alice':{'Apple':5,'eggs':2},
             'Bob':{'Apple':2,'eggs':3},
             'Nick':{'Apple':7,'milk':2}}

pprint.pprint(allguests)

def total(guests,item):
    total=0
    for k,v in guests.items():
        total =total+v.get(item,0)
    return total

print('Apples :'+str(total(allguests,'Apple')))


#################
lst=[]

def int(n):
    for i in range(1,n+1):
        lst.append(n)
    return tuple(lst)


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, n)
    print(integer_list)
"""

#############
"""
lst = [1,2,3]
newlst=[]
num =3

for i in range(0,lst[0]+1):
    for j in range(0,lst[1]+1):
        for k in range(0,lst[2]+1):
            if k+j+i != num :
                newlst.append([i,j,k])

print(newlst)
print(len(newlst))
"""

###############3
"""
import random

lst=[]
num= int(input())
diff=[]

for i in range(num):
    lst.append(random.randint(1,100))

print(lst)
print(max(lst))

maxnum= max(lst)
lst.remove(maxnum)

print(lst)
maxnum= max(lst)
print(maxnum)



for i in range(len(lst)):
    diff.append(maxnum-lst[i])
    print(diff)

maxnum_new= min(diff)
print(maxnum_new)
"""
"""
----------------------------------------

if __name__ == '__main__':
    import random
    n = int(input())
    arr = [57,57,-57,57]
    #lst=[]
    var = True

    #for i in range(n):
     #   lst.append(random.randint(1,100))

    maxnum=max(arr)
    while var:
        if maxnum in arr:
            arr.remove(maxnum)
        else:
            var=False
    print(max(arr))
"""

"""
------------------------------------------
#lst=[['srinu', 50.0], ['sow', 60.0]]
#score=[]
"""
"""
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name,score])
"""
"""
names =['Srinu','Sow','abc','kab']
score =[50.0,50.0,70.0,50.0]

maxnum= max(score)
while True:
    if maxnum in score:
        i=score.index(maxnum)
        score.remove(maxnum)
        del names[i]
    else:
        break

maxnum= max(score)
for i in range(len(score)):
    if maxnum == score[i]:
        print(names[i])
        #print(maxnum)

"""

"""
while True:
    age= input('Enter your age: ')
    try:
        age=int(age)
    except:
        print('please use numeric digits')
        continue
    if age<1:
        print('Please enter a positive number')
        continue
    break

print(f' Your age is {age}'

"""

from pathlib import Path
import os

print(Path.cwd())

print(os.listdir(Path.cwd()))



