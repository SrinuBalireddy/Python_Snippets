# Write your code here :-)
# python
# Tableprinter.py # prints list of lists in a tabular format with proper spacing

items=[['ahk','bwods','caaf','drhr'],
       ['elll','fd','gdrsg','hferf'],
       ['ikokok','jjjsss','kw','lwww'],
       ['mertyuii','nk','ooooo','pllklp']]
itemlen=[]
maxval=''

for i in range(len(items)):
    for j in range(len(items[i])):
        itemlen.append(len(items[j][i]))

maxval=max(itemlen)

def table(item,rw):
    print('Printing the items'.center(rw,'.'))
    for i in range(len(item)):
        for j in range(len(item[i])):
            #print(i,j,end='')
            print(item[j][i].rjust(rw),end=' ')
        print(sep='')


table(items,maxval)

