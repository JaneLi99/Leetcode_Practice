"""
M - DAQ OA 2

In the army, each soldier has an assigned rank. A soldier of rank X has to report (any) soldier of rank X + 1.
Many soldiers can report to the same superior. Write a function that, given an array ranks consisting of soldiers' ranks,
returns the number of soldiers who can report to some superior.

Examples:
    1. Given ranks = [3,4,3,0,2,2,3,0,0], your function should return 5, because:
       A. Three soldiers of rank 3 (ranks[0], ranks[2], ranks[6]) may report to a soldier of rank 4 (ranks[1]).
       B. Two soldiers of rank 2 may report to any soldier of rank 3.
    2. Given ranks = [4,2,0], your function should return 0.
    3. Given ranks = [3,4,3,0,2,2,3,0,0], your function soudl return 3, because:
       A. A soldier of rank 0 can report to a soldier of rank 1.
       B. Two soldier of rank 3 can report to any soldier of rank 4.
"""

def Soldier_Rank(ranks):
    res = 0
    freq_dict = {}

    for i in ranks:
        if i in ranks:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    for idx, (key, val) in enumerate(freq_dict.items()):
        if key + 1 in freq_dict:
            res += val

    return res

if __name__ == '__main__':
    print(Soldier_Rank(ranks = [4,4,3,3,1,0]))
    print(Soldier_Rank(ranks = [4,2,0]))
    print(Soldier_Rank(ranks = [3,4,3,0,2,2,3,0,0]))