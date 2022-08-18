def reverseWords(s):
    s_list = s.split(" ")

    i = 0
    while i < len(s_list):
        if len(s_list[i]) == 0:
            s_list.remove(s_list[i])
        else:
            i += 1

    s_list.reverse()
    res = " ".join(s_list)
    return res

if __name__ == '__main__':
    print(reverseWords(s = "the sky is blue"))
    print(reverseWords(s = "  hello world  "))
    print(reverseWords(s = "a good   example"))