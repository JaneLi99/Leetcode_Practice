def nextGreatestLetter(letters, target):
    letters_length = len(letters)
    low = 0
    high = letters_length - 1

    if target < letters[low] or target >= letters[high]:
        return letters[low]

    while low <= high:
        middle = (low + high) // 2
        candidate = letters[middle]

        if target < candidate:
            high = middle - 1

        if target >= candidate:
            low = middle + 1

    return letters[low]

if __name__ == '__main__':
    print(nextGreatestLetter(letters = ["c","f","j"], target = "a"))
    print(nextGreatestLetter(letters = ["c","f","j"], target = "c"))
    print(nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))
