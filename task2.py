from collections import deque


def is_palindrome(string):
    dq = deque(string.lower().replace(' ', ''))

    matches = True

    while matches and len(dq) > 1:
        first = dq.popleft()
        last = dq.pop()

        matches = first == last

    print('"{string}" is {arg}a palindrome.'.format(string=string, arg=('' if matches else 'not ')))
    return matches
