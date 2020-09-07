# Write your code here :-)
'''
import calendar

def solution(Y, A, B, W):

    vacation_weeks=0
    lapse=0
    totalweeks=[]

    months= {'January':1, 'February':2, 'March':3, 'April':4,
             'May':5,'June':6,'July':7,'August':8,'September':9,
             'October':10, 'November':11,'December':12}

    diff = months[B]-months[A]

    for monthno in range(months[A],months[A]+diff+1):
        totalweeks+= calendar.monthcalendar(Y,monthno)



    print(totalweeks)

    if 0 in totalweeks[0]:
        del totalweeks[0]

    if 0 in totalweeks[-1]:
        del totalweeks[-1]
    print()
    print(totalweeks)


    weeks = calendar.monthcalendar(Y,A)
    weeks2 = calendar.monthcalendar(Y,B)
    weeks = weeks+weeks2
    print(weeks)

    if 0 in weeks[0]:
        del weeks[0]

    if 0 in weeks[-1]:
        del weeks[-1]
    print()

    print(weeks)

    for week in weeks:
        if 0 in week:
            lapse+=1
        #vacation_weeks+=1

    #return vacation_weeks
    #return len(weeks)

print(solution(2020,'June','July',1))
'''

import calendar

def solution(Y, A, B, W):
    # write your code in Python 3.6

    vacation_weeks=0
    lapse=0
    totalweeks=[]

    months= {'January':1, 'February':2, 'March':3, 'April':4,
             'May':5,'June':6,'July':7,'August':8,'September':9,
             'October':10, 'November':11,'December':12}

    diff = months[B]-months[A]

    for monthno in range(months[A],months[A]+diff+1):
        totalweeks+= calendar.monthcalendar(Y,monthno)

    if 0 in totalweeks[0]:
        del totalweeks[0]

    if 0 in totalweeks[-1]:
        del totalweeks[-1]

    for week in totalweeks:
        if 0 in week:
            lapse+=1
        #vacation_weeks+=1

    lapse = int(lapse/2)

    return len(totalweeks)-lapse


print(solution(2020,'September','December',1))

print(calendar.monthcalendar(2020,6)+calendar.monthcalendar(2020,7))

def newcal():
    """This is a test function"""
    pass
    print(newcal.__doc__)

newcal()
