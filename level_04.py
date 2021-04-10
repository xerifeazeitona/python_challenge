"""
Python Challenge - Level 4 - follow the chain
"""
import re
import requests

def follow_chain(next_nothing):
    """Follows the chain of nothing."""
    base_link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    next_link = base_link + next_nothing
    while True:
        res = requests.get(next_link)
        res.raise_for_status()
        print(res.text)
        try:
            next_link = base_link + re.compile(
                r'and the next nothing is (\d*)$').search(res.text).group(1)
        except AttributeError:
            print(next_link)
            break

#res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.html')
#res.raise_for_status()
#print(res.text)

# looks like this time it's a php page
#res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php')
#res.raise_for_status()
#print(res.text)

# time to follow the chain
#follow_chain('12345')
#follow_chain(str(int(16044/2)))

print('http://www.pythonchallenge.com/pc/def/peak.html')
