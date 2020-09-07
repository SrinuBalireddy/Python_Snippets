# Write your code here :-)
#! python3
# fillinggaps.py - rename the files with sequential numbers

"""

"""

from pathlib import Path
import shutil

def fileno(filename):
    fileno = []

    for i in filename:
        fileno.append(i)

    fileno= fileno[4]+fileno[5]+fileno[6]
    return int(fileno)

def gaps(folder):
    filenum=[]
    files= []

    for filename in folder.glob('*.txt'):
        filename = filename.stem
        files.append(filename)
        filenum.append(fileno(filename))
        #print(filename)
    print(filenum)
    print(files)

    for i in range(len(filenum)):
        print(i)
        num = int(filenum[i])+1
        print(num)
        if num < max(filenum):
            if num not in filenum:
                filenum.append(num)
                print('00'+str(num)+'is not available')
                shutil.copy(folder/('spam00'+str(i+1)+'.txt'),r'C:\Users\srinu\Desktop\Python\10_organizing files\gaps\spam00'+str(num)+'.txt')





gaps(Path(r'C:\Users\srinu\Desktop\Python\10_organizing files\gaps'))


