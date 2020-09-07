# Write your code here :-)
#! python 3.8
# capitals.py #creates quizes with questions and answers
# in random order along with answer key

import random

capitals = {'AP':'Vizag','Telangana':'Hyd','TN':'Chennai','kerala':'cochin',
            'Karnataka':'Benguluru','Maharasthra':'Mumbai','WB':'Kolkatha'}

"""
def questionset(questions):

    global capitals

    for i in questions:
        correct_ans = capitals(
"""

for Qset in range(1,3):

    Qpaper = open('Quiz'+str(Qset)+'.txt','w')
    Anspaper = open('Answers'+str(Qset)+'.txt','w')

    print('Quiz #'+str(Qset))
    Qpaper.write('Quiz #'+str(Qset)+'\n')
    Anspaper.write('Quiz_Answers #'+str(Qset)+'\n')

    questions = list(capitals.keys())
    #print(questions)
    random.shuffle(questions)
    #print(questions)

    for i in range(len(questions)):
        #print(i)
        correct_ans= capitals[questions[i]]
        other_ans = list(capitals.values())
        del other_ans[other_ans.index(correct_ans)]
        other_ans = random.sample(other_ans,3)
        #print(correct_ans,other_ans, ='')
        correct_ans = correct_ans+'_correct'
        options = other_ans+[correct_ans]
        random.shuffle(options)
        #print(options)

        print(str(i+1)+'. What is the capital of '+ questions[i]+'?')
        Qpaper.write(str(i+1)+'. What is the capital of '+ questions[i]+'?')
        Qpaper.write('\n')
        for a in range(4):
            print(f"    {'ABCD'[a]}.{options[a]}")
            Qpaper.write(f"    {'ABCD'[a]}.{options[a]}\n")

        print(sep='')
        Qpaper.write('\n')

        Anspaper.write(f"{i+1}.{'ABCD'[options.index(correct_ans)]}")
        Anspaper.write('\n')
    Qpaper.close()
    Anspaper.close()















