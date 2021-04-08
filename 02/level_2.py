"""
Python Challenge - Level 2 - ocr
"""
import re
import requests
res = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
res.raise_for_status()

# load the mess into a variable
#print(res.text.split('<!--\n')[-1][:-6])
#mess = ''.join(re.compile(r'<!--\W(.*)-->').findall(res.text.replace('\n', '')))
mess = re.compile(r'<!--\W(.*)-->').search(res.text.replace('\n', '')).group(1)

# count how many times each character appears in the mess
ranking = {}
for character in mess:
    ranking.setdefault(character, 0)
    ranking[character] += 1

# concatenate the characters that only appear once
magic_word = ''
for key, value in ranking.items():
    if value == 1:
        magic_word += key

# solution
print(f'http://www.pythonchallenge.com/pc/def/{magic_word}.html')
