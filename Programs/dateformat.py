# Write your code here :-)
#! python
# dataformat.py - detect dates in DD/MM/YYYY format

# reg expr to read the dates from variable
# store the day,month,year to seperate variable
# validate day,month,year values


import re

dates = '01/10/2019	20/02/2000	29/02/2001 40/02/1999	10/40/2000 2/1/1999 02/4/2000 19/04/99	31/04/1999		10/05/2018	24/11/1989		31/06/2010	04/11/2011  30/02/2000		28/07/2001'
#print(dates)
valid_dts =[]
invalid_dts =[]
date_expr = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
#date_expr = re.compile(r'\d{2}/\d{2}/\d{4}')
dt_search = date_expr.findall(dates)
print(dt_search)
print(len(dt_search))


for group in dt_search:
    day,month,year=group

    if int(day) in range(1,32) and int(month) in range(1,13) and int(year) in range(1000,2999):

        if month in ['04','06','09','11']:
            if int(day)>30:
                print('Data :'+day+'/'+month+'/'+year+' is invalid')
                invalid_dts.append(day+'/'+month+'/'+year)
            else:
                print('Data :'+day+'/'+month+'/'+year+' is valid')
                valid_dts.append(day+'/'+month+'/'+year)

        elif month == '02':
            if int(year)%4 == 0:
                if int(day)>29:
                    print('Data :'+day+'/'+month+'/'+year+' is invalid')
                    invalid_dts.append(day+'/'+month+'/'+year)
                else:
                    print('Data :'+day+'/'+month+'/'+year+' is valid')
                    valid_dts.append(day+'/'+month+'/'+year)
            else:
                if int(day)>28:
                    print('Data :'+day+'/'+month+'/'+year+' is invalid')
                    invalid_dts.append(day+'/'+month+'/'+year)
                else:
                    print('Data :'+day+'/'+month+'/'+year+' is valid')
                    valid_dts.append(day+'/'+month+'/'+year)
        else:
            print('Data :'+day+'/'+month+'/'+year+' is valid')
            valid_dts.append(day+'/'+month+'/'+year)
    else:
        print('Data :'+day+'/'+month+'/'+year+' is invalid')
        invalid_dts.append(day+'/'+month+'/'+year)

print('Valid Dates: '+str(len(valid_dts)))
print('Invalid Dates: '+str(len(invalid_dts)))
