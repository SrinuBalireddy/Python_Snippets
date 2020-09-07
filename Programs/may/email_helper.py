# Write your code here :-)


import sys, pyperclip

my_dict = {
           'good': 'I appreciate all the good work you are doing. Keep it up',
           'bad' : "I hope you don't repeat this mistake again",
           'ok'  : 'keep doing the good work'
          }

if len(sys.argv) < 2:
    print('Keyword has not been provided')
    sys.exit()

keyword = sys.argv[1]

if keyword in my_dict:
    pyperclip.copy(my_dict[keyword])
    print('keyword description has been copied to clipboard')

else:
    print('keyword is not available in the dictionary')



