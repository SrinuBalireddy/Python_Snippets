# Write your code here :-)

spam =['apples', 'bananas', 'tofu', 'cats','eggs','apples', 'bananas', 'tofu', 'cats','eggs']


def comma(mylist):

    substr=''
    if len(mylist) != 0:
        sublist = mylist[1:(len(mylist)-1)]

        for item in sublist:
            substr += ', '+ item

        print(mylist[0]+substr+', and '+ mylist[-1])
    else:
        print('No list of items')

comma([])
