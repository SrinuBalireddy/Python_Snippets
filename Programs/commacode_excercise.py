# Write your code here :-)
#spam =['apples','bananas','tofu','cats']
"""
spam =['apples']
newspam=''

def commacode(name):
    global newspam
    newspam=newspam+str(name)
    return newspam
try:
    for i in range(len(spam)):
        if i == 0:
            res=commacode(spam[i])
        elif i== len(spam)-1:
            res=commacode(', and '+spam[i])
        else:
            res=commacode(', '+spam[i])


    print(res)

except NameError:
    print('Please provide non empty list')
"""

"""
----------------------------------------------------
spam =['apples','bananas','tofu','cats']

def stringlist(name):
    if len(name) ==1:
        return name[0]
    return (', '.join(name[:-1])+', and ' + name[-1])

newspam=stringlist(spam)
print(newspam)

---------------------------------------
"""
spam =['apples','bananas','tofu','cats']

def commalist(listname):
    print(*listname[:-1], sep = ', ',end=", "),
    print('and',listname[-1])

commalist(spam)
