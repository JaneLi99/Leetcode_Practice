def canConstruct(ransomNote, magazine):
    if ransomNote in magazine:
        return True

    counts = 0
    for letter in ransomNote:
        if letter in magazine:
            magazine = magazine.replace(letter, "", 1)
            counts += 1
    if counts == len(ransomNote):
        return True
    return False

if __name__ == '__main__':
    print(canConstruct(ransomNote = "a", magazine = "b"))
    print(canConstruct(ransomNote = "aa", magazine = "ab"))
    print(canConstruct(ransomNote = "aa", magazine = "aab"))
    print(canConstruct(ransomNote = "ab", magazine = "baa"))