# Write your code here :-)
"""
spam =[1,2,3,4,5]

def gen(spam):
    for i in spam:
        yield (i*i)
        yield (i*2)

res = gen(spam)

for num in res:
    print(num)
print(res)

def testgen(index):
  weekdays = ['sun','mon','tue','wed','thu','fri','sat']
  yield weekdays[index]
  yield weekdays[index+1]

day = testgen(0)
print(next(day), next(day))

spam =[1,2,3,4,5]
print(str(spam))
print(type(str(spam)))

weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)
"""

list1 = ['a','b','c']
list2 = [1,2,3]

for alpha, num in zip(list1,list2):
    print(f'{alpha}:{num}')


weekdays = ['sun','mon','tue','wed','thu','fri','abc']

print(weekdays[1::2])

listAsDict = dict(zip(weekdays[0::2], weekdays[1::2]))
print(listAsDict)


list1 = ['f', 'o', 'o']
list2 = ['hello', 'world']
lst3= []

for lst1,lst2  in zip(list1, list2):
    lst3.append(lst1)
    lst3.append(lst2)

lst3.append(list1[-1])
print(lst3)

lst4=[None]*(len(list1+list2))
print(lst4)

lst4[0::2] = list1
lst4[1::2] = list2

print(lst4)


#####

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

res = [[x, weekdays.count(x)] for x in set(weekdays)]
print(res)

####

new = ['a',1,'b','v',800,'23']

del new[0]
new.remove(1)

weekdays = ['sun','mon','Tue','wed','thu','fri','Sun','Mon','mon']

weekdays.sort(reverse = True)
print(weekdays)
weekdays.sort(key = str.lower, reverse =False)
print(weekdays)
