def uniqueMorseRepresentations(words):
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    morse_set = set()
    for word in words:
        morse_code = ""
        for i in range(len(word)):
            index = letter.index(word[i])
            morse_code += morse[index]
        morse_set.add(morse_code)

    return len(morse_set)

if __name__ == '__main__':
    print(uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
    print(uniqueMorseRepresentations(words = ["a"]))