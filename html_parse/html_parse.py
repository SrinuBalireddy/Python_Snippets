#! python 3.8
# html_parse.py - Parses a html file to validate a condition

from pathlib import Path        # to convert a string to a path variable
from bs4 import BeautifulSoup   # module to parse html

# reading the input files folder path
p = Path(r"C:\Users\srinu\Desktop\Python\hanisha")
# glob creates a generator of .html available in the folder
files = p.glob('*.html')    # here files is a generator variable


# looping through the files. Note we have casted the files variable to a list
for file in list(files):
    valuesList = []             # creates an empty list to store high , medium and low values
    with open(file,'r') as f:
        content = f.read()      # reading the contents of each file

    # just to display the file name for our reference - remove this line in prod
    print(f'Reading file {file}')
    # parsing the context data using html parser
    soup = BeautifulSoup(content, 'html.parser')
    # .summary is the class of the summary of alerts table
    summary_data = soup.select('.summary td')

    # looping through alert values. [1::2] is used to skip looping through the labels
    for value in summary_data[1::2]:
        # store the values of the high , medium and low lables
        valuesList.append(int(value.getText()))

    # unpacking the list to corresponding variables
    high, medium, low = valuesList[:3]

    # just to display the values for our reference - remove this line in prod
    print(high, medium, low)

    # validating the varaible values
    if high>0 or medium>0 or low>2:
       print('This file has unexpected alert values')
       print('Parsing aborted - Write you notification code/ docker image reading exit code here')
       # if this condition evaluates true , break stmt will exit the loop and will not parse the next files
       # write your code here to stop reading the docker images
       break
    else:
        print('No invalid values found in this file')
    print('')

