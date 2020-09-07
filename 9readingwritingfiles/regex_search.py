# Write your code here :-)
#! python3
# regex_search.py - opens .txt files in a folder,searches and displays text that matches the
#                   user supplied reg expression.

import re
from pathlib  import Path

path = Path.cwd()
Filepath = path / 'new'
print(Filepath)

textfiles = list(Filepath.glob('*.txt'))
print(textfiles)

for files in textfiles:
    text = files.open()
    fileddata = text.read()
    print('-----------------------------')
    ph_expr = re.compile(r'\d{10}')
    ph_search  = ph_expr.findall(fileddata)
    #print(ph_search)
    print('filename: '+str(files.name))
    print('No. of phone numbers found: '+str(len(ph_search)))

    for i in range(len(ph_search)):
        print(str(i+1)+'. '+ph_search[i])















