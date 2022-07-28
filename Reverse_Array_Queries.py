"""
Amazon OA Practice 1 - Reverse Array Queries
For a given array of integers, perform operations on the array. Return the resulting array after all
operations have been applied in the order given.
Each operation contains two indices. Reverse the subarray between those zero-based indices, inclusive.
"""

def performOperations(arr, operations):
    for i in range(len(operations)):
        new_rev_arr = arr[operations[i][0]: operations[i][1] + 1]
        new_rev_arr.reverse()
        new_arr = arr[:operations[i][0]] + new_rev_arr + arr[operations[i][1] + 1:]
        arr = new_arr
    return arr

if __name__ == '__main__':
    print(performOperations(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], operations = [[0, 9], [4,5], [3,6], [2, 7, [1, 8], [0, 9]]]))
    print(performOperations(arr = [1, 2, 3], operations = [[0, 2], [1, 2],[0, 2]]))