"""
Python Challenge - Level 7 - smarty
"""

import os
import subprocess
from PIL import Image

# no luck with the source code, let's examine the image
if not os.path.exists('oxygen.png'):
    subprocess.Popen(
        ['/usr/bin/wget',
         'http://www.pythonchallenge.com/pc/def/oxygen.png']).wait()

img = Image.open('oxygen.png')
# Find out image size
#print(f'width:{img.width}\nheight:{img.height}')
# find out the right y position
#print(img.getpixel((0, img.height / 2)))
# find out the size of each square
#print([img.getpixel((x, img.height / 2)) for x in range(0, 30)])    
# get the color values of the entire line
#print([img.getpixel((x, img.height / 2)) for x in range(0, img.width, 7)])
# get the color values of the entire line minus last non-gray squares
#print([img.getpixel((x, img.height / 2))[0] for x in range(0, img.width - 21, 7)])
# get the ascii character for each number
#print([chr(img.getpixel(
#    (x, img.height / 2))[0]) for x in range(0, img.width - 21, 7)])
#print(''.join([chr(img.getpixel(
#    (x, img.height / 2))[0]) for x in range(0, img.width - 21, 7)]))
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(n) for n in next_level]))
