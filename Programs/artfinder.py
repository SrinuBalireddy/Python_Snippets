# Write your code here :-)
#! python3
# Artfinder_exercise    - Command line driven text search engine

from pathlib import Path
import sys
import mmap
import re

result_dict = {}

# TODO: Read command line arguments.
if len(sys.argv) < 2:
    print('## Please provide the path to the directory containing .txt files ##')
    sys.exit()
else:
    path = Path(sys.argv[1])
    #print(path)
    #print(type(path))

# TODO: Use glob to fetch all the .txt file in the given directory.
txt_files =  path.glob('*.txt')  # check if there are any text files

# TODO: Ask the user for search string input.
search_str = bytes(input('Please provide the search string> '), encoding='utf-8').split()
#search_str = input('Please provide the search string> ').split()
#print(search_str)

# TODO: Search the input text in the directory files.
for file in txt_files:
    counter = 0
    with open(file, buffering=200) as f:
        """
        s =  f.read().split()
        print(sys.getsizeof(s))
        #s1 = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        #print(sys.getsizeof(s1))
        #print(sys.getsizeof(s1.readlines()))
        for item in search_str:
            if item in s:
                counter += 1
        """
        """
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        print(str(s))
        for item in search_str:
            if s.find(item) != -1:
                counter += 1
        """
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        for item in search_str:
            print(item)
            if re.search(rb"\b"+item+rb"\b", s):
                counter += 1

        percentage_match = round((counter/len(search_str))*100, 2)
        result_dict[file.name] = percentage_match
        print(f'{file.name}: {str(percentage_match)}%')
        #print(result_dict)
        sorted_result_dict = sorted(result_dict, key=result_dict.get, reverse = True)
        #print(sorted_result_dict)

