# Write your code here :-)
"""
import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'
outfile  = open(filename,'wb')

pickle.dump(dogs_dict,outfile)
outfile.close()
"""

values = [1,5,8,9,3,6,7]
target = 9
myset = set()

for i in range(len(values)):
    diff = target-values[i]
    if diff in values:
        myset.update((values[i],diff))
        #print(values[i], diff, sep=' ')
print(myset)






