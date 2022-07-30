from collections import Counter

def wordSubsets(words1, words2):
    # create totalword
    totalword = {}
    for b in words2:
        tmp = Counter(b)
        for k, v in tmp.items():
            if k not in totalword:
                totalword[k] = v
            else:
                totalword[k] = max(v, totalword[k])

    output = []
    # for loop A in totalword
    for a in words1:
        tmp = Counter(a)
        if all([k in tmp and v <= tmp[k] for k, v in totalword.items()]):
            output.append(a)
    return output

if __name__ == '__main__':
    print(wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))
    # output = ["facebook","google","leetcode"]
    print(wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]))
    # output = ["apple","google","leetcode"]
    print(wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode", "ee"], words2 = ["lo", "eo"]))
    # output = ["google","leetcode"]