# Write your code here :-)
import os,time
from pathlib import Path

p = Path.cwd()
filenoList = []
missingnoList = []

for file in p.glob('*txt'):
    filenoList.append(int((file.stem).strip('spam')))

print(filenoList)
maxno = max(filenoList)

for no in range(1,maxno):
    if no not in filenoList:
        missingnoList.append(no)

print(missingnoList)

for newfileno in missingnoList:

    if newfileno < 9:
        filename = 'spam00'+str(newfileno)

    elif newfileno>9 and newfileno<100:
        filename = 'spam0'+str(newfileno)

    else:
        filename = 'spam'+str(newfileno)

    f = open(filename+'.txt', 'a')
    f.write(filename)
    f.close()
    print(f'Created the missing file {filename}')
    time.sleep(0.1)
