"""
Python Challenge - Level 8 - working hard?
"""

import bz2
#import requests

#res = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
#res.raise_for_status()
#print(res.text)

# got credentials from the source code, now we 'inflate' the credentials
USERNAME = bz2.decompress(
    b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 '
    b'\x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084').decode()
PASSWORD = bz2.decompress(
    b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M'
    b'\x13<]\xc9\x14\xe1BBP\x91\xf08').decode()

print('http://www.pythonchallenge.com/pc/return/good.html')
print(f'un: {USERNAME}\npw: {PASSWORD}')
