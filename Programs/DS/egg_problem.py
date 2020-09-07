# Write your code here :-)

import random

def batch_iteration(list,low,high):

    #iterate through low and high range of the list
    for i in range(low,high):
        cracked = random.choice(['Y','N'])
        if cracked == 'N':
            continue
        else:
            print('Floor number: '+ str(list[i-1]))
            break

def eggtest(list, low, high):

    mid = (low+high)//2
    cracked = random.choice(['Y','N'])
    if cracked == 'Y':
        high = mid-1
        return batch_iteration(list, low, high)
    else:
        low = mid+1
        return eggtest(list, low, high)


floorlist = [n for n in range(1,100)]
eggtest(floorlist,0,len(floorlist)-1)

#return mt.ceil((-1.0 + mt.sqrt(1 + 8 * k)) / 2)
