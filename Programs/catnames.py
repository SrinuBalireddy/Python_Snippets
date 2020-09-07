# Write your code here :-)
catnames = []
while True:
    print('Enter you cat name')
    name = input()
    if name == '':
        break
    catnames = catnames+[name]
print('Your cat names are')
for names in catnames:
    print(' '+names)
