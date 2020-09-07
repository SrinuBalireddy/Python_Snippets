# Write your code here :-)


board1 = {'topL': 'a ', 'topM': ' ', 'topR': ' ',
         'midL': ' b', 'midM': ' ', 'midR': ' ',
         'lowL': ' c', 'lowM': ' ', 'lowR': ' ',
        }

board = {'topL': 'topL', 'topM': 'topM', 'topR': 'topR',
         'midL': 'midL', 'midM': 'midM', 'midR': 'midR',
         'lowL': 'lowL', 'lowM': 'lowM', 'lowR': 'lowR',
        }
def boardplan(board):

    print(f" {board['topL']}| {board['topM']} | {board['topR']} ")
    print('-------------------')
    print(f" {board['midL']}| {board['midM']} | {board['midR']} ")
    print('-------------------')
    print(f" {board['lowL']}| {board['lowM']} | {board['lowR']} ")
    print('')

print("Let's play Tic-Tac-Toe !")

boardplan(board)

print("Let's get started !")

while True:
    for i in range(1,3):
        print(f'Player{i} Turn !')
        selection = input('select the position and pick a letter( O or X) (ex- lowL X):').split(' ')
        print(selection)

        board[selection[0]] = ' '+selection[1]+'  '
        boardplan(board)

        if ((board['topL'] == board['topM'] == board['topR']) or
            (board['midL'] == board['midM'] == board['midR']) or
            (board['lowL'] == board['lowM'] == board['lowR']) or
            (board['topL'] == board['midL'] == board['lowL']) or
            (board['topM'] == board['midM'] == board['lowM']) or
            (board['topR'] == board['midR'] == board['lowR']) or
            (board['topL'] == board['midM'] == board['lowR']) or
            (board['topR'] == board['midM'] == board['lowL'])):

                break

    if ((board['topL'] == board['topM'] == board['topR']) or
        (board['midL'] == board['midM'] == board['midR']) or
        (board['lowL'] == board['lowM'] == board['lowR']) or
        (board['topL'] == board['midL'] == board['lowL']) or
        (board['topM'] == board['midM'] == board['lowM']) or
        (board['topR'] == board['midR'] == board['lowR']) or
        (board['topL'] == board['midM'] == board['lowR']) or
        (board['topR'] == board['midM'] == board['lowL'])):
            print('****************')
            print(f'Player{i} won')
            print('****************')

            cont = input('Wanna play again?(yes/no):')
            if cont == 'yes':
                continue
            else:
                break




