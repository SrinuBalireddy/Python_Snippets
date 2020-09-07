# Write your code here :-)
def collatz(number):

    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

while True:

    try:
        number = int(input('Enter the number: '))
        output = collatz(number)

        if output ==1:
            break
    except:
        print('Please enter an integer')

