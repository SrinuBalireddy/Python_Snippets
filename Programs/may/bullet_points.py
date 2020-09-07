# Write your code here :-)

import pyperclip


str = pyperclip.paste()
new_str = str.split('\n')

print(new_str)

for i in range(len(new_str)):

    new_str[i] = '* '+new_str[i]


pyperclip.copy('\n'.join(new_str))
