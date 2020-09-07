
# Write your code here :-)
import random
def getAnswer(randonnum):
    if randonnum == 1:
        return 'No.1'
    elif randonnum == 2:
        return 'No.2'
    elif randonnum == 3:
        return 'No.3'

print(getAnswer(random.randint(1,3)))
