"""
Python Challenge - Level 3 - re
"""
import re
import requests
res = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
res.raise_for_status()

# Load the mess into a variable
mess = re.compile(r'<!--(.*)-->').search(res.text.replace('\n', '')).group(1)

# One small letter, surrounded by EXACTLY three big boys on each of its sides
flag = ''.join(re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]').findall(mess))
print(flag)
print(f'http://www.pythonchallenge.com/pc/def/{flag}.html')
