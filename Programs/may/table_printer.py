# Write your code here :-)

items=[['ahk','bwods','caaf','drhr'],
       ['elll','fd','gdrsg','hferf'],
       ['ikokok','jjjsss','kw','lwww']]



for innerindex in range(len(items[0])):
    for index in range(len(items)):
        print(items[index][innerindex].rjust(10) , end ='')
    print('')



