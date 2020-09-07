# Write your code here :-)
#! python3
# Artfinder_exercise    - Command line driven text search engine

from pathlib import Path
import sys
import mmap
import re
import os
import glob

result_dict = {}
search_str = b''

# TODO: Read command line arguments.
if len(sys.argv) < 2:
    print('## Please provide the path to the directory containing .txt files ##')
    sys.exit()
else:
    path = Path(sys.argv[1])

# TODO: Use glob to fetch all the .txt file in the given directory.
txt_files =  path.glob('*.txt')

if not len(glob.glob1(path, '*.txt')):
    print('No text files in the given directory')
    sys.exit()

# TODO: Ask the user for search string input.
search_str = bytes(input('Please provide the search string<(type :q to exit)>'), encoding='utf-8').split()

# TODO: exit the program if user types quit.
if search_str == [b':q']:
    sys.exit()

# TODO: Search the input text in the directory files.
for file in txt_files:
    counter = 0
    with open(file) as f:
        if os.stat(file).st_size != 0:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            for item in search_str:
                if re.search(rb"\b"+item+rb"\b", s, re.IGNORECASE):
                    counter += 1

        result_dict[file.name] = round((counter/len(search_str))*100, 2)

# Sort the dictionary based on values.
sorted_result_dict = sorted(result_dict, key=result_dict.get, reverse = True)

# display the top 10 results.
print()
print('############Search Result#################')
print('"filename"'.ljust(50), '"Match_percentage"'.rjust(50))
print()
max_range = len(sorted_result_dict) if len(sorted_result_dict) < 10 else 10
for index in range(max_range):
    print(sorted_result_dict[index].ljust(50), (str(result_dict[sorted_result_dict[index]])+'%').rjust(50))

