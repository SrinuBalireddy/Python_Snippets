# Write your code here :-)
allguests = {'Alice':{'Apples':6,'Eggs':5},
             'Bob':{'Apples':7,'Spices':5}
            }

def totalguests(guests,item):
    numbrough=0
    for k,v in guests.items():
        numbrough= numbrough+v.get(item,0)
    return numbrough

print('No of things being brough:')
print('-Apples       '+str(totalguests(allguests,'Apples')))
#print('-Apples       '+str(totalguests(allguests,'Alice')))
