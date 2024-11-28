"""
IBM OA 1

Given a string with uppercase English letters, remove all occurrences of the string AWS until no more remain.
After each removal, the prefix and suffix strings are concatenated. Return the final string. If the final string
is empty, return -1 as a string

Examples:
s = "AWSAWSSG"
    AWSAWSSG -> AWSG
    AWSG -> G
Return the final string, G

Function Description
Complete the function getFinalString in the editor below.
The function getFinalString has the following parameter:
    string s[n]: a string of uppercase English characters

Return
String: the string after removing all occurrences of "AWS" from the given string or "-1"
"""

def getFinalString(s):
    while "AWS" in s:
        s = s.replace("AWS", "")

    if s:
        return s
    else:
        return "-1"

if __name__ == "__main__":
    print(getFinalString(s = "AWSAWSSG"))
    print(getFinalString(s = "AWSG"))
    print(getFinalString(s = ""))