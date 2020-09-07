# Write your code here :-)
def movestr(spam):
    spamlist = list(spam)

    for letter in spam:
        if letter == 'x':
            spamlist.remove(letter)
            spamlist.append(letter)
    return ''.join(spamlist)

print(movestr('axvxktxp'))

def movestr_rec(spamlist,i=0):

    i+=1
    print(i)

    if 'x' in spamlist:
        if i == len(spamlist):
            return ''.join(spamlist)
        spamlist.remove('x')
        spamlist.append('x')
        return movestr_rec(spamlist,i)

print(movestr_rec(list('axvxktxp')))
