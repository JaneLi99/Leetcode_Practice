def countAsterisks(s):
    if "|" not in s:
        count = 0
        for ele in s :
            if ele == "*":
                count += 1
        return count

    idx = []
    for i in range(len(s)):
        if s[i] == "|":
            idx.append(i)

    j = 0
    new_str = s[:idx[j]]
    while j < len(idx) - 2:
        new_str = new_str + s[idx[j + 1] + 1: idx[j + 2]]
        j = j + 2
    new_str = new_str + s[idx[-1]:]

    count = 0
    for a in new_str:
        if a == "*":
            count += 1
    return count

if __name__ == '__main__':
    print(countAsterisks(s = "l|*e*et|c**o|*de|"))
    print(countAsterisks(s = "iamprogrammer"))
    print(countAsterisks(s = "yo|uar|e**|b|e***au|tifu|l"))
    print(countAsterisks(s = "*||||**||*||**|**||*|||**"))