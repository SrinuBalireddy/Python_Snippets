# Write your code here :-)
"""
#1
items={'rope':1,'sticks':5,'rods':40,'scales':10,'boxes':12}

def displayinventory(dictname):
    count=0
    print('Inventory detials:')
    for k,v in dictname.items():
        print(str(v)+' '+k)
        count= count+v
    print('Total number of items: '+str(count))

displayinventory(items)
"""

#2
items={'rope':1,'sticks':5,'rods':40,'scales':10,'boxes':12}
newitems = ['rope','sticks','rope','rods','boxes','tape','tape']
newdict={}

def displayinventory(dictname):
    count=0
    print('Inventory detials:')
    for k,v in dictname.items():
        print(str(v)+' '+k)
        count= count+v
    print('Total number of items: '+str(count))

def AddtoInventory(dictname,newitems):
    count=''
    for i in newitems:
        if i in dictname.keys():
            dictname[i]=dictname[i]+1
            #print(dictname)
        else:
            dictname.setdefault(i,1)
            #print(dictname)
    return dictname

displayinventory(items)
newdict=AddtoInventory(items,newitems)
print('----------------------------')
displayinventory(newdict)




