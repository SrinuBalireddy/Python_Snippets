# Write your code here :-)
#! python3
#mclip.py - A multi clipboard program

Text = {'agree':'Yes,I Agree. That sounds fine to me',
        'busy': 'Sorry, can we do th is later',
        'upsell': 'would u consider making this montly donation'}

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase=sys.argv[1] #first command line arg is the keyphrase

if keyphrase in Text:
    pyperclip.copy(Text[keyphrase])
    print('Text for '+keyphrase +' is copied to clipboard')
else:
    print('There is no text for '+ keyphrase)
