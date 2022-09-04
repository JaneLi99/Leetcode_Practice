"""
Record the algorithm problems I encountered during developing tools at Ford
The below script is called by searching part, and it is used to delete the extra file names.
It can check and simplify the multiple search files and make the program more efficient.
E.g. input = ["apple", "appleeee", "applejuice", "orange", "oranges", "banana"], output = [“apple", "orange", "banana”].
"""

def remove_dup(list):
    # Check if search strings have the substrings
    if len(list) == 1:
        return list
    if len(list) > 1:
        idx_1, idx_2 = 0, len(list) - 1
        idx_2_times = 0

        while idx_1 < idx_2:
            if list[idx_1] in list[idx_2]:
                list.remove(list[idx_2])
                idx_2 = len(list) - 1
                idx_2_times = 0

            elif list[idx_2] in list[idx_1]:
                list.remove(list[idx_1])
                idx_2 = len(list) - 1
                idx_2_times = 0

            else:
                idx_2_times = idx_2_times + 1
                idx_2 = idx_2 - 1

            if idx_2_times == len(list[idx_1:]) - 1:
                idx_1 = idx_1 + 1
                idx_2 = len(list) - 1
                idx_2_times = 0

    return list

# Test some cases
if __name__ == '__main__':
    print(remove_dup(list = ["apple", "appleee", "orange", "pears", "pear"]))
    print(remove_dup(list = ["aaabcd", "bcd"]))
