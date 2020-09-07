# Write your code here :-)
import sys
board = {'key1':'_block1','key2':'|','key3':'_block2','key4':'|','key5':'_block3',
         'key6':'_block4','key7':'|','key8':'_block5','key9':'|','key10':'_block6',
         'key11':'_block7','key12':'|','key13':'_block8','key14':'|','key15':'_block9'}
player=''
key=''
boardkey=''
event = True

#pprint.pprint(board[1])
def griddisplay():
    for i in range(1,16):
        print(board['key'+str(i)],end='')
        if i ==5:
            print(sep='')
        elif i==10:
            print(sep='')
    print(sep='')

griddisplay()

def keyupd(key):
    if key == 1:
        boardkey='key1'
        return boardkey
    if key == 2:
        boardkey='key3'
        return boardkey
    elif key == 3:
        boardkey='key5'
        return boardkey
    elif key == 4:
        boardkey='key6'
        return boardkey
    elif key == 5:
        boardkey='key8'
        return boardkey
    elif key == 6:
        boardkey='key10'
        return boardkey
    elif key == 7:
        boardkey='key11'
        return boardkey
    elif key == 8:
        boardkey='key13'
        return boardkey
    elif key == 9:
        boardkey='key15'
        return boardkey

def gridupd(boardkey,player):
    board[boardkey]='   '+player+'   '
    print(sep='')
    griddisplay()




for i in range(1,10):
    if event:
        print(sep='')
        x=i%2
        if x == 1:
            print('Player1')
        else:
            print('Player2')
        key= int(input('Select the block to present your input:'))
        player = input('select your input-  \'O\' or \'X\':')
        boardkey=keyupd(key)
        gridupd(boardkey,player)

        def won():
            if x==1:
                print('Game over ! Player1 Won!!')
                event=False
            else:
                print('Game over ! Player2 Won!!')
                event=False

        if i >=3:
            if board['key1'] == board['key3'] and board['key3'] == board['key5']:
                won()
            elif board['key6'] == board['key8'] and board['key8'] == board['key10']:
                won()
            elif board['key11'] == board['key13'] and board['key13'] == board['key15']:
                won()
            elif board['key1'] == board['key8'] and board['key8'] == board['key15']:
                won()
            elif board['key3'] == board['key8'] and board['key8'] == board['key13']:
                won()
            elif board['key5'] == board['key10'] and board['key10'] == board['key15']:
                won()
            elif board['key5'] == board['key8'] and board['key8'] == board['key11']:
                won()
            elif board['key1'] == board['key6'] and board['key6'] == board['key11']:
                won()


'''
def player2(key):
    print('Player2!')
    key= int(input('Select the Key to present your input:'))
    player = input('select your input-\'O\' or \'X\':')
    board['key'+str(key)]=player
    griddisplay()
'''


#gridupd(boardkey)
