# Write your code here :-)
#! python
# bulletpointadder.py #Adds buller points to the start of each line of the text on the clipboard

import pyperclip
text = pyperclip.paste()

newlist = text.split('\n')
print(newlist)

for i in range(len(newlist)):
    newlist[i]= '* '+newlist[i]

newstr = ''.join(newlist)
print(newstr)
pyperclip.copy(newstr)

