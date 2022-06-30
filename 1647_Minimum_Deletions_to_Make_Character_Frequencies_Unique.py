import collections

def minDeletions(s):
    deletions = 0
    char_counts = collections.Counter(s)
    freq_set = set()
    for char, count in char_counts.items():
        while count > 0 and count in freq_set:
            count -= 1
            deletions += 1
        freq_set.add(count)

    return deletions


if __name__ == '__main__':
    print(minDeletions(s = "aab"))
    print(minDeletions(s = "aaabbbcc"))
    print(minDeletions(s = "ceabaacb"))
