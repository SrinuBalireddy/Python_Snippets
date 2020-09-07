# Write your code here :-)
#! python 3
# renamefiles.py  - rename dates with american dates format MM-DD-YYYY date format to
#                   europena DD-MM-YYYY

"""
1. find all the text files in the folder
2. create a regex to find the data match and replace them with the req data format

"""

import os,re,shutil
from pathlib import Path

p=Path.cwd()/'renamefiles'
print(p)

for filename in p.glob('*.txt'):
    print(filename.name)

    #todo - create regex to find the date in the file name

    date_expr = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    date_search= date_expr.search(filename.name)
    #date_search = date_expr.findall(filename.name)
    #print(date_search.group())
    #print(date_search)
    #print(date_search.group(1))

    #todo - create regex to replace the date with req format

    dest=f"{Path.cwd()}\\file{date_search.group(2)}-{date_search.group(1)}-{date_search.group(3)}.txt"


    shutil.move(filename,dest)





