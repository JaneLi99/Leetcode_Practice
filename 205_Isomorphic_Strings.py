def isIsomorphic(s, t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

if __name__ == '__main__':
    print(isIsomorphic(s = "egg", t = "add"))
    print(isIsomorphic(s = "foo", t = "bar"))
    print(isIsomorphic(s = "paper", t = "title"))
