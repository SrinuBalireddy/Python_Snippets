# Write your code here :-)
"""

user =take input from user r , p ,s ,q
pc = random

compare and increment win loss tie values

"""

import random,sys

print('Let\'s play rock paper scissors !')

win = 0
loss = 0
tie = 0
print('win: '+ str(win) +', loss: '+ str(loss) +', tie: '+str(tie))
print('%s wins, %s loss, %s tie' %(win,loss,tie))


user =''

while True:
    print('Select one - (r)rock (p)paper (s) scissors (q) quit: ')
    user = input()
    if user == 'p':
        print('Paper versus..')
    elif user == 'r':
        print('Rock versus..')
    elif user =='s':
        print('Scissors versus..')
    elif user =='q':
        sys.exit()

    pc_num= random.randint(1,3)
    if pc_num==1:
        pc = 'r'
        print('Rock')
    elif pc_num==2:
        pc = 'p'
        print('Paper')
    else:
        pc = 's'
        print('Scissors')

    if user == pc:
        print('It\'s a tie')
        tie = tie+1
    elif user == 'r' and pc == 's':
        print('you win')
        win = win+1
    elif user == 's' and pc == 'p':
        print('you win')
        win=win+1
    elif user == 'p' and pc == 'r':
        print('you win')
        win=win+1
    elif user == 's' and pc == 'r':
        print('you lost')
        loss = loss+1
    elif user == 'p' and pc == 's':
        print('you lost')
        loss=loss+1
    elif user == 'r' and pc == 'p':
        print('you lost')
        loss=loss+1


    print('win: '+ str(win) +', loss: '+ str(loss) +', tie: '+str(tie))





