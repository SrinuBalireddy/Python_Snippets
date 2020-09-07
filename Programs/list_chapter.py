# Write your code here :-)
num =[0,1,2,3,4,5]
for i in range(len(num)):
    print('The num in the index '+ str(i) + ' of the list: ' + str(num[i]))
print('-----------------------')
for a,b in enumerate(num):
    print('The num in the index '+ str(a) + ' of the list: ' + str(num[b]))

import random
print(random.choice(num))

num1=num.sort()
print(num1)

num2=sorted(num)
print(num2)

def listtest(parm):
    parm.sort(reverse = True)

listtest(num2)
print(num2)

