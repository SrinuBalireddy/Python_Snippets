import unittest
import sys
import glob
import os
import mmap
import re
from pathlib import Path

class Test_command_line_search(unittest.TestCase):

    def setUp(self):
        self.path = Path.cwd()
        self.text_files = self.path.glob('*.txt')

    def helper_func(self, search_str):
        """ helper function to calculate the match percentage """

        for file in self.text_files:
            counter = 0
            with open(file) as f:
                if os.stat(file).st_size != 0:
                    file_data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                    for item in search_str:
                        if re.search(rb"\b"+item+rb"\b", file_data, re.IGNORECASE):
                            counter += 1
            return counter

    def test_arguments_len(self):
        """ test if the directory name is provided as a cmd line argument """

        with self.assertRaises(IndexError):
            _ = sys.argv[1]

    def test_txt_extension(self):
        """ test to validate the files extracted by glob are .txt extension """

        for file in self.text_files:
            self.assertEqual(file.suffix,'.txt')

    def test_in_memory_allocation_size(self):
        """ test glob file storage vs original file storage """

        glob_storage = sys.getsizeof(self.path.glob('*.txt'))
        file_storage = 0

        for file in self.text_files:
            file_storage += sys.getsizeof(file)

        self.assertGreater(file_storage, glob_storage)

    def test_match_percentage(self):
        """ validate match percentage """

        search_str = bytes('srinu python',encoding='utf-8').split()
        res = self.helper_func(search_str)
        self.assertAlmostEqual(round((res/len(search_str))*100, 2), 50.00)

        search_str = bytes('srinu python abc',encoding='utf-8').split()
        res = self.helper_func(search_str)
        self.assertAlmostEqual(round((res/len(search_str))*100, 2), 66.67)

        search_str = bytes('srinu python tenet',encoding='utf-8').split()
        res = self.helper_func(search_str)
        self.assertAlmostEqual(round((res/len(search_str))*100, 2), 33.33)


if __name__ == '__main__':
    unittest.main()


