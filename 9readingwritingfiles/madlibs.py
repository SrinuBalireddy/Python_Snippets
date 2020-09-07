# Write your code here :-)
#! python3
# Madlibs.py  -reads text file data and allows users to modify the keywords

File = open('madlibs.txt')
Filetext = File.read()
print(Filetext)

lst = Filetext.split(' ')
print(lst)

adj = input('Enter the ADJECTIVE: ')
noun = input('Enter the Noun: ')
verb = input('Enter the verb: ')
noun2 = input('Enter the noun: ')

lst[lst.index('ADJECTIVE')]=adj
lst[lst.index('NOUN')]=noun
lst[lst.index('VERB.')]=verb+'.'
lst[lst.index('NOUN')]=noun2

final_text=' '.join(lst)
print(final_text)
File.close()

File = open('madlibs.txt','w')
File.write(final_text)
File.close()

