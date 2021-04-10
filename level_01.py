"""
Python Challenge - Level 1 - What about making trans?
"""
import string
#import requests
#res = requests.get('http://www.pythonchallenge.com/pc/def/map.html')
#res.raise_for_status()
#print(res.text)

INPUT_TEXT = string.ascii_lowercase         # abcdefghijklmnopqrstuvwxyz
OUTPUT_TEXT = INPUT_TEXT[2:]+INPUT_TEXT[:2] # cdefghijklmnopqrstuvwxyzab
TRANSLATION_TABLE = str.maketrans(INPUT_TEXT, OUTPUT_TEXT)
CYPHER_TEXT = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr \
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw \
rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu \
ynnjw ml rfc spj."""

#print(CYPHER_TEXT.translate(TRANSLATION_TABLE))

# The encrypted text told us to apply the same translation to the url
#print('map'.translate(TRANSLATION_TABLE)) # solution here

# Success, let's print out the next level url
print('http://www.pythonchallenge.com/pc/def/ocr.html')
