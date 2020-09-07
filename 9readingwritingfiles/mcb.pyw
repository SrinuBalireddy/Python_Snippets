# Write your code here :-)
#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all the keywords to clipboard

import shelve,sys,pyperclip

mcbshelf = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() =='delete':
    del mcbshelf[sys.argv[2]]
elif len(sys.argv)==2:
    #List keyword and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for i in mcbshelf.keys():
            del mcbshelf[i]

mcbshelf.close()
