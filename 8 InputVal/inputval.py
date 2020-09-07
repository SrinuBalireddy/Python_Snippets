# Write your code here :-)
import pyinputplus as py

#var=py.inputStr()
#var= py.inputNum()
#var = py.inputChoice(['a','b','c'])
#var = py.inputYesNo()
#var = py.inputDatetime()
#var = py.inputEmail()
#var = py.inputPassword()
#var = py.inputFilepath()
#var = py.inputNum(prompt ='Enter a number',timeout=10,default='Srinu' )
#var = py.inputStr(blockRegexes=[r'[A|B|C]'])
#var = py.inputChoice(['A','B','C'], blockRegexes=([r'[A-Ca-c']))
#print(var)


#help(py.inputChoice)

#busy program

"""
while True:
    var = py.inputYesNo(prompt='would you like to keep an idiot busy?(Yes/No)')
    if var == 'no':
        print('Have a great day, Bye!')
        break

"""

#multiplication quiz

import random,time

numofQ=10
correct = 0
for q in range(numofQ):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt ='#%s: %s*%s = ' % (q,num1,num2)

    try:
        py.inputStr(prompt,allowRegexes = ([r'^%s$' % (num1 * num2)]),
                    blockRegexes = [('.*','Incorrect!')],
                    timeout =8,
                    limit =3)
    except py.TimeoutException:
        print('out of time!')
    except py.RetryLimitException:
        print('Out of Tries!')

    else:
        print('Correct!')
        correct+=1

    time.sleep(1)

print('Score: %s / %s' % (correct,numofQ))

