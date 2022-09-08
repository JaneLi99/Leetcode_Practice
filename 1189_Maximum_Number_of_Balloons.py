def maxNumberOfBalloons(text):
    word = "balloon"
    res = 0
    while len(text) >= len(word):
        counts = 0
        for letter in word:
            if letter in text:
                text = text.replace(letter, '', 1)
                counts += 1

        if counts == len(word):
            res += 1
        else:
            return res

    return res

if __name__ == '__main__':
    print(maxNumberOfBalloons(text = "nlaebolko"))
    print(maxNumberOfBalloons(text = "loonbalxballpoon"))
    print(maxNumberOfBalloons(text = "leetcode"))
    print(maxNumberOfBalloons(text = "sdhajkfgeuirhqowdnjkdhqeuid"))