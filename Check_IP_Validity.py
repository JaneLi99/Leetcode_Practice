"""
Cisco OA 3
Given an input IPv4 addresses as a string. Check whether the IPv4 address is valid.

Input
The first line of the input consists of a string - addressIP, representing the IPv4 address.

Output
Print a string "VALID" if the IPv4 address is valid. Otherwise, print "INVALID".

Note
The output should be VALID or INVALID

Example
Examlpe 1:
Input: 10.102.34.48
Output: VALID
Example 2:
Input: 64.233.161.256
Output: INVALID
"""

def checkIPValidity(addressIP):
    parts = addressIP.split('.')
    if len(parts) != 4 or ' ' in parts:
        return "INVALID"

    for p in parts:
        if not 0 < len(p) < 4:
            return "INVALID"
        if p[0] == "0" and len(p) > 1:
            return "INVALID"
        if not p.isdigit():
            return "INVALID"
        if not 0 <= int(p) <= 255:
            return "INVALID"
    return "VALID"

def main():
    addressIP = str(input())

    result =checkIPValidity(addressIP)
    print(result)

if __name__ == "__main__":
    main()