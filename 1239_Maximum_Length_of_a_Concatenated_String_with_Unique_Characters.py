def maxLength(arr):
    arr = [c for c in arr if len(c) == len(set(c))]
    ans = [set()]
    for a in arr:
        a = set(a)
        for b in ans:
            if a & b:
                continue
            ans.append(a | b)
    return max(len(c) for c in ans)

if __name__ == '__main__':
    print(maxLength(arr = ["un","iq","ue"]))
    print(maxLength(arr = ["cha","r","act","ers"]))
    print(maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]))