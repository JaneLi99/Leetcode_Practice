from collections import defaultdict

def groupAnagrams(strs):
    lookup = defaultdict(list)

    for s in strs:
        key = "".join(sorted(list(s)))
        lookup[key].append(s)

    return [l for l in lookup.values()]

if __name__ == '__main__':
    print(groupAnagrams(strs = ["eat","tea","tan"]))
    print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams(strs = [""]))
    print(groupAnagrams(strs = ["a"]))
