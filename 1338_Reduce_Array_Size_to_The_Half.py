from collections import Counter

def minSetSize(arr):
    dict = Counter(arr)
    counts = sorted(dict.values(),reverse = True)
    count_num = counts[0]
    for j in range(len(counts)):
        if count_num >= len(arr) // 2:
            return j + 1
        else:
            count_num += counts[j + 1]

if __name__ == '__main__':
    print(minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))
    print(minSetSize(arr=[7, 7, 7, 7, 7, 7]))
