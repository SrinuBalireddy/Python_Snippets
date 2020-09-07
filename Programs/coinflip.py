# Write your code here :-)
import random
ResultList = []
Probability=0

for i in range(10):
    for i in range(100):
        if random.randint(0,1) == 0:
            ResultList.append('H')
        else:
            ResultList.append('T')


    print(len(ResultList))
    '''
    print(ResultList)
    print(list('H'*6))
    print(ResultList[0:6])
    '''

    for x in range(len(ResultList)):
        if ResultList[x:x+6]==list('H'*6) or ResultList[x:x+7]==list('T'*6):
            Probability+=1

print(Probability)
print('chance : %s%%' % (Probability/100))












