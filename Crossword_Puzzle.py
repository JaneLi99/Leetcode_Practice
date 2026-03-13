# Most crossword puzzle fans are used to anagrams — groups of words with the same letters in different orders —
# for example, OPTS, SPOT, STOP, POTS and POST. Some words, however, do not have this attribute:
# no matter how you rearrange their letters, you cannot form another word.
#
# Such words are called ananagrams. An example is QUIZ: there are no other words with the letters Q, U, I, and Z,
# but in a different order. Whether something is an ananagram depends on the domain we are working in; you might think that ATHENE is an ananagram,
# whereas a chemist might quickly think of ETHANE. One possible domain would be the entire English language (though even that"s hard to define!).
# Instead, we could restrict the domain to, say, music, in which case SCALE becomes a relative ananagram (LACES is not in the same domain)
# but NOTE is not since it can produce TONE.
#
# Your task is to write a function that will read in the dictionary of a restricted domain and determine the relative ananagrams.
# Note that single letter words are, ipso facto, relative ananagrams since they cannot be "rearranged" at all.
# The dictionary will contain no more than 1000 words.
#
# The signature of your function should be:
# def solve(input: str) -> List[str]
#
# You may implement other functions called by your `solve` function if you wish.
# Input Spec
# Input will consist of a series of lines, with one or more words on each line, and each word separated by one or more spaces.
# Words can consist of uppercase and lowercase letters, and will not be broken across lines.
# Note that words that contain the same letters but of differing case are considered to be anagrams of each other,
# thus "tIeD" and "EdiT" are anagrams.
#
# Lines longer than 80 characters should be ignored, and words longer than 20 characters should be ignored.
#
# Output Spec
# The output should be a list of strings. Each element of the list should be a single word that is a relative ananagram
# in the input dictionary (with the word's case preserved).
# Words must be output in alphabetical order (case-insensitive).
#
# Sample Input & Output
# Input:
# ladder came tape soon leader acme RIDE lone Dreis peat
# ScAlE orb eye Rides dealer NotE derail LaCeS drIed
# noel  dire  Disk  mace  Rob  dries
#
# Output:
# ["derail", "Disk", "drIed", "eye", "ladder", "NotE", "soon"]


from typing import List
from collections import defaultdict

def solve(input: str) -> List[str]:
    words = []
    word_counts = defaultdict(int)
    original_words = {}

    for line in input.splitlines():
        if len(line) > 80:
            continue

        for word in line.split():
            if len(word) > 20:
                continue

            sorted_form = "".join(sorted(word.lower()))
            words.append(word)
            word_counts[sorted_form] += 1
            original_words[sorted_form] = word

    ananagrams = [word for word in words if word_counts["".join(sorted(word.lower()))] == 1]

    return sorted(ananagrams, key=lambda w: w.lower())

if __name__ == "__main__":
    input_text = """ladder came tape soon leader acme RIDE lone Dreis peat
            ScAlE orb eye Rides dealer NotE derail LaCeS drIed
            noel  dire  Disk  mace  Rob  dries"""
    print(solve(input_text)) # ["derail", "Disk", "drIed", "eye", "ladder", "NotE", "soon"]

    input_text2 =  """dire Disk verylongwordtobeignored something
            RIDE"""
    print(solve(input_text2)) # ["Disk", "something"]

