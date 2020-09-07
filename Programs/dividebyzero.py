# Write your code here :-)
def devide(dividenum):
    try:
        return 42/dividenum
    except ZeroDivisionError:
        print('Error : Invalid argument')

print(str(devide(0)))

def Ndivide(a):
    return 42/a

try:
    print(Ndivide(2))
    print(Ndivide(0))
    print(Ndivide(3))
except ZeroDivisionError:
    print('Error')
