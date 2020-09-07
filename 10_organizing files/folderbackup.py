# Write your code here :-)
#! python3
# folderbackup.py - create a zipfile of a folder and create versions during the next run.

"""
1. identify any existing zip files with the required folder name in the cwd
2. if not exists -
    select the folder to be zipped and create a backup with _1 version
   if exists-
    retrieve the existing zip file name and append subsequent version numbers

"""

import zipfile,os
from pathlib import Path


foldername ='delicious'

#print(Path.cwd())

for filename in Path.cwd().glob('*'):
    #print(filename)
    if os.path.basename(filename) == foldername:
        if os.path.exists(foldername+'_1.zip'):
            version =int(filename.stem.split('_')[1])+1
            newzip = zipfile.ZipFile(foldername+'_'+str(version)+'.zip','w')
        else:
            newzip = zipfile.ZipFile(foldername+'_1.zip','w')
            break




"""
for filename in Path.cwd().glob('*.zip'):
    version =int(filename.stem.split('_')[1])
    print(os.path.basename(filename))
    if os.path.basename(filename) != foldername+'_'+str(version)+'.zip':
        newzip = zipfile.ZipFile(foldername+'_1.zip','w')
        break
        #newzip.write(foldername,compress_type=zipfile.ZIP_DEFLATED)
    #if os.path.basename(filename) == foldername+'_'+str(version)+'.zip':
     #   continue
    else:
        print(filename.stem)
        #version =int(filename.stem.split('_')[1])
        newversion = version+1
        #print(newversion)
        print(foldername+'_'+str(newversion)+'.zip')
        newzip = zipfile.ZipFile(foldername+'_'+str(newversion)+'.zip','w')

"""








