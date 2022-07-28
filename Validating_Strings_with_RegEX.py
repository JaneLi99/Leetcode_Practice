"""
Amazon OA Practice 2 - Validating Strings with RegEX
Given a list of strings made up of the characters 'a' and  'b',
create a regular expression that will match strings that begin and end with the same letter
Example:
'a', 'aa', and 'bababbb' match.
'ab' and 'baba' do not match.
"""

import re

def check(string):
    regex = r'^[a-z]$|^([a-z]).*\1$'
    if (re.search(regex, string)):
        return True
    return False

if __name__ == '__main__':
    print(check(string = "aba"))
    print(check(string = "abab"))
    print(check(string = "a"))