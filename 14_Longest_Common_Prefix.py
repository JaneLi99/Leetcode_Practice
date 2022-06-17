def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    length_of_shortest_word_sum = []
    for i in range(len(strs)):
        length_of_shortest_word = []
        for prefix in strs[i]:
            length_of_shortest_word.append(1)
        length_of_shortest_word_sum.append(sum(length_of_shortest_word))

    # minimum length of the word in the strs list
    min = 0
    for j in range(len(length_of_shortest_word_sum) - 1):
        if length_of_shortest_word_sum[j] < length_of_shortest_word_sum[j + 1]:
            min = length_of_shortest_word_sum[j]
        else:
            min = length_of_shortest_word_sum[j + 1]

    if len(strs) == 1:
        output = ''.join(strs)
        return output
    else:
        prefix_of_strs = []
        for b in range(1, min + 1):
            times = []
            letter = strs[0][:b]
            for a in range(len(strs)):
                # print('a:', a)
                if letter == strs[a][:b]:
                    letter = strs[a][:b]
                    times.append(1)

                if sum(times) == len(strs):
                    prefix_of_strs.append(strs[0][:b])
        # print('prefix_of_strs', prefix_of_strs)

        if len(prefix_of_strs) >= 1:
            last = len(prefix_of_strs) - 1
            output = prefix_of_strs[last]
            return output
        else:
            output = ''
            return output

if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))

    # Input: strs = ["flower", "flow", "flight"]
    # Output: "fl"
    #
    # Input: strs = ["dog", "racecar", "car"]
    # Output: ""