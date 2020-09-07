# Write your code here :-)
returnval= True

de f collatz(number):
    print('Function has been called')
    if number%2 == 0:
        return number//2
    elif (number%2) == 1:
        return 3*number+1
try:
    while returnval:
        askuser = int(input('Enter a number:'))
        funans=collatz(askuser)
        print(funans)
        if funans ==1:
            returnval=False

except ValueError:
    print('Type an integer')

