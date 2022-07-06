def simplifyPath(path):
    res = []
    path_split = path.split('/')
    for p in path_split:
        if p:
            if p == "..":
                if res:
                    res.pop()
            elif p == ".":
                continue
            else:
                res.append(p)

    result = '/' + '/'.join(res)
    return result

if __name__ == '__main__':
    print(simplifyPath(path = "/home/"))
    print(simplifyPath(path = "/../"))
    print(simplifyPath(path = "/home//foo/"))