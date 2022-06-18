def strStr(haystack, needle):
    if needle in haystack:
        index = haystack.index(needle)
        return index
    else:
        return -1

if __name__ == '__main__':
    strStr(haystack = "hello", needle = "ll")
    strStr(haystack = "aaaaa", needle = "bba")