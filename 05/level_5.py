"""
Python Challenge - Level 5 - peak hell
"""

import os
import pickle # Peak hell 'rhymes' with pickle
import subprocess
import requests

res = requests.get('http://www.pythonchallenge.com/pc/def/peak.html')
res.raise_for_status()
#print(res.text)

# looking at the source code we found this interesting file
if not os.path.exists('banner.p'):
    subprocess.Popen(['/usr/bin/wget', 'http://www.pythonchallenge.com/pc/def/banner.p']).wait()

# the contents of the file have been pickled! we need to unpickle them
with open('banner.p', 'rb') as file_obj:
    data = pickle.load(file_obj)
#print(data)

# it's a list of lists of tuples, with a character and a number, let's print it
for line in data:
    for character, count in line:
        print(character * count, end='')
    print()

print('http://www.pythonchallenge.com/pc/def/channel.html')
