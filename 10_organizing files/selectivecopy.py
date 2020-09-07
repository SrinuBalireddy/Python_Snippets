# Write your code here :-)
#! python3
# selectivecopy.py - copy selective files in a directory tree

import os ,shutil
from pathlib import Path

#count=0
"""
for foldername,subfolders, filenames in os.walk(Path.cwd()):
    count=0

    print('I am in '+ foldername)
    for subfolder in subfolders:

        print('subfolder name '+subfolder)

    for filename in filenames:
        path = Path(foldername+'\\'+filename)
        if path.suffix == '.txt' or path.suffix=='.pdf':
            count +=1
            shutil.copy(filename,'C:\\Users\\srinu\\Desktop\\Python\\new')
            print(f' {filename} copied')
    print(f'count of .txt and .pdf files in  {foldername} -{str(count)}')
"""

def selectivecopy(folder):
    folder = os.path.abspath(folder)

    for foldername,subfolder,filenames in os.walk(folder):

        for filename in filenames:
            if  filename.endswith('.txt') or filename.endswith('.pdf'):
                filename=os.path.join(foldername,filename)
                shutil.copy(filename,'C:\\Users\\srinu\\Desktop\\Python\\new')
                print('Copying '+ filename+ '...')




selectivecopy(Path.cwd())
print('Done')



