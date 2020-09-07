"""
command line driven text search engine.
"""
#! python3
# Artfinder_exercise    - Command line driven text search engine

from pathlib import Path
import sys
import mmap
import re
import os
import glob

def command_line_search():
    """
    command line driven text search engine.
    """

    # Read command line arguments
    if len(sys.argv) < 2:
        print('## Please provide the path to the directory containing .txt files ##')
        sys.exit()
    else:
        path = Path(sys.argv[1])

    no_of_files = len(glob.glob1(path, '*.txt'))

    if not no_of_files:
        print('No text files in the given directory..')
        sys.exit()
    else:
        print(f'{no_of_files} files read in the given directory..')

    while True:
        result_dict = {}

        # Use glob to fetch all the .txt file into memory from the given directory.
        txt_files = path.glob('*.txt')

        # Ask the user for to input the search string.
        # converting the string to byte format for mmap object comparision
        print()
        search_str = bytes(input('Please provide the search string<(type :q to exit)>'),
                           encoding='utf-8').split()

        # exit the program if user types :q.
        if search_str == [b':q']:
            print('Existing the program..')
            sys.exit()
        elif len(search_str) == 0:
            print('No search string has been provided')
            continue

        # Search the input text in the directory files.
        for file in txt_files:
            counter = 0     # helper variable to calculate match percentage
            with open(file) as file_context:
                if os.stat(file).st_size != 0:
                    # reading the file data into memory with filesize >0
                    file_data = mmap.mmap(file_context.fileno(), 0, access=mmap.ACCESS_READ)
                    for item in search_str:
                        if re.search(rb"\b"+item+rb"\b", file_data, re.IGNORECASE):
                            counter += 1

                # load the results into dictionary
                # ZeroDivisionError is already validated.
                result_dict[file.name] = round((counter/len(search_str))*100, 2)

        # Sort the dictionary based on values.
        sorted_result_dict = sorted(result_dict, key=result_dict.get, reverse=True)

        # display the top 10 results.
        print()
        print('############Search Result#################')
        print('"filename"'.ljust(50), '"Match_percentage"'.rjust(50))
        print()
        max_range = len(sorted_result_dict) if len(sorted_result_dict) < 10 else 10
        for index in range(max_range):
            print(sorted_result_dict[index].ljust(50),
                  (str(result_dict[sorted_result_dict[index]])+'%').rjust(50))


# executing the main program
if __name__ == '__main__':
    command_line_search()
