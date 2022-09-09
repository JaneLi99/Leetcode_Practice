def maxRepeating(sequence, word):
    k = 0
    while True:
        if k * word not in sequence:
            return k - 1
        k += 1

if __name__ == '__main__':
    print(maxRepeating(sequence = "ababc", word = "ab"))
    print(maxRepeating(sequence = "ababc", word = "ba"))
    print(maxRepeating(sequence = "ababc", word = "ac"))
    print(maxRepeating(sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba", word = "aaaba"))
