"""
Python Challenge - Level 10 - what are you looking at?
"""


def get_next_member(previous_member):
    """Returns the next_member of the look and say sequence"""
    previous_digit = previous_member[0]
    count = 0
    next_member = ''

    for current_digit in previous_member:
        if current_digit == previous_digit:
            count += 1
        else:
            next_member += f'{count}{previous_digit}'
            count = 1
        previous_digit = current_digit
    next_member += f'{count}{previous_digit}'

    return next_member


a = ['1']
for i in range(30):
    a.append(get_next_member(a[-1]))
print(f'len(a[30]) = {len(a[30])}')

print('http://www.pythonchallenge.com/pc/def/5808.html')
