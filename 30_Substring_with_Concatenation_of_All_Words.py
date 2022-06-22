def findSubstring(s, words):
    length_of_words = 0
    for word in words:
        length_of_words = length_of_words + len(word)
    length_of_each_word = int(length_of_words / len(words))

    res = []
    for i in range(len(s) - length_of_words + 1):
        substring = s[i : i + length_of_words]

        split_substring = []
        for j in range(0, len(substring), length_of_each_word):
            split_substring.append(substring[j:j + length_of_each_word])

        for a in words:
            if a in split_substring:
                split_substring.remove(a)

        if len(split_substring) == 0:
            res.append(i)
    return res


if __name__ == '__main__':
    print(findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
    print(findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
    print(findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]))
    print(findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
    print(findSubstring(s="ababaab", words=["ab", "ba", "ba"]))
