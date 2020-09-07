# Write your code here :-)
#! python3.8
# sandwichmaker.py
#import pyinputplus as py

#help(py.inputMenu)

import pyinputplus as py
#help(py.inputMenu)
selectbread = py.inputMenu(['wheat','white','sourdough'])
selectbread=10
selectopping1 = py.inputMenu(['chicken','turkey','ham','tofu'])
selectopping1=10
selectcheeseYN = py.inputYesNo('want cheese?')
if selectcheeseYN == 'yes':
    selectcheese = py.inputMenu(['cheddar','Swiss','mozzarella'])
    selectcheese = 10
else:
    selectcheese = 0
selecttoppingYN = py.inputYesNo('want mayo/mustard/lettuce/tomoto?')
if selecttoppingYN == 'yes':
    selecttopping2 = py.inputMenu(['mayo','mustard','lettuce','tomoto'])
    selecttopping2=10
else:
    selecttopping2 = 0

count = py.inputNum(min=1,prompt ='Enter the no.of sandwiches')

price  = count * (selectbread+selectopping1+selectcheese+selecttopping2)
print(price)





