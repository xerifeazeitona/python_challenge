"""
Python Challenge - Level 6 - now there are pairs
"""
import os
import subprocess
import zipfile
import re
import requests

def follow_chain(next_nothing, list_of_files=None):
    """Follows the chain of nothing."""
    next_file = f'channel/{next_nothing}.txt'
    while True:
        with open(next_file) as file_obj:
            content = file_obj.read()
        print(content)
        try:
            next_nothing = re.compile(
                r'nothing is (\d*)$').search(content).group(1)
        except AttributeError:
            break
        next_file = f'channel/{next_nothing}.txt'
        if list_of_files is not None:
            list_of_files.append(f'{next_nothing}.txt')

def collect_comments(list_of_files):
    """Returns a string with the comments for each file in 'list_of_files'"""
    zipped = zipfile.ZipFile('channel.zip')
    comments = []
    for filename in list_of_files:
        comments.append(zipped.getinfo(filename).comment.decode('utf-8'))
    zipped.close()
    return ''.join(comments)

#res = requests.get('http://www.pythonchallenge.com/pc/def/channel.html')
#res.raise_for_status()
#print(res.text)

# looks like we have a zip file to download
if not os.path.exists('channel.zip'):
    subprocess.Popen(
        ['/usr/bin/wget',
         'http://www.pythonchallenge.com/pc/def/channel.zip']).wait()

# now let's see what's inside of the zip file
#channel_zip = zipfile.ZipFile('channel.zip')
#print(channel_zip.namelist())
#channel_zip.close()

# lots of files, better extract them into a separate folder
if not os.path.exists('channel'):
    channel_zip = zipfile.ZipFile('channel.zip')
    channel_zip.extractall('channel')
    channel_zip.close()

# there's a readme.txt, a nice starting point
#with open('channel/readme.txt') as file_obj:
#    print(file_obj.read())

# as hinted above, we start with 90052.txt
#with open('channel/90052.txt') as file_obj:
#    print(file_obj.read())

# This could take a long time, let's use a loop
#follow_chain('90052')

# last hint told us to collect the comments, let's do it
#channel_zip = zipfile.ZipFile('channel.zip')
#print(collect_comments(channel_zip.namelist()))
#channel_zip.close()

# the procedure is right but the order is very wrong, let's try the same
# order used to find the 'collect the comments.' hint
list_of_nothing = []
follow_chain('90052', list_of_nothing)
#print(list_of_nothing)
print(collect_comments(list_of_nothing))

# I think we got the solution here, don't we?
res = requests.get('http://www.pythonchallenge.com/pc/def/hockey.html')
res.raise_for_status()
print(res.text)

# we do indeed!
print('http://www.pythonchallenge.com/pc/def/oxygen.html')
