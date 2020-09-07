# Write your code here :-)
"""
#testing string isX functions ---
while True:
    pwd = input('Enter your password:')
    if pwd.isalpha():
        break
    print('Password can only have alphabets and integers')

----------------------------------------
spam= 'Hello#world'
before,sep,after=spam.partition('#')
print(before,sep,after, sep='\n')

"""
items = {'Sandwich':5,'Boiled Eggs':2,'Coffee':3,'Roll':4}
print(items)

def displayitems(items,rw,lw):
    print(rw)
    print('Sandwich Station Menu'.center(rw+lw,'#'))
    for k,v in items.items():
        print(k.ljust(rw,'.'),str(v).rjust(lw,'.'),sep='')



displayitems(items,20,20)
