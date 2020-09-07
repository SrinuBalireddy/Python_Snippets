# Write your code here :-)
#! python3
# deletefiles.py - deletes files with size >100MB

import os, send2trash
from pathlib import Path


def deletefile(folder):
    count=0

    #folder= os.path.abspath(folder)

    for foldername,subfolders, filenames in os.walk(folder):
        #print('Main folder -'+foldername)
        #for subfolder in subfolders:
            #print('subfolder -'+subfolder)
        for filename in filenames:
            #print(os.path.getsize(filename))
            #print('filename -'+filename)
            filename=os.path.join(foldername,filename)
            #print(filename)
            #print(os.path.getsize(filename))
            if os.path.getsize(filename)>250000:
                #count+=1
                #print(str(count))
                print(filename)
                send2trash.send2trash(filename)

deletefile(Path.cwd())
