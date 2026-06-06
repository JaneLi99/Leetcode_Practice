# Problem: Count Words With Matching First and Last Letters
# You are given a string s consisting of words separated by spaces.
# A word is considered valid if its first and last characters are the same, ignoring letter case.
# Return the number of valid words in the string.
#
# Example 1
# Input: s = "level apple radar banana"
# Output: 2
# Explanation:
# "level" → first = l, last = l → valid
# "apple" → first = a, last = e → invalid
# "radar" → first = r, last = r → valid
# "banana" → first = b, last = a → invalid
# Total valid words = 2
#
# Example 2
# Input: s = "Anna civic kayak test"
# Output: 3
# Explanation:
# Case is ignored.
# "Anna" → a == a → valid
# "civic" → c == c → valid
# "kayak" → k == k → valid
# "test" → t != t? Actually t == t, so valid → correction: output should be 4 if counted.
# (Example adjusted depending on interpretation.)

def countMatchingWords(s: str) -> int:
    count = 0

    for word in s.split():
        if word[0].lower() == word[-1].lower():
            count += 1

    return count

def main():
    # Test Case 1
    s = "level apple radar banana"
    print("Test Case 1")
    print("Input:", s)
    print("Output:", countMatchingWords(s))
    print()

    # Test Case 2
    s = "Anna civic kayak test"
    print("Test Case 2")
    print("Input:", s)
    print("Output:", countMatchingWords(s))
    print()

    # Test Case 3
    s = "Hello wow noon world"
    print("Test Case 3")
    print("Input:", s)
    print("Output:", countMatchingWords(s))
    print()

    # Test Case 4
    s = "a aa aba abc"
    print("Test Case 4")
    print("Input:", s)
    print("Output:", countMatchingWords(s))


if __name__ == "__main__":
    main()