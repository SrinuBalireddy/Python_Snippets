# Write your code here :-)
import csv

#outputFile = open('example1.csv', 'w', newline='')
outputFile = open('example1.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','news','heros'])
outputWriter.writerow(['Hello,world','eggs','news','heros'])
outputWriter.writerow(['10','11','12','13'])
outputWriter.writerow(['0.1','a1i82','b&eey','heros1'])
outputFile.close()

inputFile = open('example.csv')
inputReader = csv.reader(inputFile)
#exampleReader = list(inputReader)


for row in inputReader:
    print(str(inputReader.line_num)+' : '+ str(row))
