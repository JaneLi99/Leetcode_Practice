def checkDistances(s, distance):
    dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
            "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18,
            "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    simple_s = set(s)
    tmp = 0
    for letter in simple_s:
        idx_list = []
        for idx, l in enumerate(s):
            if letter == l:
                idx_list.append(idx)

        real_dist = abs(idx_list[0] - idx_list[1]) - 1
        idx_of_l = dict.get(letter)
        if real_dist == distance[idx_of_l]:
            tmp += 1

    if tmp == len(simple_s):
        return True
    return False

if __name__ == '__main__':
    print(checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    print(checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
