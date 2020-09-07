# Write your code here :-)
"""
import shutil
from pathlib import Path

p = Path.home()
#print(shutil.copy(p/'spam.txt',Path.cwd()))
print(shutil.move(Path.cwd()/'spam_new.txt',Path.cwd()/'new'))
"""

"""
import os
from pathlib import Path

for foldername,subfolders,filenames in os.walk(Path.cwd()/'Delicious'):


    for subfolder in subfolders:
        print('Subfolder of '+ foldername+': '+subfolder)

    for filename in filenames:
        print('File Inside '+ foldername+ ': '+ filename)

    print('')
"""
"""
import zipfile ,os
from pathlib import Path

p= Path.cwd()
exampleZip = zipfile.ZipFile(p/'delicious.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('delicious/spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print(f'compressed file is {round(spamInfo.file_size/spamInfo.compress_size,2)}x smaller!')
#exampleZip.extract('delicious/spam.txt')
try:
    #exampleZip.extractall()
    print(exampleZip.extract('delicious/spam.txt'))
except:
    print('in catch block')

exampleZip.close()

"""
"""
import zipfile

newzip = zipfile.ZipFile('new.zip','w')
print(newzip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED))

print(newzip.namelist())
Zipinfo = newzip.getinfo('spam.txt')
print(Zipinfo)
print(Zipinfo.file_size)
print(Zipinfo.compress_size)

print(f'the compressed file is {round(Zipinfo.file_size/Zipinfo.compress_size,2)}x smaller!')
newzip.close()
"""
import zipfile ,os
from pathlib import Path
print(list(os.walk(Path.cwd())))
