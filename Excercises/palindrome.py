# Write your code here :-)

str='malayalam1'

lst=list(str)
lstnew=list(str)
lstnew.reverse()
print(lst)
print(lstnew)

if lst==lstnew:
    print(str+' is a palindrome')
else:
    print(str+' is not a palindrome')
