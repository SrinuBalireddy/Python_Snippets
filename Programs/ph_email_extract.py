# Write your code here :-)
#! python 3.8
# ph_email_extract.py  -Finds all the email and phone in a textinput

#use pyperclip to get the data into a variable from clipboard
#write phone number reg expression
#write email reg expression
#copy the data to clipboard

import re,pyperclip

text= pyperclip.paste()
#print(text)
matches=[]

ph_expr = re.compile(r'''(
          (\d{3}|\(\d{3}\))?    #code
          (\s|-|\.)?            #seperator
          (\d{3})                 #digits
          (\s|-|\.)             #seperator
          (\d{4})                 #digits
          )''',re.VERBOSE)

email_expr = re.compile(r'''(
             ([a-zA-Z])+     #starts with alphabet
             ([a-zA-Z0-9.-_])      #combination of digits and letters
             @
             ([a-zA-Z0-9.-])+
             (\.[a-zA-Z]{2,4})
             )''',re.VERBOSE)

ph_search = ph_expr.findall(text)
print(ph_search)
for i in range(len(ph_search)):
    #print(ph_search[i][0], sep='')
    matches.append(ph_search[i][0])


email_search = email_expr.findall(text)
#print(email_search)
for k in range(len(email_search)):
    #print(email_search[k][0], sep='')
    matches.append(email_search[k][0])

print(matches)
final_res= '\n'.join(matches)
print(final_res)
pyperclip.copy(final_res)
