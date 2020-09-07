# Write your code here :-)
# python
# piglatin.py #Add yay to a word starting with vowel,
              #Add ay to a word starting with consonant and move the consonant to the end

text='Srinu is good and he is 30yrs old'
newtext= text.split(' ')
print(newtext)

for i in range(len(newtext)):
    if newtext[i].upper().startswith('A') or newtext[i].upper().startswith('E') or newtext[i].upper().startswith('I') or newtext[i].upper().startswith('O') or newtext[i].upper().startswith('U'):
        newtext[i]=newtext[i]+'yay'
    else:
        temp=newtext[i]
        for k in range(len(temp)):
            #temp[a]=temp[1:]+temp[0]
            newtext[i]=temp[1:]+temp[0]+'ay'


print(newtext)



