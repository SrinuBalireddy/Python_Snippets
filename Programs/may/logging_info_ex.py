# Write your code here :-)
# Write your code here :-)
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level = logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of program')

def factorial(n):
    logging.info ('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1,n+1):
        total*=i
        logging.info('i is '+str(i)+ ', total is ' + str(total))

    logging.info('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.info('End of program')

import PyPDF2
print(help(PyPDF2))

