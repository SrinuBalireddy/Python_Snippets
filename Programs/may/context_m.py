# Write your code here :-)

import requests

class open_file():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exe_type, exc_val, traceback):
        self.file.close()


res = requests.get('http://127.0.0.1:8000/post/36/update/')

with open_file('newfile.html','w') as f:
    f.write(res.text)

print(f.closed)

"""

import requests

res = requests.get('http://127.0.0.1:8000/post/36/update/')
print(res.text[0:250])
"""
