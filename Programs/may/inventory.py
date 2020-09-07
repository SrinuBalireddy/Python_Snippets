# Write your code here :-)

invent = {'rope':1, 'torch': 6 , 'gold coin': 42, 'dagger':1, 'arrow':12}
items = ['gold coin', 'torch', 'glue', 'gold coin', 'dagger', 'spiral']

def displayinventory(invent):

    count =0

    for k,v in invent.items():
        count += v

        print(f'{v} {k}')

    print('Total Number of items:'+ str(count))
    print('')

#displayinventory(invent)

def addinventory(invent, additems):

    for item in additems:
        if item in invent:
            invent[item] = invent[item]+1
        else:
            invent.setdefault(item,1)


displayinventory(invent)
addinventory(invent,items)
displayinventory(invent)
