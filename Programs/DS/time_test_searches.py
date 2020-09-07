# Write your code here :-)
import time

items = [n for n in range(1000)]
target=999

def linear_search(list, target):

    for i in list:
        if i == target:
            return "element found"
    return "element not found"

start = time.perf_counter()
print(linear_search(items,target))
finish = time.perf_counter()
print(f'program finished in {round(finish-start,2)} second(s)')



import re
i= ' && && '
re_input = re.compile(r"(?<= )&& ")
re_text = re_input.findall(i)
print(re_text)
#print(re_text.sub(r"\s+&&+\s",' and '))
print(re_input.sub('and ',i))

sub_string= 'CDC'
string = 'ABCDCDC'

#compile_string = f'r"(?<={sub_string[-1]})({sub_string})"'
compile_string = f"(?<={sub_string})"
                 #f"'(?={sub_string})'"
print(compile_string)

re_input = re.compile(compile_string)
re_text = re_input.findall(string)
print(len(re_text))
print(re_text)

s= 'Srinu'
print(s[::-1])

