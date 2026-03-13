# You are given a string word consisting of lowercase English letters,
# and a list of strings skeletons consisting of '-' characters and lowercase English letters.
# Every skeleton will always be the same length as word.
#
# Your task is to return a list of skeletons that can form the given word.
# A skeleton can form a word if all '-' characters can be replaced with characters taken from the same skeleton to make the string equal to word.
# If no strings within skeletons can form the given word, return an empty list.
# The matching skeletons should be returned in the same order they appear in skeletons.
# The list of skeletons may contain duplicates.

# Example
# word = "hello"
# skeletons = ["he-lo", "he--o", "-ell-", "hello"]
# Output: ["he-lo", "hello"]

# Explanation
# "he-lo" is a skeleton of "hello"
# There is one '-' character which should be an l.
# There is an l in the skeleton already (4th position).
#
# "he--o" is NOT a skeleton of "hello"
# There are two '-' characters which should both be l.
# But there are no l characters in the skeleton.
#
# "-ell-" is NOT a skeleton of "hello"
# Two '-' characters should be h and o.
# But there are no h or o characters in the skeleton.
#
# "hello" is a skeleton of "hello" because it already matches.

# Input / Output
# Execution limits
# execution time limit: 4 seconds (py3)
# memory limit: 1 GB
# Input
# string word
# A word consisting of lowercase English letters.
#
# Constraints
# 0 < word.length ≤ 100
# array<string> skeletons
#
# An array of strings consisting of '-' characters and lowercase English letters.
# Constraints
# 1 ≤ skeletons.length ≤ 100
# skeletons[i].length == word.length

from typing import List


def solution(word: str, skeletons: List[str]) -> List[str]:
    result = []

    # Write your solution here
    for skeleton in skeletons:
        if can_form_word_better_solution(word, skeleton):
            result.append(skeleton)

    return result


def can_form_word(word: str, skeleton: str) -> bool:
    """
    Return True if skeleton can form the word.
    """
    if word == skeleton:
        return True

    for i in range(len(word)):
        if skeleton[i] == word[i]:
            continue
        else:
            if skeleton[i] == "-" and word[i] in skeleton:
                continue
            else:
                return False

    return True

def can_form_word_better_solution(word: str, skeleton: str) -> bool:
    """
    Return True if skeleton can form the word.
    """
    letters = set(c for c in skeleton if c != "-")

    for w, s in zip(word, skeleton):
        if s == "-":
            if w not in letters:
                return False
        elif s != w:
            return False

    return True

def main():
    word = "hello"
    skeletons = ["he-lo", "he--o", "-ell-", "hello"]

    output = solution(word, skeletons)

    print("Word:", word)
    print("Skeletons:", skeletons)
    print("Output:", output)


if __name__ == "__main__":
    main()